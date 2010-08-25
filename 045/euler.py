#!/usr/bin/python

def triangle(n):
	return (n * (n + 1)) / 2

def pentagonal(n):
	return (n * (3 * n - 1)) / 2

def hexagonal(n):
	return (n * (2 * n - 1))

def find():
	t = 285
	p = 165
	h = 143

	v = vt = triangle(t)
	vp = pentagonal(p)
	vh = hexagonal(h)

	while (True):
		t += 1
		vt = triangle(t)

		while (vt < v):
			t += 1
			vt = triangle(t)
		v = vt
		while (vp < v):
			p += 1
			vp = pentagonal(p)
		v = vp
		while (vh < v):
			h += 1
			vh = hexagonal(h)
		v = vh
		if (vt == vp and vt == vh):
			return v
		
		
	


print find()
