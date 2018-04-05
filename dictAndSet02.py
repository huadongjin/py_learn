#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '-------set------'

ss = set([1,2,3,4,5,5])
print "ss is:",ss

ss.add(6)
ss.add(7)
ss.add(5)
print "ss add 5,6,7 ss:",ss

ss.remove(1)
print "ss remove 1 ss:",ss

# ss.remove(8)
print "ss remove unexists num 8 ss:",ss

print u'---------------function checkAndAddSpecNuber-------'
flag = True
number_temp = -1
for s in ss:
	while s == 6:
		number_temp = s
		flag = False
		break
	print "for loop in set,and s:",s
if flag == True:
	print "do nothing!"
else:
	print "remove spec number: ",number_temp
	ss.remove(number_temp)
print "finally, ss is:",ss
print u'---------------function end------------------------'

print u'set 和 dict类似，也是一组key的组合，最常见的的key是字符串，但set是无序且不重复的key，且不存储Value'