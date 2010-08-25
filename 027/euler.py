#!/usr/bin/python

import math

def isprime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	for i in range(3, math.sqrt(num) + 1, 2):
		if num % i == 0:
			return False
	return True

def numprimes(a, b):
	n = 1
	while (True):
		v = n * n + a * n + b
		if not isprime(v):
			return n - 1
		n += 1

def find():
	max = 0
	solution = 0
	for a in range(-1000,1001,1):
		print a
		for b in range(-1000,1001,1):
			num = numprimes(a, b)
			if num > max:
				max = num
				solution = a * b
	return max, solution

print find()
