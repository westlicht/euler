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

def computescore(name):
	score = 0
	for i in range(0, len(name), 1):
		score += ord(name[i]) - ord("A") + 1
	return score

def buildtriangle(num):
	list = []
	for i in range(1,num,1):
		list.append((i * (i + 1)) / 2)
	return list

table = loadtable("input.txt")
triangles = buildtriangle(21)

print triangles

count = 0
for item in table:	
	score = computescore(item)
	try:
		triangles.index(score)
	except:
		continue
	count += 1

print count
