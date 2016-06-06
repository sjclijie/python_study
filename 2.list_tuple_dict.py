#!/usr/bin/python
# -*- coding=utf8 -*-

"""
    1. 成员关系  in, not in
    2. 连接操作符 +
    3. 重复操作符 seq * copise_int
    4. 切片 [], [ starting_index : ending_index ], [::]
"""

#字符串反转
a = ["a", "b", "c", "d"]
b = "hello world"
print a[::-1]
print b[::-1]

#每次去掉最后一个字符
c = "sjclijie"
i = -1

for i in [None] + range( -1, -len(c), -1 ):
    print c[:i]

#列表连接操作也可以使用extend, 但extend返回None
l1 = [1,2,3]
l2 = [4,5,6]

print l1.extend( l2 ) #None
print l1  #[1,2,3,4,5,6]

    
