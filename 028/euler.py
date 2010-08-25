#!/usr/bin/python

def find(maxsize):
	sum = 1
	a = 1
	b = 2
	size = 1

	while (size < maxsize):
		for i in range(4):
			a += b
			print a
			sum += a
		size += 2
		b += 2

	return sum
		
		

print find(1001)
