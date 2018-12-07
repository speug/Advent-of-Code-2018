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
	sums = np.sum(guardSleepMatrix,axis=1)
	worstGuard = np.argmax(sums)
	worstMinute = np.argmax(guardSleepMatrix[worstGuard,:])
	print('The worst guard is {0}. They was most asleep at 00:{1}. The checksum is thus {2}'.format(str(worstGuard),str(worstMinute),str(worstGuard*worstMinute))) 
		
