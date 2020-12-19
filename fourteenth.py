import csv


def getCsv(txtFileName='fourteenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def getSumOfMemory(commandList):
    mask = ''
    memory = {}
    for row in commandList:
        if row[0] == 'mask':
            mask = row[2]
            continue
        memoryIndex = row[0][4:-1]
        desiredValue = int(row[2])
        desiredValueOnesSet = desiredValue | int(mask.replace("X", "0"), 2)
        desiredValueZerosSet = desiredValueOnesSet & int(mask.replace("X", "1"), 2)
        memory[memoryIndex] = desiredValueZerosSet
    return sum(memory.values())


def getIndizesWithX(memoryIndexMask):
    indizes = []
    for index, value in enumerate(memoryIndexMask):
        if value == 'X':
            indizes.append(index)
    return indizes


def getMemoryIndexList(memoryIndexOnesSet, mask):
    memoryIndexMask = getMemoryIndexMask(mask, memoryIndexOnesSet)
    indizesWithX = getIndizesWithX(memoryIndexMask)
    numberIndizesWithX = len(indizesWithX)
    numberOfMemoryAdresses = 2 ** numberIndizesWithX
    memoryIndexList = []
    for counter in range(numberOfMemoryAdresses):
        binaryString = decimalToBinary(counter).zfill(numberIndizesWithX)
        memoryIndex = list(memoryIndexMask)
        for index in range(numberIndizesWithX):
            memoryIndex[indizesWithX[index]] = binaryString[index]

        memoryIndexList.append(int(''.join(memoryIndex), 2))
    return memoryIndexList


def getMemoryIndexMask(mask, memoryIndexOnesSet):
    memoryIndexMask = ''
    for index, value in enumerate(mask):
        if value == 'X':
            memoryIndexMask = memoryIndexMask + 'X'
        else:
            memoryIndexMask = memoryIndexMask + decimalToBinary(memoryIndexOnesSet).zfill(36)[index]

    return memoryIndexMask


def getSumOfMemoryVersion2(commandList):
    mask = ''
    memory = {}
    for row in commandList:
        if row[0] == 'mask':
            mask = row[2]
            continue
        memoryIndex = int(row[0][4:-1])
        desiredValue = int(row[2])
        memoryIndexOnesSet = memoryIndex | int(mask.replace("X", "0"), 2)
        memoryIndexList = getMemoryIndexList(memoryIndexOnesSet, mask)
        for index in memoryIndexList:
            memory[index] = desiredValue

    return sum(memory.values())


commandList = getCsv('fourteenth.txt')
sum = getSumOfMemoryVersion2(commandList)
print(sum)