import re

while True:
    print("Please enter a password: ", end='')
    password = input()
    overEightWordsRegex = re.compile(r'\w{8,}') # more than 8 words
    mustOneNumberRegex = re.compile(r'\w*\d\w*') # must contain 1 number
    mustOneUpperAlphaRegex = re.compile(r'\w*[A-Z]\w*') # must contain 1 uppercase alphabet
    mustOneLowerAlphaRegex = re.compile(r'\w*[a-z]\w*') # must contain 1 lowercase alphabet
    isStrong = True
    if overEightWordsRegex.search(password) == None:
        print("Strong password must contain more than 8 words")
        isStrong = False
    if mustOneNumberRegex.search(password) == None:
        print("Strong password must contain at lease 1 number")
        isStrong = False
    if mustOneUpperAlphaRegex.search(password) == None:
        print("Strong password must contain at lease 1 uppercase alphabet")
        isStrong = False
    if mustOneLowerAlphaRegex.search(password) == None:
        print("Strong password must contain at lease 1 lowercase alphabet")
        isStrong = False
    if isStrong:
        print("It is a STRONG password")
    else:
        print("Is is not strong password")
    print()

