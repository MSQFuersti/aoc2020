import csv
import numpy as np


def getCsv(txtFileName='tenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def getJolts():
    return [int(row[0]) for row in (getCsv('tenth.txt'))]

functionCalls = 0
def getProductOfOneJoltAndThreeJoltsDifferences(jolts):

    jolts.sort()
    joltsDevice = np.max(jolts) + 3
    minuend = np.append(np.array(jolts), joltsDevice)
    joltsPlugSocket = np.array([0])
    subtrahend = np.append(joltsPlugSocket, np.array(jolts))
    joltDifferences = minuend - subtrahend
    numOnes = np.sum(joltDifferences == 1)
    numThrees = np.sum(joltDifferences == 3)
    return numOnes*numThrees

def getNumberOfDistinctArrangementsByRecursion(jolts):
    global functionCalls

    if len(jolts) == 1:
        functionCalls += 1
        print(functionCalls)
        return 1

    numberOfArrangements = getNumberOfDistinctArrangementsByRecursion(jolts[1:])

    if len(jolts) > 2 and jolts[2] - jolts[0] <= 3:
        numberOfArrangements += getNumberOfDistinctArrangementsByRecursion(jolts[2:])
    if len(jolts) > 3 and jolts[3] - jolts[0] <= 3:
        numberOfArrangements += getNumberOfDistinctArrangementsByRecursion(jolts[3:])

    return numberOfArrangements

def getNumberOfDistinctArrangementsByDynamicProgramming(jolts):
    joltsWithSocketPlug = jolts[:]
    joltsWithSocketPlug.insert(0 ,0)
    numberofArrangements = []
    for index, value in enumerate(joltsWithSocketPlug):
        if index == 0:
            numberofArrangements.append(1)
            continue

        numberofArrangementsUntilIndex = 0
        if index > 2 and value - joltsWithSocketPlug[index - 3] <= 3:
            numberofArrangementsUntilIndex += numberofArrangements[-3]
        if index > 1 and value - joltsWithSocketPlug[index - 2] <= 3:
            numberofArrangementsUntilIndex += numberofArrangements[-2]
        if value - joltsWithSocketPlug[index - 1] <= 3:
            numberofArrangementsUntilIndex += numberofArrangements[-1]

        numberofArrangements.append(numberofArrangementsUntilIndex)

    return numberofArrangements[-1]



jolts = getJolts()
print(getProductOfOneJoltAndThreeJoltsDifferences(jolts))
print(getNumberOfDistinctArrangementsByDynamicProgramming(jolts))