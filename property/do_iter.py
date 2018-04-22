#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findMinAndMax(L):
	if L == []:
		return (None,None)
	else:
		max = L[0]
        min = L[0]
        for num in L:
          if num > max:
             max = num
          elif num < min:
             min = num
        return (min, max)


# test
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')