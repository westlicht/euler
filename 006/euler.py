#!/usr/bin/python

def sumsquares(max):
	num = 0
	for i in range(1,max+1,1):
		num += i * i
	return num

def squaresum(max):
	num = 0
	for i in range(1,max+1,1):
		num += i
	return num * num

max = 100
a = sumsquares(max)
b = squaresum(max)

print "%d - %d = %d" % (b, a, b -a)
