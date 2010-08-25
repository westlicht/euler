#!/usr/bin/python

def cyclelen(text):
	l = len(text)
	l2 = int(l / 2)
	for i in range(1, l2 + 1, 1):
		if text[l - i:l] == text[l - 2 * i:l - i]:
			return i
	return 0

def cycle(nom, denom):
	cycle = ""
	while (True):
		nom *= 10
		d = nom / denom
		cycle += "%d" % (d)
		nom -= d * denom
		if (nom == 0):
			return 0
		if (d == 0):
			continue
		if len(cycle) < 5000:
			continue
		l = cyclelen(cycle)
		if l == 0:
			continue
		return l

def find():
	max = 0
	maxdenom = 0
	for i in range(1000):
		l = cycle(1, i + 1)
		if l > max:
			max = l
			maxdenom = i + 1
	return max, maxdenom

#print cycle(1,7)
print find()
