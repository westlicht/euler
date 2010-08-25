#!/usr/bin/python

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninetine"]

decades = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def humandecimal(value):
	name = ""

	# thousands
	if value >= 1000:
		name += numbers[value / 1000 - 1] + " thousand "
	value %= 1000
	if value == 0:
		return name

	if len(name) > 0:
		name += "and "

	# hundreds
	if value >= 100:
		name += numbers[value / 100 - 1] + " hundred "
	value %= 100
	if value == 0:
		return name

	if len(name) > 0:
		name += "and "

	# tens
	if value >= 20:
		name += decades[value / 10 - 2]
		value %= 10
		if value == 0:
			return name
		name += numbers[value - 1]
		return name
	else:
		name += numbers[value - 1]
		return name

sum = 0
for i in range(1,1001,1):
	name = humandecimal(i)
	sum += len(name.replace(" ", "").strip())
	print name

print sum
