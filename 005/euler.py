#!/usr/bin/python


def divisible(num, max):
	for i in range(1,max,1):
		if num % i != 0:
			return False
	return True
			

def find(max):
	num = max
	while (True):
		if divisible(num, max):
			return num
		num += max

print find(20)
