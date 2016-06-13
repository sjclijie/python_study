#!/usr/bin/python 
#encoding=utf8

# python的字典是用可变hash表实现的

#### 创建
dict1 = { "name":"jaylee", "age": 22}
dict2 = dict( (["x", "1"], ["y", "2"]) ) #python 2.2后支持
dict3 = {}.fromkeys( ("xx", "yy"), "default" ) #python 2.3支持

print dict1
print dict2
print dict3

#### 访问
#1. 遍历
for key in dict1.keys():
    print "key=%s, value=%s" % ( key, dict1[key] )

# 2. 从python2.2开始，可以使用迭代器访问类序列对象
for key in dict1:
    print "key=%s, value=%s" % ( key, dict1[key] )

# 3. has_key 检查是否存在想关key ( 在以后的版本中将被废弃)
print dict1.has_key( "name" )
print dict1.has_key( "class" )

# 4. 建议使用in 和 not in 来判断 ( python2.3以前没有bool常量，存在返回1， 不存在返回0)
print "name" in dict1
print "class" in dict1

# 5.
dict4 = {1:"xyz", 3.2:"abc", "1":456}

#### 删除字典元素和字典

del dict4["1"]
print dict4

del dict4
try:
    print dict4
except NameError, e:
    print e

