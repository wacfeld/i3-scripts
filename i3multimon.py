#!/usr/bin/env python3
import os, subprocess, json
import time
from i3grid import *

# get display names
# xrandr = exshell('xrandr').split('\n')
# displays = [x.split(' ')[0] for x in list(filter(lambda x: x.split(' ')[1] == 'connected', xrandr))]
# print(displays)
# ^^ don't actually need, just get from visible workspaces

# get visible workspaces
spaces = spaceinfo()
visible = list(filter(lambda x: x["visible"], spaces))
print(visible)
nums = [int(x['name']) for x in visible]
displays = [x['output'] for x in visible]
print(nums)

if __name__ == '__main__':
    d = sys.argv[1]

    # if d == 'init': # mod+Home
    #     spacing = sys.argv[2] # how far apart to put each monitor
    #     os.system('i3-msg 

    change = None
    if d == 'next':
        change = 1
    elif d == 'prev':
        change = -1

    # we do everything in parallel to avoid the shift-overwrite error
    # for some reason Popen with the list works on negatives while os.system and manually typing it does not
    newnums = [x + change for x in nums]
    for i in range(len(displays)):
        subprocess.Popen(['i3-msg', 'workspace ' + str(nums[i])]) # select the proper monitor
        subprocess.Popen(['i3-msg', 'workspace tmp' + str(nums[i])]) # move to temp so no clobbering
    for i in range(len(displays)):
        subprocess.Popen(['i3-msg', 'workspace tmp' + str(nums[i])]) # run through again
        subprocess.Popen(['i3-msg', 'workspace ' + str(newnums[i])]) # go to new workspace
        os.system('i3-msg move workspace to output ' + str(displays[i]))
    for i in range(len(displays)):
        subprocess.Popen(['i3-msg', 'workspace ' + str(newnums[i])]) # focus new workspaces after shuffling things around
