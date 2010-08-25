#!/usr/bin/python

def find():
	h = {}

	for a in range(2,101,1):
		for b in range(2,101,1):
			n = pow(a, b)
			h[n] = True

	return len(h)

print find()
