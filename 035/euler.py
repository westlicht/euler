#!/usr/bin/python

max = 1000000

def prime_table(n):
	t = []
	for i in range(0, n + 1):
		t.append(False)
	if n == 2:
		t[2] = True
		return
	elif n < 2:
		return
	t[2] = True
	s = range(3, n + 1, 2)
	mroot = n ** 0.5
	half = (n + 1) / 2 - 1
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3) / 2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	i = 3
	for x in s:
		if x:
			t[i] = True
		i += 2
	return t
		
	
def is_prime(v, t):
	return t[v]


def is_circular_prime(value, t):
	if not is_prime(value, t):
		return False
	s = str(value)
	l = len(s)
	for i in range(1, l):
		s = s[l - 1] + s[0:l - 1]
		v = int(s)
		if not is_prime(v, t):
			return False
	return True
		


t = prime_table(max)

count = 0

for i in range(0, max):
	if is_circular_prime(i, t):
		count += 1

print count
