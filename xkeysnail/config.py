# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

import imp
sup = imp.load_source('sup', 'shortcut_support.py')

managed_apps = ['emacs','mate-terminal']

define_keymap(None, {
    K("Super-C-M-Space"): {
        K("F"): sup.find_or_launch("firefox"),
        K("S"): sup.find_or_launch("mate-terminal"),
        K("N"): sup.find_or_launch("caja"),
        K("K"): sup.find_or_launch("slack"),
        K("M"): sup.find_or_launch("evolution"),
        K("U"): sup.find_or_launch("whatsapp"),
        K("R"): sup.find_or_launch("jira"),
        K("C"): sup.find_or_launch("chrome"),
        K("I"): sup.find_or_launch("youtube-music"),
        K("P"): sup.find_or_launch("dbeaver"),
        K("D"): sup.find_or_launch("calendar"),
        K("E"): sup.find_or_launch("figma"),
        K("X"): sup.find_or_launch("libreoffice-calc"),
        K("W"): sup.find_or_launch("atril"),
        K("Y"): sup.find_or_launch("yed"),
        K("Q"): sup.find_or_launch("emacs")
    }
}, "Apptivator")

define_keymap(None, {
    K("LM-GRAVE"): K("RM-GRAVE"),
    K("LM-KEY_1"): K("RM-KEY_1"),
    K("LM-KEY_2"): K("RM-KEY_2"),
    K("LM-KEY_3"): K("RM-KEY_3"),
    K("LM-LEFT_BRACE"): K("RM-LEFT_BRACE"),
    K("LM-RIGHT_BRACE"): K("RM-RIGHT_BRACE"),
    K("LM-APOSTROPHE"): K("RM-APOSTROPHE"),
    K("LM-BACKSLASH"): K("RM-BACKSLASH")
}, "AltChars")

define_keymap(lambda wm_class: wm_class.casefold() not in managed_apps, {
    K("Super-RIGHT"): K("END"),
    K("Super-LEFT"): K("HOME"),
    K("Super-Shift-RIGHT"): K("Shift-END"),
    K("Super-Shift-LEFT"): K("Shift-HOME"),
    K("Super-DOWN"): K("C-END"),
    K("Super-UP"): K("C-HOME"),
    K("Super-Shift-DOWN"): K("Shift-C-END"),
    K("Super-Shift-UP"): K("Shift-C-HOME"),
    K("M-LEFT"): K("C-LEFT"),
    K("M-RIGHT"): K("C-RIGHT"),
    K("M-Shift-LEFT"): K("C-Shift-LEFT"),
    K("M-Shift-RIGHT"): K("C-Shift-RIGHT")
}, "Cursor")

define_keymap(lambda wm_class: wm_class.casefold() not in managed_apps,{
    K("Super-C"): K("C-C"),
    K("Super-V"): K("C-V"),
    K("Super-X"): K("C-X"),
    K("Super-A"): K("C-A"),

    K("Super-Z"): K("C-Z"),
    K("Super-Shift-Z"): K("C-Shift-Z"),

    K("Super-F"): K("C-F"),
    K("Super-E"): K("C-F"), # Enter selection
    K("Super-G"): K("C-G"),
    K("Super-Shift-G"): K("C-Shift-G"),

    K("Super-S"): K("C-S"),
    K("Super-Shift-S"): K("C-Shift-S"),
    K("Super-N"): K("C-N"),
    K("Super-Shift-N"): K("C-Shift-N"),
    K("Super-O"): K("C-O"),
    K("Super-P"): K("C-P"),
    K("Super-W"): K("C-W"),
    K("Super-Q"): K("C-Q"),

    K("Super-B"): K("C-B"), # Bold
    K("Super-I"): K("C-I"), # Italic
    K("Super-U"): K("C-U"), # Underline

    K("Super-T"): K("C-T"), # New tab
    K("Super-R"): K("C-R"), # Reload

    K("Super-RIGHT_BRACE"): K("C-RIGHT_BRACE"), # Zoom in
    K("Super-SLASH"): K("C-SLASH"), # Zoom out
    K("Super-KEY_0"): K("C-KEY_0"), # Zoom default
    K("Super-KEY_1"): K("C-KEY_1"),
    K("Super-KEY_2"): K("C-KEY_2"),
    K("Super-KEY_3"): K("C-KEY_3"),
    K("Super-KEY_4"): K("C-KEY_4"),
    K("Super-KEY_5"): K("C-KEY_5"),
    K("Super-KEY_6"): K("C-KEY_6"),
    K("Super-KEY_7"): K("C-KEY_7"),
    K("Super-KEY_8"): K("C-KEY_8"),
    K("Super-KEY_9"): K("C-KEY_9"),

    K("Super-L"): K("C-L") # Goto line, go to location...

}, 'Default')

