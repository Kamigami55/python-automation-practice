import re

madLibsFile = open('0804-madLibsFile', 'r')
content = madLibsFile.read()
madLibsFile.close()

madLibsRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

result = madLibsRegex.search(content)
while result != None:
    result = result.group()
    if result == 'ADJECTIVE' or result == 'ADVERB':
        print("Enter an %s:" % (result.lower()))
    else:
        print("Enter a %s:" % (result.lower()))
    replacement = input()
    content = madLibsRegex.sub(replacement, content, 1)
    result = madLibsRegex.search(content)

print(content)
madLibsFile = open('madLibsFile', 'w')
madLibsFile.write(content)
madLibsFile.close()
