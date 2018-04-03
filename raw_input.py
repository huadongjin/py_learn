#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'lesson:fun raw_input()'

name = raw_input('please input your name:')
print 'hello ', name ,'!'

adrress = raw_input('please input your adrress:')
print name , ', please mark sure your adrress:',adrress

flag = raw_input("yes/no")
print 'your choice:',flag, ' and adrress is:',adrress

if flag=='yes':
	print 'your adrress is:',adrress
else:
	print 'please input your adrress again!'

