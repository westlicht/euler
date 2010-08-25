#!/usr/bin/python

import math

def subcheck(n, d, sn, sd):
	if sn == sd:
		return
	if sd == 0:
		return
	v1 = float(n) / float(d)
	v2 = float(sn) / float(sd)
	if v1 != v2:
		return
	print "%d/%d = %d/%d %f %f" % (n, d, sn ,sd, v1, v2)

def check(n, d):
	if n % 10 == 0 or d % 10 == 0:
		return
	n1 = n / 10
	n2 = n % 10
	d1 = d / 10
	d2 = d % 10
	if n1 == d1:
		subcheck(n, d, n2, d2)
	if n1 == d2:
		subcheck(n, d, n2, d1)
	if n2 == d1:
		subcheck(n, d, n1, d2)
	if n2 == d2:
		subcheck(n, d, n1, d1)

def find():
	for n in range(10,100,1):
		for d in range(n+1,100,1):
			check(n, d)

#print check(49,98)
find()

