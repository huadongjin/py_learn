#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归

def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
print "5的阶乘是多少：fact(5) :" ,fact(5)	

# 使用递归函数需要放置栈溢出，因为函数调用是通过栈这种数据结构
# 实现的，每当进入一个函数调用，栈就会加一层栈桢，每当
# 函数返回，栈就会减一层栈桢。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 比如调用 fact(1000)


# 解决办法：通过“尾递归”优化，“尾递归”是指，在函数返回的适合，调用自身本身，且return语句补鞥包含表达式。
# 这样 编辑器或解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈桢，不会出现栈溢出的情况。

# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。

# 改造需要把每一步的乘积传入到递归函数中：

def fact_new(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

# 上述函数中，return fact_iter(num -1,num * product)仅仅返回递归函数本身，num -1 和
# num * product 在函数调用前就会被计算，不影响函数调用。

#尾递归优化后，栈不会增长，但是因为python解释器没有做优化，所以，做了尾递归后，还是会导致栈溢出。