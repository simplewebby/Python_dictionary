#1
for i in range(1):
    for j in range(0):
        print(i, j, end = "")


#2

spell = 'accio'
freq = 0
pointer = 0
while freq != 2:
    letter = spell[pointer]
    freq = spell.count(letter)
    pointer += 1
print(pointer)


#3
s = 'slice and dice'
print(s[:5] + s[-5:])

#4

def animalSound(sound, animal):
    for letter in sound:
        if letter in animal:
            return True
    return False
print(animalSound('moo', 'cow'))


#5
substances = ['oobleck', 'flubber']
vowels = 'aeiou'
for substance in substances:
    for vowel in vowels:
        if vowel in substance:
            break
        print(substance[0], end="")
#6
scaries = [['bat', 'ghost', 'goblin'], ['boo', 'shriek', 'scream'], 'dark']
print(scaries[1][1])


#7
def inFileCount(fileName, length):
    inF = open(fileName)
    contents = inF.read().split()
    count = 0
    for word in contents:
        if len(word) == length:
            count += 1
    inF.close()
    return count
outF = open('dylan.txt', 'w')
outF.write('You would not think to look at him,' + '\n')
outF.write('but he was famous long ago' + '\n')
outF.write('For playing the electric violin on Desolation Row' + '\n')
outF.close()
print(inFileCount('dylan.txt', 3))


#8
def returnVal(x, d):
    if x in d:
        return 'key'
    elif x in d.values():
        return 'value'
    else:
        for v in d.values():
            if x in v:
                return v
foods = {'drink':['beer'], 'burger':['veggie', 'beef'], 'salad':'beet'}
print(returnVal('ee', foods))


#9

bools = [True or False, True, True and False, True and not False]
cum = 0
for bool in bools:
    if bool == True:
        cum += 1
    else:
        cum *= 2
        print(cum)
print(cum)

#10
bob = 'I heard the roar of a wave that could drown the whole world'
def compare(t, wordList):
    rtn = []
    words = t.split()
    for word in words:
        if word in wordList:
            continue
        if word[0] == 'w':
            rtn.append(word)
            break
        rtn.append(word)
    return rtn
print(compare(bob, ['a','of','the']))

#11
def letterX(t, length):
    t.down()
    t.lt(45)
    for i in range(4):
        t.fd(length)
        t.bk(length)
        t.lt(90)
    t.rt(45)

def exes(t, initSize, deltaSize, sep, xNum):
    for i in range(xNum):
        letterX(t, initSize)
        initSize*=deltaSize
        t.up()
        t.fd(sep)
        t.down()
        
import turtle
s = turtle.Screen()
shelly = turtle.Turtle()
exes(shelly, 100, 0.6, 30, 6)



#12

def wordLengths(text):
    d={}
    words=text.split()
    for word in words:
        if len(word) not in d:
            d[len(word)]=1
        else:
            d[len(word)]+=1
    return d

text = 'Go to Heaven for the climate Hell for the company'
print(wordLengths(text))

f = open('run.txt', 'w')
f.write("It's a death trap, it's a suicide rap" + '\n')
f.write("We gotta get out while we're young" + '\n')
f.write('\n')
f.write("Cause tramps like us, baby we were born to run" + '\n')
f.close()




#13
def initVowelCount(inFile, outFile):
    vowels=['a','e','i', 'o','u']
    outContent=[]
    inF =open(inFile)
    outF=open(outFile, 'w')
    content =inF.readlines()
    for line in content:
        line=line.split()
        count=0
        for word in line:
            if word[0].lower() in vowels:
                count+=1
        if count==0:
            outContent.append('\n')
        else:
            outContent.append(str(count) + '\n')

    for line in outContent:
        outF.write(line)
    outF.close()
    inF.close()

initVowelCount('run.txt', 'runMostFreq.txt')
        

