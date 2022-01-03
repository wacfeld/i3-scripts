#!/usr/bin/env python3

# TODO visual aide
# TODO moving windows
# TODO multiple displays
import os, json, subprocess
import sys

# get output of shell command
def exshell(comm):
    res = subprocess.run(comm.split(' '), stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n')
    return res

# get all workspace info
def spaceinfo():
    return json.loads(exshell('i3-msg -t get_workspaces'))

# get current workspace
def getspace():
    spaces = spaceinfo()
    foc = list(filter(lambda x : x["focused"], spaces))[0]["name"]
    return foc

# move in a cardinal direction
def move(name, d):
    spl = name.split('_')
    x = int(spl[1])
    y = int(spl[2])
    if d == 'up':
        y -= 1
    elif d == 'down':
        y += 1
    elif d == 'left':
        x -= 1
    elif d == 'right':
        x += 1

    return "_"+str(x)+"_"+str(y)


if __name__ == '__main__':
    d = sys.argv[1]
    name = getspace()
    newname = move(name, d)

    os.system("i3-msg workspace "+newname)
