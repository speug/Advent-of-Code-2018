from datetime import datetime as dt

def stamp2date(s):
	timestring = s[1:17]
	date,clock = timestring.split(' ')
	year,month,day = [int(x) for x in date.split('-')]
	hours,minutes = [int(x) for x in clock.split(':')]
	return dt(year, month, day, hours, minutes)

with open('raw_input.txt') as fp:
	lines = fp.readlines()
	sortedByTime = sorted(lines, key = stamp2date)
	with open('sorted_input.txt','w') as op:
		for l in sortedByTime:
			op.write('%s' % l)	
	print('Done')		
