#!/usr/bin/env python
# -*- coding: utf-8 -*-

# condition check and for loop
print u'condition check:if else'

age = 29
if age >=18:
	print "your age is", age ," your are adult"
else:
	print "your age chilren"


your_age = 6
if your_age > 18:
	print "your age is:", your_age
elif your_age > 6:
	print "teenager"
else:
	print 'your are kid'

# for loop
print u'for loop: for a in as'

names = ['apollo','vtamin','thinkpad']
for name in names:
	print "current name is %s:" %name
print u'------------------tips--------------------------------'
print u'才发现...字符串和变量拼接时候，用不用占位符有区别：'
print u'1、用占位符的时候，不需要逗号间隔，直接是%s %变量；'
print u'2、不用占位符的时候，需要逗号间隔，否则不符合语法要求；'
print u'3、单变量的时候，直接字符串拼接即可，没必要使用占位符；'
print u'----------------------------------------------------'

print u" range()"
for name in names:
	print "currint name is: ", name

sum = 0
for x in xrange(1,101):
	sum = sum + x
print sum	


print u"while loop"
count = 0
num = 99
while num > 33:
	count = count + num 
	num = num - 3
print count