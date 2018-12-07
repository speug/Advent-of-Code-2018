def react(l,currentIdx,nextIdx,s):
	currChar = l[currentIdx]
	if currChar != '' and nextIdx < s:
		nextChar = l[nextIdx]
		while nextIdx < s and nextChar == '':
			nextIdx += 1
			nextChar = l[nextIdx]
		if currChar.swapcase() == str(nextChar):
			l[currentIdx] = ''
			l[nextIdx] = ''
			nextCurrIdx = currentIdx - 1 if currentIdx > 0 else 0 
			while nextCurrIdx > 0 and l[nextCurrIdx] == '':
				nextCurrIdx -= 1
			react(l,nextCurrIdx,nextIdx+1,s)

with open('input.txt') as fp:
	polymerList = list('dabAcCaCBAcCcaDA')
	s = len(polymerList)
	for i in range(0,s):
		react(polymerList,i,i+1,s)
	reactedList = list(filter(lambda a: a != '',polymerList))
	print(len(reactedList))	
	print(''.join(reactedList))
