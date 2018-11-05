#1
def initialLetterCount(wordList):
    d={}
    for word in wordList:
        if word[0] not in d:
            d[word[0]]=1
        else:
            d[word[0]]+=1

    return d


horton = ['I','say','what','I','mean','and','I','mean','what','I','say']
print(initialLetterCount(horton))


#2

def initialLetters(wordList):
    d={}
    for word in wordList:
        for letter in word:
            if letter==word[0]:
                d[letter]=[word]

    return d
print(initialLetters(horton))



print(shareALetter(horton))
