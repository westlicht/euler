#!/usr/bin/python

import pickle

MAX_SUM = 28123
COMPUTE_ABUNDANT = False

# Check if a number is abundant
def is_abundant(value):
	sum = 1
	for i in range(2, value / 2 + 1):
		if value % i == 0:
			sum += i
	return sum > value

# Find all abundant numbers
def find_abundant(min, max):
	abundant = []
	for i in range(min, max + 1):
		if is_abundant(i):
			abundant.append(i)
	return abundant


def is_abundant_sum(value, abundant, abundant_hash):
	for a in abundant:
		if a >= value:
			break
		try:
			abundant_hash[value - a]
			return True
		except:
			pass
	return False



# Create abundant numbers
if COMPUTE_ABUNDANT:
	abundant = find_abundant(1, MAX_SUM + 1)
	pickle.dump(abundant, open("abundant.dat", "w"))

# Load abundant numbers
abundant = pickle.load(open("abundant.dat", "r"))

# Build a hash map of all abundant numbers
abundant_hash = {}
for a in abundant:
	abundant_hash[a] = True

# Find all integers which are not a sum of abundant numbers
sum = 0
for i in range(1, MAX_SUM + 1):
	if not is_abundant_sum(i, abundant, abundant_hash):
		sum += i

print sum

