tableData = [['apples','oranges','cherries','banana', 'hingymagic'],
             ['Alice','Bob','Carol','David', 'Thymagic'],
             ['dogs','cats','moose','goose', 'Thingymag']]


def printTable(nestedArray):
    tableDataDict = {}
    nestIndex = 0
    elementIndex = 0
    row = ''
    for nestIndex in range(len(nestedArray)):
        tableDataDict.setdefault(nestIndex, 0)
        for elementIndex in range(len(nestedArray[nestIndex])):
            if tableDataDict[nestIndex] < len(nestedArray[nestIndex][elementIndex]):
                tableDataDict[nestIndex]=len(nestedArray[nestIndex][elementIndex])
    for elementIndex in range(len(nestedArray[nestIndex])):
        row = ''
        for nestIndex in range(len(nestedArray)):
            row += nestedArray[nestIndex][elementIndex].rjust(tableDataDict[nestIndex])+' '
        print(str(row))

printTable(tableData)