define_keymap(re.compile("emacs", re.IGNORECASE),{
    K("Super-S"): [K("C-x"), K("C-s")] # For some reason, s-s never arrives to Emacs
}, 'Emacs')

define_keymap(re.compile("terminal", re.IGNORECASE),{
    K("Super-C"): K("C-Shift-C"),
    K("Super-V"): K("C-Shift-V"),
    K("Super-A"): K("C-Shift-A"),

    K("Super-F"): K("C-Shift-F"),
    K("Super-E"): K("C-Shift-F"), # Enter selection
    K("Super-G"): K("C-Shift-H"),
    K("Super-Shift-G"): K("C-Shift-G"),

    K("Super-N"): K("C-Shift-N"),
    K("Super-Q"): K("C-Shift-Q"),

    K("Super-T"): K("C-Shift-T"), # New tab
    K("Super-W"): K("C-Shift-W"), # Close tab
    K("Super-Shift-W"): K("C-Shift-Q"), # Close window

    K("Super-RIGHT_BRACE"): K("C-Shift-RIGHT_BRACE"), # Zoom in
    K("Super-SLASH"): K("C-Shift-SLASH"),             # Zoom out
    K("Super-KEY_0"): K("M-KEY_0"),                # Go to tab N
    K("Super-KEY_1"): K("M-KEY_1"),
    K("Super-KEY_2"): K("M-KEY_2"),
    K("Super-KEY_3"): K("M-KEY_3"),
    K("Super-KEY_4"): K("M-KEY_4"),
    K("Super-KEY_5"): K("M-KEY_5"),
    K("Super-KEY_6"): K("M-KEY_6"),
    K("Super-KEY_7"): K("M-KEY_7"),
    K("Super-KEY_8"): K("M-KEY_8"),
    K("Super-KEY_9"): K("M-KEY_9"),

    K("Super-M-LEFT"): K("C-PAGE_UP"),    # Tab left
    K("Super-M-RIGHT"): K("C-PAGE_DOWN"),  # Tab right

    K("Super-RIGHT"): K("END"),
    K("Super-LEFT"): K("HOME")

}, 'Terminal')

define_keymap(re.compile("firefox", re.IGNORECASE),{
    # K("Super-Shift-I"): K("C-Shift-I"),   # Inspect
    K("Super-LM-I"): K("C-Shift-I"),   # Inspect
    K("Super-M-LEFT"): K("C-PAGE_UP"),    # Tab left
    K("Super-M-RIGHT"): K("C-PAGE_DOWN")  # Tab right
}, 'Firefox')

define_keymap(re.compile("webapp", re.IGNORECASE),{
    # K("Super-Shift-I"): K("C-Shift-I"),   # Inspect
    K("Super-LM-I"): K("C-Shift-I"),   # Inspect
    K("Super-M-LEFT"): K("C-Shift-TAB"),    # Tab left
    K("Super-M-RIGHT"): K("C-TAB")  # Tab right
}, 'Firefox-WebApps')

define_keymap(re.compile("chrome", re.IGNORECASE),{
    # K("Super-Shift-I"): K("C-Shift-I"),   # Inspect
    K("Super-LM-I"): K("C-Shift-I"),   # Inspect
    K("Super-M-LEFT"): K("C-PAGE_UP"),    # Tab left
    K("Super-M-RIGHT"): K("C-PAGE_DOWN")  # Tab right
}, 'Chrome')

define_keymap(re.compile("caja", re.IGNORECASE),{
    K("Super-M-LEFT"): K("C-PAGE_UP"),    # Tab left
    K("Super-M-RIGHT"): K("C-PAGE_DOWN")  # Tab right
}, 'Caja')

define_keymap(None, {
    K("Super-H"): sup.hide_current_app_windows,
    K("Super-Shift-W"): sup.close_current_window
}, "GlobalActions")
