from collections import defaultdict

def countOccs(xs):
	counts = defaultdict(int)
	for x in xs:
		counts[x] += 1
	return counts

with open('input.txt') as fp:
	lines = fp.readlines()
	twos = 0
	threes = 0
	for l in lines:
		c = countOccs(l)
		twos += (2 in c.values())
		threes += (3 in c.values())
	print('Checksum: ' + str(twos * threes))
			
