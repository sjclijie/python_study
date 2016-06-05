#!/usr/bin/python 
#-*- coding:utf-8 -*-


"""

标准类型：
    1. Integer
    2. Boolean
    3. Long integer
    4. Floating point real number
    5. Complex number
    6. String
    7. List  列表
    8. Tuple  元祖
    9. Dictionary 字典

其它内建类型：
    1. 类型
    2. Null对象(None) 只有一个值None
    3. 文件
    4. 集合/固定集合
    5. 函数/方法
    6. 模块
    7. 类

内部类型：
    1. 代码  编译过的python源代码片段，可以通compile()得到代码对象,可以被exec命令或者eval()内建函数来执行
    2. 帧    python的执行栈帧
    3. 跟踪记录   当异常发生时
    4. 切片       使用切片语法的时候会自动创建一个切片对象
    5. 省略       用于扩展切片语法中，起记号作用
    6. Xrange

"""


print type(42)

print type(type(42)) #所有的类型对象的类型都是type


a = [ 5, "a", -9.1 ]

b = a

#使用is 和 is not 判断两个变量是否指向同一个对象

print a is b  #True

print a is not b #False


"""
    内建函数：
        type
        isinstance
        cmp
        repr  返回一个对象的字符串表示  obj == eval( repr(obj) )
        str   可读性更好的字符串表示
"""
print str("hello world 李杰")


print isinstance( 1.23, ( int, long, float, complex ) )


"""
    if type(111) == type(0):
        print "111 is an int type"

"""

import types

#对象值比较
print type(111) == types.IntType
print type("string") == types.StringType

#对象身份比较
print type( 111 ) is types.IntType

#另一种用法
from types import IntType

print type( 111 ) is IntType

#使用isinstance()来判断类型
print isinstance( 111, int )

"""
    类型工厂函数：
        1. int()  long()  float()  complex()
        2. str()  unicode()  basestring()
        3. list() tuple()
        4. type()

        5. dict()
        6. bool()
        7. set()  frozenset()
        8. object()
        9. classmethod() 
        10. staticmethod()
        11. super()
        12. property()
        13. file()
"""

fd = open( "./README.md", "r" )
print isinstance( fd, file )












