#!/usr/bin/env python3

import sys, tempfile, os
# from unimake import formatdir


if __name__ == '__main__':
    # get arguments
    program = sys.argv[1] # what program to use (ex. zathura)
    startdir = sys.argv[2] # where ranger will start (ex. ~/pdfs)
    tmpdir = sys.argv[3] # where file will be stored (ex. /tmp)

    # create temporary file for ranger
    tf = tempfile.NamedTemporaryFile(dir=tmpdir)
    tfname = tf.name
    
    # start ranger with a slew of options
    os.system("xterm -e 'exec ranger "
            "--cmd=\"shell i3-msg floating toggle\" " # make it an i3 floating window
            "--cmd=\"flat 2\" " # recursive flattening
            "--cmd=\"shell -f sleep 0.1; xdotool key z f minus e k space; sleep 0.01; xdotool key alt+g\" " # kludge! zf is filter in ranger
            "" + startdir + " --choosefile=" + tfname + "'")
    # explanation of the xdotool line:
    # sleep 0.1 : so that things have time to load, otherwise the keypresses aren't registered
    # zf : filter
    # -ek : open on enter; keep console open when pressing enter on directory
    # sleep 0.01 : more time to load
    # alt+g : put "cmap <A-g> move to=0" in your ranger config, goes to top of directory
    # os.system("xterm -e 'exec ranger " + startdir + " --choosefile=" + tfname + "'") # start ranger

    sel = tf.read().decode('UTF-8') # file selection
    # print(sel) # print selection to stdout

    if sel != '': # if quits file selection, it will be blank, and then we don't do anything
        os.system(program + " " + sel)
    
