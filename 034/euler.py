#!/usr/bin/python

def fac(n):
	sum = 1
	while (n > 1):
		sum *= n
		n -= 1
	return sum

def check(num):
	sum = 0
	str = "%d" % (num)
	for i in range(len(str)):
		sum += fac(int(str[i]))
	if sum == num:
		print num
		return num
	return 0

def find():
	sum = 0
	for i in range(11,1000000,1):
		sum += check(i)
	return sum

print find()
