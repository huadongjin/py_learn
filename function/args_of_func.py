#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python中函数的参数使用灵活多变

# 默认参数

def power(x):
	return x * x

# 计算N次方，默认计算平方,n=2表示当第二个参数没有传值的时候使用默认值2，也就是计算平方。
def power_default(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

si = power_default(3)
six = power_default(3,5)
print u"3的平方是多少？",si
print u"3的5次方是多少？",six

# 这里是顺序关系，必选参数必须靠前，默认参数靠后

# 再如：多个必选和多个默认参数,可节省在函数调用时候的输入，比java灵活；

def enroll(name, gender, age=6,city = 'Beijing'):
	print  'your name is:',name
	print  'your gender is:',gender
	print  'your age is:',age
	print  'your city is:',city

enroll('xiaoming','F3-2')
enroll('xiaofang','F3-2',city = 'hanghzou')
enroll('xiaoxiao','F3-2',age = 5,city = 'hanghzou')

# 坑：默认参数必须指向不可变对象

# 这个函数多次调用默认函数会有问题：
def add_end(L=[]):
	L.append('End')
	return L

print add_end()
print add_end()
# 结果会违背函数本意，再次运行时会多次追加‘End’字符串
# 修改如下：将参数指向不可变对象None解决。

def add_end_update(L=None):
	if L is None:
		L = []
	L.append('End')
	return L
print add_end_update()
print add_end_update()

# 可变参数 *numbers  定义求平方和函数
def calc(*numbers):
	sum = 0
	for num in numbers:
		sum = sum + num * num
	return sum

count = calc(1,2,3,4,5)
print "从1到5的平方和是多少 ？ ",count

# 也可以通过list 或者 tuple 作为可变参数进行传参
# 繁琐的写法
nums_old = [1,2,3]
count_1 = calc(nums_old[0],nums_old[1],nums_old[2])

# 通过list或者tuple简易传参
nums = [1,2,3,4,5,6]
count_2 = calc(*nums)
print "从1到6的平方和是多少 ？ ",count_2


# 关键词参数:
# 关键词参数允许你传入0个或者N个含参数名的参数，在函数内部会自动组装成dict.
def person(name,age,**kw):
	print 'name:',name, 'age:',age,'other:',kw
# 其中 name 和 age 为必选参数， **kw 为关键词参数。

peter = person('peter',30,address = 'hangzhou-yuhan',phone =15912345678)
other_agvs = {'city':'hangzhou','job':'Engineer'}
peter_wang = person('peter_wang',30,**other_agvs)

# 关键词参数特别有用，在确保必选参数后，对于其他未知参数我们就可以定义为关键词参数，用来接收更多的参数；

# 参数组合
# 函数中，以上的必选参数、默认参数、可变参数和关键词参数可随意组合使用，但有顺序关系，必须是：必选 -> 默认 - > 可变 -> 关键词参数
def house(address,house_name,size = 150,*person_name,**other):
	print 'address:',address, 'house name:',house_name,'size is:',size,' person name is:',person_name, ' other is:',other

per_list = ['dabao','xiaobao','baba','mama']

house('hangzhou','siji',200,*per_list,**other_agvs)







