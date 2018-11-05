#1
nurseryRhyme = 'Rain rain go away'
vowelCount = 0
n = -1
while vowelCount < 3:
    if nurseryRhyme[n] in 'aeiouAEIOU':
        vowelCount += 1
    n -= 1
print(n)



#2

def splitLength(sentence):
    result = 0
    for s in sentence.split():
        
        if len(s) > 3:
            result += 1
    return result
lisa = 'Dad, are you listening to me?'
print(splitLength(lisa))


#3

boolList = [False, False or False, False and False, not False, not not False]
sum = 0
for b in boolList:
    if not b:
        sum += 1
print(sum)


#4
s = 'abc'
print(s[0:] + s[-2:2] + s[:1])


#5

def mirrorOnWheels(s):
    prev = 0
    for current in range(1, len(s) - 1):
        prev = current - 1
        next = current + 1
        if s[prev] == s[next]:
            break
        else:
            continue
        return 0
    return prev
s = 'Good decision!'
print(mirrorOnWheels(s))



#6
mixture = {1:[1, 2, 0], 2:[2, 0, 1], 0:[0, 1, 2]}
print(mixture[2][2])


#7

noOddHeroes = []
heroes = ['superman', 'batman', 'aquaman']
for hero in heroes:
    if len(hero) % 2 == 0:
        noOddHeroes.append(hero)
print(noOddHeroes)


#8

candyOnStick = 'lolli lolli lolli lollipop lollipop'
wordList = candyOnStick.split('i')
d = {}
for word in wordList:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(len(d))

#9


def oldMcDonald(farm):
    result = 0
    for animal in farm:
        if animal[0] in farm[animal]:
            result += 1
    return result
farm = {'cow':'moo', 'duck':'quack', 'cricket':'chirp'}
print(oldMcDonald(farm))


#10


def analyzer(fileName):
    inputFile = open(fileName)
    line = inputFile.readline()
    inputFile.close()
    return line.count(',')
quotes = open('alice.txt', 'w')
quotes.write('Now, here, you see, it takes all the running\n')
quotes.write('you can do, to keep in the same place.\n')
quotes.close()
print(analyzer('alice.txt'))


#11

def triangle(t, side):
    t.down()
    for i in range(3):
        t.fd(side)
        t.lt(360/3)
def umbrella(t, side, rotation, count):
    for i in range(count):
        triangle(t, side)
        t.lt(rotation)
##import turtle
##snappy = turtle.Turtle()
##umbrella(snappy, 100, 60, 6)


#12

def analyzeAreaCodes(phones):
    d={}
    for phone in phones:
        if phone[:3] not in d:
            d[phone[:3]]=1
        else:
            d[phone[:3]]+=1
    return d

phones = ['982-867-5309', '800-649-2568', '979-606-0842', '982-779-311']
print(analyzeAreaCodes(phones))



#13

def lineStats(inFile, outFile):
    inF=open(inFile)
    outF=open(outFile, 'w')
    vowels='aeiouAEIOU'
    const=' bcdfghjklmnpqsrtvxzwyBCDFGHJKLMNPQRSTVXZWY'
    for line in inF:
        c=v=0
        for char in line:
            if char in vowels:
                v+=1
            elif char in const:
                c+=1
        outF.write(str(c) + '   '+ str(v) + '\n')
    outF.close()
    inF.close()

lineStats('mary.txt', 'maryStats.txt')



    
