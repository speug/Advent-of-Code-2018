with open('input.txt') as fp:
	lines = fp.readlines()
	res = 0
	for l in lines:
		toAdd = float(l[1:-1])
		sign = l[0]
		if sign == '+':
			res = res + toAdd
		else:
			res = res - toAdd
	print('The final result is ' + str(res))	
