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

print "#######################################\n"

#1. 将字符串第一个字符大写
print string.capitalize("hello world")
print "hello world".capitalize()


#2. 填充
print "|" + "hello world".center( 50 ) + "|"


#3. string.count(str, start, end)   str出现现string中的次数
print "hello world".count("o", 0, 8)

#4. string.decode( encoding='UTF-8', errors='strict|ignore|replace')   解码

#5. string.encode( encoding='UTF-8', errors='strict|ignore|replace' ) 编码 

#6. string.endswith(str,  beg=0, end=len(string)  ) 检查string是否以str结束
print "string".endswith("ing")

#7. string.expandtabs( tabsize = 8 ) 把tan转为空格 
print "Hello\tworld".expandtabs(4)

#8. string.find( str, beg=0, end=len(string))  str是否包含在string中, 返回首次出现的index
print "hello world".find("world")

#9. string.index( str, beg=0, end=len(string) ) 和find一样，如果不存在会抛出异常
try:
    print "hello world".index("world111")
except ValueError, e:
    print e

#10. string.isalnum() string不为空并且所有的字符都是字母或者数字 
print "helloworld_".isalnum()
print "hello1234".isalnum()

#11. string.isalpha() string不为空并且所有的字符都是字母
print "hello".isalpha()
print "h1234".isalpha()

#12. string.isdigit() string不为空并且所有的字符都是数字 
print "1234xxx".isdigit()
print "1234".isdigit()

print "1234".isalnum()

#13. string.islower() 所有字符都是小写
print "abcdefgH".islower()
print "abcdefg".islower()

#14. string.isupper()  所有字符都是大写
print "HELLO".isupper()

#15. string.isspace() 只包含空格
print "   ".isspace()

#16. string.join(str)  以string为分隔符，将str合并为新字符串
print "|".join("abc")

#17. string.ljust(with) 左对齐+填充长度
print "|" + "hello".ljust(50) + "|"
print "|" + "hello".rjust(50) + "|"

#18. lower upper 转换大小写
print "hello".upper()
print "HELLO".lower()

#19. string.lstrip()  去除空格
print "|"+"    he".lstrip() + "|"
print "|"+"he    ".rstrip() + "|"

#20. string.partition( str ) 从str出现的第一个位置起，把string切成一个三元祖
print "helloworld".partition("llo")
print "helloworld".partition("xxx")

print "1aahelloworldaa1".rpartition("aa") #从右边开始


#21. string.replace( str1, str2, num=string.count(str1) ) 把string中str1替换成str2
print "hello world".replace( "l", "i", 2 )

#22. string.rfind() 从字符串右边开始查找
print "aaaaastringa".find("a")
print "aaaaastringa".rfind("a")

print "aaaaastringa".index("a")
print "aaaaastringa".rindex("a")


#23. string.split( str="", num=string.count(str) ) 以str为分隔符切片
print "hello,world".split(",")

#24. string.splitlines( num=string.count("\n") ) 按行分隔
print "hello\nworld".splitlines()

#25. string.startswith( str, beg=0, end=len(string) ) 检查字符串string是否以str开头
print "helloworld".startswith("hello")

#26. string.strip([obj]) 同时执行lstrip和rstrip
print "|" + " helloworld ".strip() + "|"

#27. string.swapcase() 翻转大小写
print "HELLO world".swapcase()

#28. string.title()
print "hello world".title()

#29. string.zfill(with) 返回长度为with的字符串，不够前面补0
print "hello".zfill(10)



a = "abc"
print id(a)
a = a + "dec"
print id(a)

s = "abcdefg"

print "%sC%s" % ( s[0:2], s[3:] )

s = u"我是李杰"

print unicode( s )

print ord( u"李" )
print unichr( 26446 )

#=========== ===== ===== ===== ===== =====

# 1. 程序员出现字符串一定要使用unicode字符串
# 2. 不要使用str()函数，用unicode()代替
# 3. 不要使用过时的string模块
# 4. 不到必须时不要在程序中使用encode和decode unicode字符串，除非要写入文件或者数据库

# UnicodeError异常是在exceptions中定义的，ValueError的字类





























