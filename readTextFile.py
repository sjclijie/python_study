#!/usr/bin/env python

fname = raw_input("Enter Filename:")

print 


try:

    fobj = open( fname, "r")


    for eachLine in fobj:
        print eachLine

except IOError, e:
    print "file open error:", e

else:

    fobj.close()



