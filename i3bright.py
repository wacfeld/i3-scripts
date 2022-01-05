#!/usr/bin/env python3
import sys, os
from i3grid import exshell
d = sys.argv[1]

val = None
if d == 'up':
    val = "+20"
elif d == 'down':
    val = "20-"
else:
    val = "+0"

os.system("brightnessctl set " + val)
max = int(exshell("brightnessctl max"))
cur = int(exshell("brightnessctl get"))

per = 'Brightness ' + str(round(cur / max * 100)) + "%"

os.system('notify-send -t 500 "' + per + '"')
