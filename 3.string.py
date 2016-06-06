#!/usr/bin/python 
# -*- coding=utf8 -*-

"""
Python 有三类字符串：
    1. 通常意义的字符串( str )
    2. unicode字符串 ( unicode )
    3. 抽象类 ( basestring ) 不能被实例化
"""

s = "hello world"

#切片
print s[:5]

print s[6:]

print s[2]

#字符串长度
print len(s)
print s[0:len(s)]

#成员操作符 in,  not in
print "a" in s
print "he" in s 
print "ss" not in s 

#大小写 
import string
print string.uppercase
print string.lowercase
print string.letters
print string.digits

print string.lower("HELLO world")
print "XXX".lower()

print string.upper("hello WORLD")
print "xxx".upper()

print string.capwords("hello world sjclijie")

#字符串连接
print 'http://www.baidu.com' ':8080' '/cgi-bin/hello.py'

#如果一个普通字符串和一个unicode字符串相连接，python会在连接操作前将普通字符串转成unicode字符串
print "hello" u'我是unicode字符串'

#字符串格式化
"""
    %c 转成ascii
    %r 优先使用repr()
    %s 优先使用str()

    其它的都一样...
"""

print "%c %r %s" % (65, "hello", "world")

#也可以使用字典类型

print "%(name)s %(age)d" % {"age":22, "name":"sjclijie" }

#模板字符串
from string import Template
#Template.substitute()  在缺少key的时候会报错 KeyError
#Template.safe_substitute() 

s = Template("There are ${how} ${lang} Quotation Symbols.")

print s.substitute(lang="python", how="xxxs")
print s.safe_substitute( lang="python" )


#原始字符串
print r"\n"
print  "\n"

f = open( r"./README.md", 'r')
print f.readline()
f.close()

import re

m = re.search( r"\\[rtvnf]", r"hello world!\n" )
print m

#Unicode字符串
print u'abc\u1234\n'




###### 内建函数

# 1.cmp 按ascii比较大小

print cmp("a", "A")
print ord("A") #65
print ord("a") #97

# 2.len
print len("hello world")

# 3.max min
print max("abc")
print min("abc")

# 4.enumerate
s = "hello world" 

for i in range(0, len(s)):
    print i, s[i]

for index, text in enumerate(s):
    print index, text


# 字符串类型函数

print isinstance( u"\0xAB", str )
print isinstance( u"\0AB", unicode )
print isinstance( u"\00AB", basestring )


#chr ord unichr 
print chr(65)
print ord("A")

try:
    print unichr(1236)
    print unichr(123456)
except ValueError, e:
    print e
else:
    print unichr(1111)
finally:
    print unichr(2222)


print ord( u"\u1235" )

print unichr(4661)


########## 内建函数










































