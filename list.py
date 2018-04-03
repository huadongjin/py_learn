#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "有序、可变数据类型list"

girls = ['poly','lili','luxi','小昭']
print len(girls)
print girls[0]
print girls[len(girls)-1]

print girls[-1]

girls.insert(4,'zhao ming')
print girls
print len(girls)

girls.append('zhu')
print girls
print len(girls)

girls.pop(2)
print girls
print len(girls)

# 二维数组
list_a = [999,'lili','story']
list_b = ['wuji','shiwang',list_a,'yinwang']
print list_a
print len(list_a)
print list_b
print len(list_b)

print list_b[2][1]