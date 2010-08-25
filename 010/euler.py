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

def primesum(max):
	prime = 2
	sum = 0
	while (True):
		sum += prime
		prime = nextprime(prime)
		if (prime >= max):
			break
	return sum
	
print primesum(1000000)		
