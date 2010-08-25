#!/usr/bin/python

def check(num):
	str = "%d" % (num)
	sum = 0
	for i in range(len(str)):
		sum += pow(int(str[i]), 5)
	if sum == num:
		print str
		return num
	return 0

def find():
	sum = 0
	for i in range(2,1000000,1):
		sum += check(i)
	return sum

print find()
