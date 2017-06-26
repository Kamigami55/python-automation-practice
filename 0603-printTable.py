tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0]*len(data)
    for i in range(len(data)):
        for text in data[i]:
            if len(text) > colWidths[i]:
                colWidths[i] = len(text)
    for row in range(len(data[0])):
        for col in range(len(data)):
            print(data[col][row].rjust(colWidths[col]), end=' ')
        print()

printTable(tableData)

