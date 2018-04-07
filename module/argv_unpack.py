#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

# unpack解包，将随同文件传递进来的每个参数赋值给每一个变量，称为解包。即把
# argv中的东西解包，将所有的参数依次赋值给左边的这些变量。
script,first_arg, sec_arg, third_arg = argv

print "your script is:",script
print "the first variable is:",first_arg
print "the second variable is:",sec_arg
print "the third variable is:",third_arg

flag = raw_input("do you understand this module?  yes/no \n")
if flag == 'yes':
	print "well done!"
else:
	print "learn it again!"

# 需要注意 python xx.py first second third  
# python 命令之后就是是参数了，对于sys模块来说，需要解包的argv的参数
# 就是跟随在python命令之后的