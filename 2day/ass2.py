with open('input.txt') as fp:
    lines = fp.readlines()
    s = len(lines)
    lenOfWord = len(lines[0]) - 2
    common = ''
    for i in range(0, s):
        curr = lines(i)
            for j in range(i+1,s):
                currComp = lines(j)
                stopFlag = False
                for k in range(0, lenOfWord):
                    if curr[k] == currComp[k]:
                        common += curr[k]
                    else:
                        if !stopFlag:
                            break
                break
    print('Common letters: ' + common)
