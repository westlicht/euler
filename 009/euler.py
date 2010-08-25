#!/usr/bin/python

def checktriplet(a, b, c, tot):
	if a + b + c != tot:
		return False
	if a * a + b * b != c * c:
		return False
	return True

def find(max):
	for b in range(2,max,1):
		for a in range(1,b-1,1):
			c = max - a - b
			if checktriplet(a, b, c, max):
				print "%d, %d, %d, %d" % (a, b, c, a * b * c)
				return
	
find(1000)
	
