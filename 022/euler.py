#!/usr/bin/python

def loadtable(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	
	for line in lines:
		line = line.replace("\"", "").strip()
		values = line.split(",")
		values.sort()
		return values

def computescore(index, name):
	print name
	score = 0

	for i in range(0, len(name), 1):
		score += ord(name[i]) - ord("A") + 1

	return score * index


table = loadtable("input.txt")
score = 0
index = 1
for item in table:	
	score += computescore(index, item)
	index += 1

print score	
