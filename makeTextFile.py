#!/usr/bin/env python

import os

ls = os.linesep

all = []


while True:

    entry = raw_input(">")

    if entry == ".":
        break
    else:
        all.append( entry )


fobj = open("./aaa.txt","w")
fobj.writelines([ "%s %s" % ( x, ls ) for x in all])
fobj.close()

print "DONE"

