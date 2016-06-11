#!/usr/bin/python
#encoding=utf8

aList= ["abc",123, None]
print aList

print list( "hello world") #["h", "e", "l", "l", "o", "" ...]

#访问 切片
print aList[0:2]

aList.append(["abc", "def"])

print aList[3][1]

#删除
del aList[3][1]
print aList
aList.remove("abc")
print aList

#成员关系
print 123 in aList

bList = ["a", "b", "c"]
print aList + bList
aList.extend( bList )
print aList

try:
    aList + "xx"
except TypeError, e:
    print e


print aList * 2

print len( aList )


# ==================================  相关函数

print aList

print sorted( aList )
for i in reversed( aList ):
    print i


for index, item in enumerate( aList ):
    print index, item

bList = [1,2,3,4,5]
print sum(bList)

aTuple= tuple( bList )
print aTuple

print [ id(x) for x in aTuple ]

print aList
bList = list( aList )
print aList, bList
print id(aList), id(bList)
aList[0] = "111111111";
print aList, bList
print id(aList), id(bList)

print dir( list )

# ==================================  内建函数

#1. list.append( obj ) 添加一个obj, 参数可以是任何类型
aList.append(0)
print aList
# 2. list.count(obj) obj在list中出现的次数
print aList.count("a")
# 3. list.extend( seq ) 参数是序列
aList.extend( ("1",2,3,4,5) )
print aList

# 4. list.index( obj, i=0, j=len(list) ) 返回list[k] = obj 时，k的值
print aList.index("1")

# 5. list.insert(index, obj ) 在索引index处插入obj
bList = [0,1,2,3,4,5]
bList.insert(0, "a")
print bList

# 5.list.pop( index = -1 ) 删除一个对象并返回这个对象，  默认是最后一个
print bList.pop()
print bList

# 6. list.remove(obj) 从list中删除obj
bList.extend([1,2,3,4])
print bList
bList.remove(2)
print bList

#7. list.reverse() 反转列表
bList.reverse()
print bList

#8. list.sort( func=None, key=None, revese=False ) 排序
bList.sort()
print bList


#默认为浅拷贝

person = ["name", ["saving", 100.00]]

hubby = person[:]
hubby = person[1][1] = 50.00

wifey = list( person )

print [ id(x) for x in person, hubby, wifey ]

#深拷贝
import copy
aaa = copy.deepcopy( person )
aaa[1][1] = 10.00
print aaa
print person














