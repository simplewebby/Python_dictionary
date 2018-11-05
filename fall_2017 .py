#1

def characterAnalysis(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] *= -1
    return len(d)
print(characterAnalysis('bib'))


#2

def substring(a, b):
    indexA = 0
    rtnString = ""
    while True:
        if indexA > len(a):
            return False
        elif a[:indexA] == b:
            return b
        elif b in a[:indexA]:
            return a[:indexA]
        indexA += 1
    return rtnString
firstString = 'aha'
secondString = 'ha'
print(substring(firstString, secondString))


#3
def aSym(text):
    wordList = text.split()
    image = []
    for i in range(len(wordList)):
        if wordList[i] == wordList[-i-1]:
            image.append(i)
    return image
s = 'all for one and one for all'
print(aSym(s))


#4

word = 'boo'
prior = ""
for letter in word:
    if prior == letter:
        out = ""
        continue
    if letter == prior:
        out = letter
        break
    else:
        prior = letter
        out = word[0]
print([prior, out])


#5
mixedKeys = {1:{'three':3, 0:'zeroval'}, 0:'zero', 'two':2}
print(mixedKeys[1][0])


#6
bools = [True, 0>-1, not not True, 2%2 == 0, True and False]
index = 0
while bools[index]:
    index += 1
print(index)

#7
for i in range(2):
    for j in range(1):
        print(i, j, end = " ")

#8
fats = "You broke my heart when you said we'll part"
def makeDict(t):
    wordList = t.split()
    d = {}
    for word in wordList:
        initial = word[0]
        if initial not in d:
            d[initial] = [word]
        else:
            d[initial].append(word)
    return d
print(len(makeDict(fats)))


#9
def lengthCount(inFile, num):
    inF = open(inFile)
    different = 0
    content = inF.read()
    words = content.split()
    for word in words:
        if len(word) != num:
            different += 1
    inF.close()
    return different
print(lengthCount('edgar.txt', 3))


#10
fred = 'power concedes nothing without a demand'
freq = {}
for thing in fred.split():
    freq[thing] = fred.count(thing)
print(len(freq))


#11

def hemispheres(t, radius):
    t.down()
    t.circle(radius)
    t.lt(90)
    t.fd(radius*2)
    t.backward(radius*2)

def  multispheres(t, size, ratio, angle, num):
    for i in range(num):
        hemispheres(t, size)
        t.rt(360/angle)
        size*=ratio

##import turtle
##s = turtle.Screen()
##paint = turtle.Turtle()
##multispheres(paint, 100, 0.8, 80, 4)


def countVowels(text):
    d={}
    vowels='aeiou'
    for word in text.split():
        count=0
        if word not in d:
            d[word]=0
            for vowel in word:
                if vowel in vowels:
                    count+=1
                    d[word]=count
            
    return d

abe = "government of the people by the people for the people shall not perish"
print(countVowels(abe))





def longestOnLine(inFile, outFile):
    inF=open(inFile)
    outF=open(outFile, 'w')
    for line in inF:
        line=line.split()
        longest =-1
        for word in line:
            
            if len(word)> longest:
                longest=len(word)
            if len(word)==-1:
                longest= 0
        outF.write(str(longest)+ '\n')

    outF.close()
    inF.close()

longestOnLine('tom.txt', 'tomLongestOnLine.txt')
