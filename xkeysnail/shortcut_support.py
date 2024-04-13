import subprocess

app_windows = {
    "calendar": "crx_kjbdgfilnfhdoflbpgamdcdgpehopbep.Google-chrome",
    "chrome": "google-chrome.Google-chrome"
}

app_cmds = {
    "firefox": "gtk-launch firefox",
    "evolution": "gtk-launch org.gnome.Evolution",
    "jira": "gtk-launch webapp-Jira9090",
    "whatsapp": "gtk-launch webapp-WhatsApp0114",
    "figma": "gtk-launch webapp-Figma5770.desktop",
    "dbeaver": "gtk-launch _usr_share_dbeaver-ce_",
    "libreoffice-calc": "gtk-launch libreoffice-calc",
    "chrome": "gtk-launch google-chrome"
}

def find_or_launch(appname):
    """Activate the window or launch the program"""
    def find_or_launch_f():
        matching_windows = find_matching_windows(appname)
        ordered_windows = get_ordered_windows()
        topmost_window = find_topmost_window(matching_windows, ordered_windows)
        if not topmost_window:
            _launch(appname)
            return

        res, out = _run_wmctrl(['wmctrl', '-a', topmost_window, '-i'])
        if res == 0:
            return
    return find_or_launch_f

# We need to execute the corresponding command as the user
# It should work with:
# sudo -u jes -i nohup cmd_line &> /dev/null &
# But it has some edge cases:
#   - emacs doesn't seem to work
#   - caja launches another process, not connected to the normal one
#   - Slack, being a snap, seems to act weirdly
# So we only do it with a whitelist of applications and sanctioned commandlines.
def _launch(appname):
    cmdline = app_cmds.get(appname)
    if cmdline:
        print("Launching %s" % appname)
        final_cmdline = "sudo -u jes -i -- nohup %s > /dev/null 2>&1 &" % cmdline
        print("Executing: %s" % final_cmdline)
        subprocess.run(final_cmdline, shell=True)
    else:
        print("Not launching %s" % appname)

def _run_wmctrl(args):
    try:
        with subprocess.Popen(["wmctrl"] + args, stdout=subprocess.PIPE) as p:
            output = p.communicate()[0].decode()[:-1]  # Drop trailing newline
            returncode = p.returncode
    except FileNotFoundError:
        return 1, 'ERROR: Please install wmctrl'

    return returncode, output

def find_matching_windows(name):
    windows = _run_wmctrl(["wmctrl", "-l", "-x"])[1].splitlines()
    window_name = app_windows.get(name, name)
    matches = [line.split()[0] for line in windows if window_name.lower() in line.split()[2].lower()]
    return matches

def get_ordered_windows():
    output = subprocess.run(["xprop", "-root"], capture_output=True, text=True).stdout
    window_line = next(line for line in output.splitlines() if "_NET_CLIENT_LIST_STACKING(WINDOW)" in line)
    window_ids = window_line.split("window id # ")[1].split(", ")[1:]
    return window_ids

def find_topmost_window(best_windows, ordered_windows):
    if not best_windows or not ordered_windows:
        return None

    reversed_ordered_windows = ordered_windows[::-1]
    best_window_ids = [int(window, 16) for window in best_windows]

    for window in reversed_ordered_windows:
        if int(window, 16) in best_window_ids:
            return window

    return None
