#!/usr/bin/python

import datetime

begin = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
delta = datetime.timedelta(days=1)

sum = 0

date = begin
while (date <= end):
	date += delta
	if date.timetuple()[2] == 1 and date.timetuple()[6] == 6:
		sum += 1

print sum
