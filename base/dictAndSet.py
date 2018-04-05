#!/usr/bin/env python
# -*- coding: utf-8 -*-

print u"----dict and set-----"

dd = {'xiaoming':100,'xiaofang':88,'xiaoxx':78}
print "who record is top ?"
record01 = dd['xiaofang']
record02 = dd['xiaoming']
record03 = dd['xiaoxx']
rec_list = [record01,record02,record03]
rec_temp = 0
for rec in rec_list:
	if rec > rec_temp:
		rec_temp = rec
print "the top record is:",rec_temp

print "get xiaozhu record:", dd.get("xiaozhu","no record")

print "add xiaozhu record 99!"
dd["xiaozhu"] = 99
print "try again!"
print "get xiaozhu record:", dd.get("xiaozhu","no record")

print "now delete xiaoxx record::"
dd.pop("xiaoxx")
print "check,get xiaoxx record:",dd.get("xiaoxx","no record")

print '-------function------return the top record and name-----'
d_temp = 0
d_name = 'none'
best_name = 'somebody'
for d in dd:
	d_name = d
	record = dd.get(d_name)
	print "name and record is: %s,%s " % (d_name,record)
	if record > d_temp:
		best_name = d_name
		d_temp = record
print "the top record is:",best_name,d_temp
print '-------function------end---------------------------------'

print u'dict 类似java的map,通过键值对存储，查找速度极快，缺点是费内存。'
print u'跟list不同，dict不会随着key的增多 查找速度变慢，但list占用空间小，浪费内存很少'
print u'so , dict是通过空间换时间的一种方法。'