with open('input.txt') as fp:
	lines = fp.readlines()
	res = 0
	s = set()
	stop = False
	linesSize = len(lines)
	i = 0
	while not stop:
		l = lines[i]
		toAdd = float(l[1:-1])
		sign = l[0]
		if sign == '+':
			res = res + toAdd
		else:
			res = res - toAdd
		if res in s:
			stop = True
		else:
			s.add(res)
		i = (i + 1) % linesSize
	print('The first result to repeat is ' + str(res))	
