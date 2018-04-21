#!/usr/bin/env python
# -*- coding: utf-8 -*-

#取指定索引范围的操作，可以通过切片（slice）完成，注意是下标从0开始，左开右闭。


name_list = ['machael','strone','david','guide']
print 'name list',name_list

# 取前三，0，1，2
print 'slice :3',name_list[:3]

# 指定索引范围
print 'slice 2:3',name_list[2:3]


# 倒数切片 取最后一位
print 'slice -1',name_list[-1]

# 倒数切片 从倒数第二取到尾部
print 'slice -2:-1',name_list[-2:]

# 倒数切片 指定区间,倒数第二个，左开右闭，
print 'slice -2',name_list[-2]


# 灵活的切片，根据下标可以随心所欲取值

range_list = range(100)
print 'range_list: ',range_list[60:88]

# 取前20个，每隔2个取一个
print '取前20个，每隔2个取一个 range_list: ',range_list[:20:2]

print '取中间指定10个，每隔5个取一个 range_list: ',range_list[30:40:5]

print '所有数，每5个取一个 range_list[::5]: ',range_list[::5]


# 字符串切片
cha_list = 'abcdefghijk'
print 'cha_list,取前两个: ',cha_list[:2]
print 'cha_list,隔3个取一个: ',cha_list[::3]