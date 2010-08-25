#!/usr/bin/python

def fac(x):
	val = 1
	for i in range(1,x+1,1):
		val *= i
	return val

def sum(num):
	sum = 0
	num = "%d" % (num)
	for i in range(0,len(num),1):
		sum += int(num[i])
	return sum
	

num = fac(100)
print sum(num)
		
