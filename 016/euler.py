#!/usr/bin/python

num = pow(2, 1000)
str = "%d" % (num)
sum = 0
for i in range(len(str)):
	sum += int(str[i])
print sum
