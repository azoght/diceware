import csv
import random

def tsvtoList(filename) -> []:
    t = open(filename)
    r = csv.reader(t, delimiter="\t")
    l = []
    for row in r:
        o = []
        for c in row:
            o.append(c)
        l.append(o)
    t.close()
    return l

dicewareWords = tsvtoList("officialDicewareWordList.tsv")

random.shuffle(dicewareWords)

def generatePassword(n: int,wordlist: []) -> str:
    p = ""
    for x in range(n):
        num = ""
        for i in range(5):
            s = str(random.randint(1,6))
            num += s
        w = ""
        for j in range(len(dicewareWords)):
            if dicewareWords[j][0] == num:
                w = wordlist[j][1]
                break
        if x > 0:
            p += " "
        p += w
    return p


def randomCapitalizer(password: str) -> str:
    password = [char for char in password]
    p = 0
    while p < len(password):
        if password[p] == " ":
            del password[p]
        p += 1
    numOfChars = random.randint(1, int(len(password) / 2))
    for n in range(numOfChars):
        place = random.randint(0,(len(password)-1))
        password[place] = password[place].upper()
    password = "".join(password)
    return password


def randomCharacterReplacer(password: str) -> str:
    chars = ["!","@","#","$","%","&","*","+","?","/","~","=","-","^","_","."]
    password = [char for char in password]
    p = 0
    while p < len(password):
        if password[p] == " ":
            del password[p]
        p += 1
    numOfChars = random.randint(1,int(len(password)/2.5))
    for n in range(numOfChars):
        char = random.randint(0,(len(chars)-1))
        place = random.randint(0,(len(password)-1))
        password[place] = chars[char]
    password = "".join(password)
    return password

def randomlyShortenToMaximum(password: str) -> str:
    charsToRemove = len(password) - 12
    removedChars = []
    while len(removedChars) <= charsToRemove:
        place = random.randint(0,(len(password)-1))
        if not place in removedChars:
            removedChars.append(place)

    removedChars = sorted(removedChars)[::-1]

    password = [char for char in password]
    p = len(password) -1
    while len(password) >= 12:
        if p in removedChars:
            del password[p]
            del removedChars[0]
            p +=1
        p -= 1

    password = "".join(password)
    return password

p = generatePassword(5,dicewareWords)

print(p)

p = randomCapitalizer(p)

print(p)

p = randomCharacterReplacer(p)

print(p)

p = randomlyShortenToMaximum(p)

print(p)
