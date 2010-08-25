#!/usr/bin/python

str = " "
n = 1
while len(str) <= 1000000:
	str += "%d" % (n)
	n += 1

print int(str[1]) * int(str[10]) * int(str[100]) * int(str[1000]) * int(str[10000]) * int(str[100000]) * int(str[1000000])
