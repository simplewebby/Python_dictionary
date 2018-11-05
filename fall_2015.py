
#1
var = 0
num = 1
for i in range(3):
    if i%2 == 0:
        num *= -1
    var += num
    print(var, end = ' ')

#2

scary = 'boo! boo!'
place = 0
while place <= len(scary):
    current = scary[place]
    print(current, end='')
    place += scary.count(current)


#3

eap = 'rapping, rapping'
print(eap[:4] + eap[-4:])


#4
seasonal = 'boo'
out = ''
idx = 0
while True:
    letter = seasonal[idx]
    letterCount = seasonal.count(letter)
    out += letter
    if seasonal[idx] > seasonal[idx+1]:
        idx += letterCount
    elif seasonal[idx] < seasonal[idx+1]:
        idx -= letterCount
    else:
        break
print(out)


#5

favs = ['Leia', 'R2-D2', 'Solo', 'Chewbacca']
vowels = 'aeiou'
for vowel in vowels:
    for fav in favs:
        if vowel in fav:
            continue
        else:
            print(fav[0], end='')
            break


#6

pairs = {'':'empty', 2:'prime', 1:['polio', 'smallpox']}
print(pairs[1][1])


###7
##def dictTest(aType, aDict):
##    if aType in aDict:
##        return aType
##    else:
##        for v in aDict.values():
##            if aType in v:
##                return v
##types = {string:'string', num:0, tuple:('a','ok')}
##print(dictTest('string', types))

#8

boolExprs = [True and False, not True, True or False, True and not False]
tCount = 0
for expr in boolExprs:
    if expr == True:
        tCount = 2*tCount + 1
    else:
        break
print(tCount)

#9

def contains(txt, letters):
    rtn = []
    aList = txt.split()
    for w in aList:
        if w in letters:
            rtn.append(w)
    return rtn
burns = "a man's a man for a' that"
print(contains(burns, 'abc'))

#10
def fileCount(fileName, s):
    inF = open(fileName)
    count = 0
    content = inF.read()
    for thing in content:
        if s in thing:
            count += 1
    inF.close()
    return count
    print(count)
w = open('seuss.txt', 'w')
w.write('You are on your own' + '\n')
w.write('and you know what you know' + '\n')
w.close()

print(fileCount('seuss.txt', 'you'))


