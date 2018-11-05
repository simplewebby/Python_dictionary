#1

for i in range(1):
    for j in range(1):
        print(i, j, end = "")


#2



m2Date = '2017-03-27'
freq = -1
position = 0
while freq != 1:
    x = m2Date[position]
    freq = m2Date.count(x)
    position = int(freq)
print(position)


#3

s = 'Newark'
print(s[:-3])

#4

def vehicleSound(vehicle, sound):
    for letter in vehicle:
        if letter not in sound:
            return False
    return True
print(vehicleSound('car', 'beep'))


#5
activities = ['eat', 'dream']
vowels = 'aeiou'
for vowel in vowels:
    for activity in activities:
        if vowel in activity:
            break
        print(activity + " ", end="")



#6
food_issues = [['lactose', 'gluten'], ['sugar', 'fat', 'salt'], 'fiber']
print(food_issues[1][1][1])

#7
def returnVal(d, x):
    if x in d:
        return 'key'
    elif x in d.values():
        return 'value'
    else:
        for v in d.values():
            if x in v:
                return v
web = {'secure':['https'], 'protocols':['ftp', 'tcp/ip'], 'markup':'html5'}
print(returnVal(web, 'm'))


#8

bools = [True and False, not False, False or True, not not False]
cum = 0
for bool in bools:
    if bool == False:
        cum += 1
    else:
        cum *= 3
print(cum)


#9

worth = "A thousand people in the street Singing songs and carrying signs"
def compare(t, pivot):
    rtn = []
    words = t.split()
    for word in words:
        if len(word) < pivot:
            continue
        if word[0].isupper():
            rtn.append(word)
    return rtn
print(compare(worth, 4))


#10
def inFileCount(fileName):
    inF = open(fileName)
    length = len(inF.read())
    inF.close()
    return length
outF = open('cat.txt', 'w')
outF.write('The sun did not shine.' + '\n')
outF.write('It was too wet to play.' + '\n')
outF.close()
print(inFileCount('cat.txt'))


#11

def tri(t, length):
    t.down()
    for i in range(2):
        t.fd(length)
        t.bk(length)
        t.lt(360/3)

def tris(t, initSize, ratio, rotation, num):
    for i in range(num):
        tri(t, initSize)
        t.lt(rotation)
        initSize*=ratio
##import turtle
##s = turtle.Screen()
##shelly = turtle.Turtle()
##tris(shelly, 100, 1.2, 30, 4)


#12

def initialLets(t):
    d={}
    for word in t.split():
        if word[0] not in d:
            d[word[0]]=1
        else:
            d[word[0]]+=1
    return d
text = "I'm born to trouble I'm born to fate"
print(initialLets(text))

#13

def initVowelCount(inFile, outFile):
    inF=open(inFile)
    outF =open(outFile, 'w')
    outContent=[]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    content = inF.readlines()
    for line in content:
        line=line.split()
        for word in line:
            if word[0] in vowels:
                outContent.append(word)
        if len(outContent)==0:
            outContent.append('\n')
    for line in outContent:
        outF.write(line+ '\n')

    outF.close()
    inF.close()

    
initVowelCount('pay_me.txt', 'pay_me_vowels.txt')   
           


