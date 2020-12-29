import csv
import copy
import matplotlib.pyplot as plt


def getCsv(txtFileName='twentyfourth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseLineList(csvFile):
    instructionList = []
    for row in csvFile:
        instruction = list(row[0])
        instructionEntry = []
        while True:
            if not instruction:
                break
            recentInstruction = instruction.pop(0)
            if recentInstruction == 'e':
                instructionEntry.append(complex(2, 0))
                continue

            if recentInstruction == 'w':
                instructionEntry.append(complex(-2, 0))
                continue

            if recentInstruction == 's':
                recentInstruction = instruction.pop(0)
                if recentInstruction == 'e':
                    instructionEntry.append(complex(1, -1))
                    continue

                if recentInstruction == 'w':
                    instructionEntry.append(complex(-1, -1))
                    continue

            if recentInstruction == 'n':
                recentInstruction = instruction.pop(0)
                if recentInstruction == 'e':
                    instructionEntry.append(complex(1, 1))
                    continue

                if recentInstruction == 'w':
                    instructionEntry.append(complex(-1, 1))

        instructionList.append(instructionEntry)

    return instructionList


def getNumberOfBlackNeighbors(recentBlackTiles, tileToCheck):
    numberBlackNeighbors = 0
    if tileToCheck + complex(2, 0) in recentBlackTiles:
        numberBlackNeighbors += 1
    if tileToCheck + complex(-2, 0) in recentBlackTiles:
        numberBlackNeighbors += 1
    if tileToCheck + complex(1, -1) in recentBlackTiles:
        numberBlackNeighbors += 1
    if tileToCheck + complex(-1, -1) in recentBlackTiles:
        numberBlackNeighbors += 1
    if tileToCheck + complex(1, 1) in recentBlackTiles:
        numberBlackNeighbors += 1
    if tileToCheck + complex(-1, 1) in recentBlackTiles:
        numberBlackNeighbors += 1
    return numberBlackNeighbors



def determineBlackTilesAfterDays(blackTiles, days):
    recentBlackTiles = copy.deepcopy(blackTiles)
    nextBlackTiles = []
    for counter in range(days):
        reals = [z.real for z in recentBlackTiles]
        imags = [z.imag for z in recentBlackTiles]
        maxRe = int(max(reals)) + 4
        minRe = int(min(reals)) - 4
        maxIm = int(max(imags)) + 2
        minIm = int(min(imags)) - 2

        for imagIndex in range(minIm, maxIm + 1):
            if imagIndex % 2 == 0:
                for realIndex in range(0, minRe + 1, -2):
                    tileToCheck = complex(realIndex, imagIndex)
                    numberOfBlackNeighbors = getNumberOfBlackNeighbors(recentBlackTiles, tileToCheck)
                    if tileToCheck in recentBlackTiles and numberOfBlackNeighbors in [1, 2]:
                        nextBlackTiles.append(tileToCheck)
                    elif tileToCheck not in recentBlackTiles and numberOfBlackNeighbors == 2:
                        nextBlackTiles.append(tileToCheck)
                for realIndex in range(2, maxRe + 1, 2):
                    tileToCheck = complex(realIndex, imagIndex)
                    numberOfBlackNeighbors = getNumberOfBlackNeighbors(recentBlackTiles, tileToCheck)
                    if tileToCheck in recentBlackTiles and numberOfBlackNeighbors in [1, 2]:
                        nextBlackTiles.append(tileToCheck)
                    elif tileToCheck not in recentBlackTiles and numberOfBlackNeighbors == 2:
                        nextBlackTiles.append(tileToCheck)
            else:
                for realIndex in range(-1, minRe + 1, -2):
                    tileToCheck = complex(realIndex, imagIndex)
                    numberOfBlackNeighbors = getNumberOfBlackNeighbors(recentBlackTiles, tileToCheck)
                    if tileToCheck in recentBlackTiles and numberOfBlackNeighbors in [1, 2]:
                        nextBlackTiles.append(tileToCheck)
                    elif tileToCheck not in recentBlackTiles and numberOfBlackNeighbors == 2:
                        nextBlackTiles.append(tileToCheck)
                for realIndex in range(1, maxRe + 1, 2):
                    tileToCheck = complex(realIndex, imagIndex)
                    numberOfBlackNeighbors = getNumberOfBlackNeighbors(recentBlackTiles, tileToCheck)
                    if tileToCheck in recentBlackTiles and numberOfBlackNeighbors in [1, 2]:
                        nextBlackTiles.append(tileToCheck)
                    elif tileToCheck not in recentBlackTiles and numberOfBlackNeighbors == 2:
                        nextBlackTiles.append(tileToCheck)

        recentBlackTiles = nextBlackTiles[:]
        nextBlackTiles  =[]

    return recentBlackTiles


testCase = [['nwwswee']]
testInstruction = parseLineList(testCase)
assert testInstruction[0] == [complex(-1, 1), complex(-2, 0), complex(-1, -1), complex(2, 0), complex(2, 0)]
assert sum(testInstruction[0]) == complex(0, 0)

csvFile = getCsv()
instructionList = parseLineList(csvFile)
flippedTiles = [sum(instruction) for instruction in instructionList]
blackTiles = []
for tile in flippedTiles:
    if tile in blackTiles:
        blackTiles.remove(tile)
    else:
        blackTiles.append(tile)
print(len(blackTiles))

blackTilesAfterDays = determineBlackTilesAfterDays(blackTiles, 100)
print(len(blackTilesAfterDays))
