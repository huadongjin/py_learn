#!/usr/bin/env python
# -*- coding: utf-8 -*-

print u"有序集合：可变list和不可变tuple"

the_count = [1,2,3,4,5,6]
print "count 0 is: %d " % the_count[0]

print "count len is: %d " % len(the_count)

# for x in xs:
for num in the_count:
	print "now num is: %d " % num

double_count = [1,2,3,[11,22],4]
# for count in counts and add condition check
i = 0
for dc in double_count:
	if i == 3:
		pass
	else:
		print "double count is: %d " %dc
	i = i + 1

print '不可变tuple'
tuple_count = ('ddW','we','try','it')
# for tc in tuple_count
#	print "tc is: %s " %tc
print "tc is: %s " % tuple_count[1]