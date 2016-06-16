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

#清空
dict3.clear()
print dict3

# 删除并返回 dict2.pop( key, default )
print dict2.pop("x")

print "#############"

# 内建函数
dict1 = { "name": "lijie", "port":8080 }
dict2 = { "name": "lijie", "port":80 }

print cmp( dict1, dict2 )

# cmp比较过程： 1. 比较字典长度， 2. 比较字典的键  3.比较字典的值


# copy 浅复制
dict1 = dict( x=1, y=2 )
dict2 = dict1.copy()
print dict2
dict2["x"] = 100
print dict2

# hash() 是否可以作为字典的键, 返回object的hash
print hash(())

# keys() 返回一个列表，包含字典中的所有键
# values() 返回一个列表，包含字典中的所有值
# items()  返回一个包含所有键值元组的列表
print dict2.keys()
print dict2.values()
print dict2.items()

# dict.get( key, None ) 获取dict中的key的值
print dict2.get( "name", "lijie" )

# dict.update( dict2 ) 用dict2中的键值更新dict
dict2.update( {"x":10000, "name":"jaylee"} )
print dict2

# {}.fromkeys("xxxx", default)
print {}.fromkeys( ("name",), "default")
print {}.fromkeys("name", "default")

# iterkeys, iteritems, itervalues
for key in dict2.iteritems():
    print key

for key in dict2.iterkeys():
    print key

for key in dict2.itervalues():
    print key








