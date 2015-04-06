# -*- coding: utf-8 -*-
class A:
	def hello(self, name):
		return 'hello!' + name

a = A()
b = A()
# Объявление атрибута
a.arg = 'John'
b.arg = 2

print (a.arg)
print a.hello(a.arg)