#!/usr/bin/python

num = 13195
num = 317584931803

i = 1

def nextprime(n):
	found = False
	while (not found):
		n += 1
		found = True
		for i in range(2, n - 1, 1):
			if n % i == 0:
				found = False
				break
	return n

while (True):
	i = 2
	while (num % i != 0):
		i = nextprime(i)
	print i, num
	num = num / i
		
