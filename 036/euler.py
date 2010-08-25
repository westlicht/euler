#!/usr/bin/python

a = 1
b = 1

sum = 0

def ispalindrome(s):
	for i in range(0,len(s)/2,1):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

def tobinary(num):
	str = ""
	while (num > 0):
		if num % 2 == 0:
			str = "0" + str
		else:
			str = "1" + str
		num /= 2
	return str

def check(num):
	s = "%d" % (num)
	if not ispalindrome(s):
		return 0
	s = tobinary(num)
	if not ispalindrome(s):
		return 0
	print num
	return num
	
	

def find():
	sum = 0
	for i in range(1,1000000,1):
		sum += check(i)
	return sum

print find()
