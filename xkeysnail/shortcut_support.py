import subprocess

def find_or_launch(appname):
    """Activate the window or launch the program"""
    def find_or_launch_f():
        matching_windows = find_matching_windows(appname)
        ordered_windows = get_ordered_windows()
        topmost_window = find_topmost_window(matching_windows, ordered_windows)
        if not topmost_window:
            return # See FIXME below

        res, out = _run_wmctrl(['wmctrl', '-a', topmost_window, '-i'])
        if res == 0:
            return
        else:
            # FIXME: Disabling execution of programs as root
            # We need to execute them as the user
            # subprocess.Popen(appname)
            return
    return find_or_launch_f

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
    matches = [line.split()[0] for line in windows if name.lower() in line.split()[2].lower()]
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
