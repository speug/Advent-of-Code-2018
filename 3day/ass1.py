import numpy as np

def claim2mat(s):
	splitted = s.split(' ')
	cornerX,cornerY = (splitted[2][:-1].split(','))	
	cornerX,cornerY = int(cornerX),int(cornerY)	
	adjX,adjY = (splitted[3][:-1].split('x'))
	adjX,adjY = int(adjX)+cornerX,int(adjY)+cornerY
	#print('{0}:{1},{2}:{3}'.format(cornerX,adjX,cornerY,adjY))
	out = np.zeros((1000,1000))
	out[cornerX:adjX,cornerY:adjY] = 1
	return out

with open('input.txt') as fp:
	lines = fp.readlines()
	fabric = np.zeros((1000,1000))
	for l in lines:
		lMat = claim2mat(l)
		fabric = np.add(fabric,lMat)
	fabric = fabric >1
	print('Square inches with multiple claims: ' + str(np.count_nonzero(fabric)))
