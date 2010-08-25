#!/usr/bin/python

a = 1
b = 1

sum = 0

while (b <= 1000000):
	if b % 2 == 0:
		sum += b
	a, b = b, a + b

print sum
