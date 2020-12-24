import csv
import numpy as np
from scipy import signal
import copy


def getCsv(txtFileName='seventeenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseCharacter(character):
    value = 1 if character == '#' else 0
    return value


def parseInput(csvFile):
    return [[parseCharacter(character) for character in (list(row[0]))] for row in csvFile]


def prepareInitialArray(input, plannedIterationSteps):
    inputArray = np.array(input)
    inputArrayShape = list(np.shape(inputArray))

    initialArrayShapeXAxis = inputArrayShape[0] + 2 * plannedIterationSteps
    initialArrayShapeYAxis = inputArrayShape[1] + 2 * plannedIterationSteps
    initialArrayShapeZAxis = 1 + 2 * plannedIterationSteps
    initialArrayShape = [initialArrayShapeXAxis, initialArrayShapeYAxis, initialArrayShapeZAxis]
    initialArray = np.zeros(initialArrayShape)
    initialArray[plannedIterationSteps:plannedIterationSteps + inputArrayShape[0],
    plannedIterationSteps:plannedIterationSteps + inputArrayShape[1], plannedIterationSteps] = inputArray
    return initialArray


def determineConfiguration(initialState, iterationSteps):
    recentState = copy.deepcopy(initialState)
    summationFilter = np.ones((3, 3, 3))
    summationFilter[1, 1, 1] = 0
    for counter in range(iterationSteps):
        summationArray = signal.convolve(recentState, summationFilter, 'same', 'direct')
        sumIsThree = summationArray == 3
        sumIsNotTwoOrThree = np.logical_not(np.logical_or(summationArray == 2, summationArray == 3))
        recentState[np.logical_and(recentState == 0, sumIsThree)] = 1
        recentState[np.logical_and(recentState == 1, sumIsNotTwoOrThree)] = 0
    return recentState


csvFile = getCsv()
providedInput = parseInput(csvFile)
iterationSteps = 6
initialArray = prepareInitialArray(providedInput, iterationSteps)
finalState = determineConfiguration(initialArray, iterationSteps)
print(np.sum(finalState))
