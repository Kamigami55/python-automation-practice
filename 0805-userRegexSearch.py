import os, re

print("Please enter a regular expression: ", end='')
userRegex = re.compile(input())

for filename in os.listdir('./0805-files'):
    if filename.endswith('.txt'):
        file = open('./0805-files/'+filename, 'r')
        for line in file.readlines():
            if userRegex.search(line) != None:
                print(line, end='')
        file.close()
