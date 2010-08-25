#!/usr/bin/python

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

def getprime(num):
	prime = 2
	while (num > 1):
		print num
		prime = nextprime(prime)
		num -= 1
	return prime

print getprime(10001)
