#1

for i in range(-3, -1):
    print(i, end = ' ')


#2

catty = 'cat in the hat'
vowel_count = 0
vowels = 'aeiou'
idx = 0
while vowel_count < 3:
    if catty[idx] in vowels:
        vowel_count += 1
    idx += 1
print(idx)

#3

s = '123'
print(s[:] + s[:1] + s[2:])


#4

faces = 'ooh-la-la'
aList = ['oo', '-', 'la']
inCount = 0
for i in range(len(faces)-1):
    if faces[i] + faces[i+1] in aList:
        inCount += 1
print(inCount)


#5

double_hero = ""
supe = 'superman'
bat = 'batman'
for letter in bat:
    if letter not in supe:
        break
    else:
        double_hero.append(letter)
        continue
print(double_hero)


###6
##candidates = {'dems':2, 'reps':3, 'out':15}
##print(candidates[2])


#7

def dictTest(d, aVal):
    for k in d:
        if d[k] == aVal:
            return k
    return None
lengths = {'one':3, 0:1, 'two':3}
print(dictTest(lengths, 3))


#8

bool_exprs = [True or False, True, True and False, not False]
accumulator = 0
for expr in bool_exprs:
    if expr == True:
        accumulator += 1
        accumulator *= 2
        continue
    break
print(accumulator)


#9

q = 'What is the Matrix?'
def splitLength(t):
    rtn = 0
    aList = t.split()
    for s in aList:
        rtn += len(s)
    return rtn
print(splitLength(q))

#10

def occurrences(fileName, searchStr):
    rtnVal = 0
    inF = open(fileName)
    for line in inF:
        lineLower = line.lower()
        rtnVal += lineLower.count(searchStr)
    inF.close()
    return rtnVal
seuss = open('you.txt', 'w')
seuss.write('Today you are You, that is truer than true.' + '\n')
seuss.write('There is no one alive who is Youer than You.' + '\n')
seuss.close()
print(occurrences('you.txt', 'you'))
seuss.close()

#11

def capitalL(t, width):
    
    t.down()
    t.fd(width)
    t.backward(width)
    t.lt(90)
    t.fd(width*2)
    t.backward(width*2)
    t.rt(90)




def Ls(t, initWidth, multiplier, reps, angle):
    for i in range(reps):
        capitalL(t, initWidth)
       
        initWidth*=multiplier
        t.rt(angle)
##
##import turtle
##s = turtle.Screen()
##aPen = turtle.Turtle()
##aPen.left(60)
##Ls(aPen, 20, 1.5, 3, 20)



#12

def initialDict(text):
    d={}
    for word in text.split():
        if word[0].lower() not in d:
            d[word[0].lower()]=[word]
        else:
            d[word[0].lower()]+=[word]
    return d
print(initialDict('The Call of the Wild'))


#13

def lineStats(inFile, outFile):
    inF=open(inFile)
    outF= open(outFile, 'w')
    for line in inF:
        if len(line[:-1])==0:
            outF.write('0' + ' '+'0' + '\n')
        else:
            words = line[:-1].split()
            outF.write(str(len(words))+ ' '+ str(len(line[:-1])) + '\n')

    outF.close()
    inF.close()

f = open('promisedLand.txt', 'w')
f.write('The dogs on main street howl,' + '\n')
f.write('cause they understand,' + '\n')
f.write('\n')
f.write('I believe in a promised land...' + '\n')

f.close()

inF = 'promisedLand.txt'
outF = 'promisedLandStats.txt'
lineStats(inF, outF)            
