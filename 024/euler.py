#!/usr/bin/python

import sys

counter = 0

def swap(set, i, j):
	t = set[i]
	set[i] = set[j]
	set[j] = t


def rotate_left(set, start, num):
	t = set[start]
	for i in range(start, num - 1):
		set[i] = set[i + 1]
	set[num - 1] = t


def permute(set, start, num):
	global counter
	counter += 1
	if counter == 1000000:
		print set
		sys.exit
	if start < num:
		for i in range(num - 2, start - 1, -1):
			for j in range(i + 1, num):
				swap(set, i, j)
				permute(set, i + 1, num)
			rotate_left(set, i, num)



set = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

permute(set, 0, 10)


