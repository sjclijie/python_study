#!/usr/bin/python 
#encoding=utf8

CODEC="utf-8"
FILE = "test.txt"
s = u"我是李杰"

f = open( FILE, "w" )
f.write( s.encode(CODEC) )
f.close()

f = open( FILE, "rb")
bytes_int = f.read()
f.close()
print bytes_int.decode( CODEC )


