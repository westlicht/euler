#!/usr/bin/python

def loadfile(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	
	for line in lines:
		line = line.strip()
		values = line.split(",")
		data = []
		for value in values:
			data.append(int(value))
		return data

def decipher(data, pw):
	result = ""
	i = 0
	for value in data:
		result += chr(value ^ ord(pw[i]))
		i = (i + 1) % len(pw)
	return result

def sum(text):
	sum = 0
	for i in text:
		sum += ord(i)
	return sum

def check(data, pw):
	text = decipher(data, pw)
	if text.find("with") >= 0:
		print text
		print pw
		print sum(text)
		return

def find(data):
	a = ord("a")
	for i in range(26):
		for j in range(26):
			for k in range(26):
				pw = chr(a + i) + chr(a + j) + chr(a + k)
				check(data, pw)

data = loadfile("input.txt")
find(data)
