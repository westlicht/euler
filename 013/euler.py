#!/usr/bin/python

def bigsum(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	sum = []
	first = True
	for line in lines:
		line = line.strip()
		for i in range(0,len(line),1):
			if first:
				sum.append(int(line[i]))
			else:
				sum[i] += int(line[i])
		first = False

	i = len(sum) - 1
	rem = 0
	while (True):
		if i >= 0:
			rem += sum[i]
			i -= 1
		print rem % 10
		rem /= 10
		if rem == 0:
			break
		

bigsum("input.txt")
	 
