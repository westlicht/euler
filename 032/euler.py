#!/usr/bin/python

def find():
	a = 2
	while (a < 9999999):
		min = 100000000 / a
		max = 999999999 / a + 1
#		print min, max
#		for b in range(min,max+1,1):
#			c = a * b
#			if c < 100000000 or c > 999999999:
#				continue
#			print c
		a += 1

print find()
