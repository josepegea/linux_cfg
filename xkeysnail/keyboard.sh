#!/bin/sh

# Should be run as root.
# Using setuid

cd /home/jes/Code/linux_cfg/xkeysnail
xkeysnail config.py --watch --quiet

