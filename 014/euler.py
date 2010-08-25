#!/usr/bin/python

def count(start):
	value = start
	count = 1
	while (value != 1):
		if value % 2 == 0:
			value = value / 2
		else:
			value = 3 * value + 1
		count += 1
	return count

def find():
	max = 0
	start = 0
	for i in range(1,1000000,1):
		cur = count(i)
		if cur > max:
			max = cur
			start = i
		if i % 1000 == 0:
			print i
	return max, start

print find()
