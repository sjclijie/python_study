#!/usr/bin/python
#encoding=utf8
__author__ = 'Jaylee'

# python 2.3开始引入集合, 可继承Set 和 ImmuteablSet
# python 2.4可用集合类型

# 1. 创建  set()和frozenset() 工厂方法创建

s1 = set("cheeseshop")
print s1
print type(s1)

#不可变集合
s2 = frozenset(['c', 'e', 'h', 'o', 'p', 's'])
print s2
print type(s2)

print s1 == s2

# in, not in
print "s" in s1

# add, update, remove
s1.add( "abc" )
print s1

s1.remove("c")
print s1

del s1
del s2

#集合关系
# in, not in

#集合等价/不等价
# s == t , s != t

#子集超集
#子集 <, <=
#超集 >, >=

print set("abc") <= set("abcd") # True

#联合 |
print set("abc") | set("bcd") # a, b, c, d

#交集
print set("abc") & set("bcd") # c, b

#差集
print set("abc") - set("bcd") # a

#对称差集 异或
print set("abc") ^ set("bcd") # a, d

#集合类型操作符
#update
s1 = set("abc");
s1 |= set("bcd");
print s1 # a, b ,c ,d

#等价

s1 = set("abc")
s1.update( set("bcd") )
print s1 # a, b, c, d


# &=  交集
s1 = set("abc")
s1 &= set("bcd")
print s1 # c, b

s2 = frozenset("abc")
s2 &= set("bcd")
print s2 # frozenset( [ c, b] )

# -= 差集
s3 = set("abc")
s3 -= set("bcd") 
print s3 # a # 异或 s4 = set("abc") s4 ^= set("bcd") print s4 #a, d ##################### print len(s4)
#set()和frozenset()工厂函数分别用来生成可变和不可变集合。如果不提供任何参数，默认会生成空集合
#如果提供一个参数，则该参数必须是可迭代的,如一个文件或者一个字典

f = open("./number", "w")
for i in range(10):
    f.write( "%d\n" % i)
f.close()

f = open("./number", "r")
s4 = set(f)
print s4



# 内建方法
# s.issubset(t) s是否为t的子集
print set("abc").issubset(set("abc")) #True
print set("abcd").issubset(set("abc")) #False

# s.issuperset(t) s是否为t的超集
print set("abcd").issuperset( set("abc") ) #True

# s.union(t) 返回s和t的并集
print set("abc").union( set("bcd") ) #abcd

# s.intersection(t) 返回交集
print set("abc").intersection(set("bcd")) #bc

# s.difference(t) 差集
print set("abc").difference(set("bcd")) #a

# s.symmetric_difference(t) 对称差集
print set("abc").symmetric_difference("bcd") #a,d

# s.copy 浅复制
s1 = set("abc")
s2 = s1.copy()
s2.add("abc")
print s1, s2

################# 仅适用于可变集合
# 1. s.update(t) 用t修改s
s1 = set("abc")
s1.update(set("bcd"))
print s1 # a,b,c,d

# 2. s.intersection_update(t) 修改s
s1 = set("abc")
s1.intersection_update(set("bcd"))
print s1 #b,c

# 3. s.difference_update(t)
# 4. s.symmetric_difference_update
# 5. s.add(obj)
# 6. s.remove(obj)
s1 = set("abc")
s1.discard("a")
print s1
s1.discard("aaaa")

# 7. s.pop()
# 8. s.clear()





















