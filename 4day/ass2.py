import numpy as np
np.set_printoptions(threshold=np.inf)
with open('sorted_input.txt') as fp:
	lines = fp.readlines()
	guardSleepMatrix = np.zeros((10000,60))
	currentID = 0
	fellAsleepTime = 0
	for l in lines:
		if 'begins shift' in l:
			currentID = int((l.split('#')[1]).split(' ')[0])
			fellAsleepTime = 0
		elif 'falls asleep' in l:
			fellAsleepTime = int(l.split(']')[0][-2:])
		elif 'wakes up' in l:
			wokeUpTime = int(l.split(']')[0][-2:])
			for i in range(fellAsleepTime,wokeUpTime):
				guardSleepMatrix[currentID][i] += 1
		else:
			raise ValueError('Log \"' + l + '\" does not match any conditions')
	worstIdx = np.unravel_index(np.argmax(guardSleepMatrix, axis=None), guardSleepMatrix.shape)
	print('The worst minute is 00:{0}. The guard associated is {1}. The checksum is thus {2}'.format(str(worstIdx[1]),str(worstIdx[0]),str(worstIdx[0]*worstIdx[1]))) 
		
