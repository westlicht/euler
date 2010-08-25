#!/bin/python

count = 0
sum = 0

for i in range(1,1000,1):
	if (i % 3 != 0) and (i % 5 != 0):
		continue
	count += 1
	sum += i

print "count: %d sum: %d" % (count, sum)
