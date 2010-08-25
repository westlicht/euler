#!/usr/bin/python

a = 1
b = 1

sum = 0

def ispalindrome(num):
	s = "%d" % (num)
	for i in range(0,len(s)/2,1):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

def findbiggest(max):
	biggest = 0
	for a in range(max-1,1,-1):
		for b in range(max,a,-1):
			c = a * b
			if ispalindrome(c):
				if c > biggest:
					biggest = c
				print "%d x %d = %d" % (a, b, c)
	return biggest

print findbiggest(999)
