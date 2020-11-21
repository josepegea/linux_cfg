import subprocess

def find_or_launch(args):
    """Activate the window or launch the program"""
    def find_or_launch_f():
        res, out = _run_wmctrl(['wmctrl', '-a', args[0], '-x'])
        if res == 0:
            return
        else:
            subprocess.Popen(args)
    return find_or_launch_f

def _run_wmctrl(args):
    try:
        with subprocess.Popen(["wmctrl"] + args, stdout=subprocess.PIPE) as p:
            output = p.communicate()[0].decode()[:-1]  # Drop trailing newline
            returncode = p.returncode
    except FileNotFoundError:
        return 1, 'ERROR: Please install wmctrl'

    return returncode, output
