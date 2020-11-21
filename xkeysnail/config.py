# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

import imp
sup = imp.load_source('sup', 'shortcut_support.py')

managed_apps = ['emacs','mate-terminal']

define_keymap(None, {
    K("Super-C-M-Space"): {
        K("F"): sup.find_or_launch(["firefox"]),
        K("S"): sup.find_or_launch(["mate-terminal"]),
        K("N"): sup.find_or_launch(["caja"]),
        K("Q"): sup.find_or_launch(["emacs"])
    }
}, "Apptivator")


define_keymap(lambda wm_class: wm_class.casefold() not in managed_apps,{
    K("Super-C"): K("C-C"),
    K("Super-V"): K("C-V"),
    K("Super-X"): K("C-X"),

    K("Super-F"): K("C-F"),
    K("Super-G"): K("C-G"),

    K("Super-S"): K("C-S"),
    K("Super-N"): K("C-N"),
    K("Super-O"): K("C-O"),
    K("Super-Q"): K("C-Q")

}, 'Default')

define_keymap(re.compile("emacs", re.IGNORECASE),{
    K("Super-S"): [K("C-x"), K("C-s")] # For some reason, s-s never arrives to Emacs
}, 'Emacs')
