with open('input.txt') as fp:
    lines = fp.readlines()
    s = len(lines)
    lenOfWord = len(lines[0]) - 1
    common = ''
    for i in range(0, s):
        curr = lines[i]
        for j in range(i+1,s):
            currComp = lines[j]
#            print('Comparing {0} and {1}'.format(curr, currComp))
            stopFlag = False
            for k in range(0, lenOfWord):
                if curr[k] == currComp[k]:
                    common += curr[k]
                else:
                    if stopFlag:
                        common = ''
                        break
                    else:
                        stopFlag = True
            if common != '':
                break
        if common != '':
            break
    print('Common letters: ' + common)
