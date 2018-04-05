#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
print "-- def func --"

# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

num = my_abs(5)
print "param 5 call my_abs is:",num
str_num = my_abs("5")
print "param '5' call my_abs is:",str_num

def age_check_func(age):
	if age > 18:
		return "you are adult"
	else:
		return "teenth"
age_desc = age_check_func(21)
print "age desc is:",age_desc

def my_abs_check(num):
	if not isinstance(num,(int,float)):
		raise TypeError('bad operand type')
	if num >= 0:
		return num
	else:
		return -num

# n_c = my_abs_check("aa")
# print "'aa' my_abs_check is:",n_c

n_c_c = my_abs_check(99)
print "99 my_abs_check is:",n_c_c

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

k = move(100,100,60,math.pi / 6)
x,y = move(100,100,60,math.pi / 6)
print "move k is:",k
print "move x is:",x
print "move y is:",y


# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。