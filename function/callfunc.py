#!/usr/bin/env python
# -*- coding: utf-8 -*-

print u'python 内置的函数中，不同函数调用受参数数量和类型校验。这点和java一样。'
print u'函数在线查询：https://docs.python.org/2/library/functions.html'

print "----不同类型在函数使用的时候，常用到类型转换----"

str_to_int = int('123')
print "str_to_int = int('123') is:",str_to_int

str_to_float = float('12.2')
print "str_to_float = float('12.2') is:",str_to_float

float_to_int = int(12.23)
print "float_to_int = int(12.23) is:",float_to_int

float_to_str = str(23.33)
print "float_to_str = str(23.33) is:",float_to_str

int_to_str = str(1111)
print "int_to_str = str(1111) is:",int_to_str

to_unicode = unicode(100)
print "to_unicode = unicode(100) is:",to_unicode

int_to_boolean = bool(1)
print "int_to_boolean = bool(1) is:",int_to_boolean

str_to_boolean = bool('dd')
print "str_to_boolean = bool('dd') is:",str_to_boolean

