import csv
import numpy as np


def getCsv(txtFileName='eleventh.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseCharacter(character):
    if character == '.':
        return 0
    if character == 'L':
        return 1


def getInitialSeatList():
    rawSeatList = getCsv('eleventh.txt')
    return [[parseCharacter(character) for character in row[0]] for row in rawSeatList]


def upperStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    while True:
        actualRowIndex = rowIndex - counter
        if actualRowIndex < 0:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, columnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1


def lowerStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    numRows, numColumns = np.shape(matrixNp)
    while True:
        actualRowIndex = rowIndex + counter
        if actualRowIndex == numRows:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, columnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1


def leftStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    while True:
        actualColumnIndex = columnIndex - counter
        if actualColumnIndex < 0:
            return 0
        actualSeatPosition = np.array(matrix)[rowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1


def rightStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    numRows, numColumns = np.shape(matrixNp)
    while True:
        actualColumnIndex = columnIndex + counter
        if actualColumnIndex == numColumns:
            return 0
        actualSeatPosition = matrixNp[rowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1

def upperLeftStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    while True:
        actualRowIndex = rowIndex - counter
        actualColumnIndex = columnIndex - counter
        if actualColumnIndex < 0 or actualRowIndex < 0:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1


def upperRightStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    numRows, numColumns = np.shape(matrixNp)
    while True:
        actualRowIndex = rowIndex - counter
        actualColumnIndex = columnIndex + counter
        if actualColumnIndex == numColumns or actualRowIndex < 0:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1

def lowerRightStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    numRows, numColumns = np.shape(matrixNp)
    while True:
        actualRowIndex = rowIndex + counter
        actualColumnIndex = columnIndex + counter
        if actualColumnIndex == numColumns or actualRowIndex == numRows:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1

def lowerLeftStraightOccupied(matrix, rowIndex, columnIndex):
    counter = 1
    matrixNp = np.array(matrix)
    numRows, numColumns = np.shape(matrixNp)
    while True:
        actualRowIndex = rowIndex + counter
        actualColumnIndex = columnIndex - counter
        if actualColumnIndex < 0 or actualRowIndex == numRows:
            return 0
        actualSeatPosition = matrixNp[actualRowIndex, actualColumnIndex]
        if actualSeatPosition == 1:
            return 0
        if actualSeatPosition == 10:
            return 10
        counter = counter + 1


def findConvergedSeatListForAdjacentLineRule(initialSeatList):
    actualSeatList = np.array(initialSeatList)
    nextSeatList = np.zeros(np.shape(initialSeatList))

    numRows, numColumns = np.shape(initialSeatList)

    while True:
        for rowIndex in range(numRows):
            for columnIndex in range(numColumns):
                actualPosition = actualSeatList[rowIndex, columnIndex]
                if actualPosition == 0:
                    continue

                sumAdjacentPositions = 0

                sumAdjacentPositions += upperStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += lowerStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += leftStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += rightStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += upperLeftStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += upperRightStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += lowerRightStraightOccupied(actualSeatList, rowIndex, columnIndex)
                sumAdjacentPositions += lowerLeftStraightOccupied(actualSeatList, rowIndex, columnIndex)


                if actualPosition == 1:
                    if sumAdjacentPositions < 10:
                        nextSeatList[rowIndex][columnIndex] = 10
                    else:
                        nextSeatList[rowIndex][columnIndex] = 1
                if actualPosition == 10:
                    if sumAdjacentPositions >= 50:
                        nextSeatList[rowIndex][columnIndex] = 1
                    else:
                        nextSeatList[rowIndex][columnIndex] = 10

        if np.array_equal(actualSeatList, nextSeatList):
            return nextSeatList

        actualSeatList = nextSeatList
        nextSeatList = np.zeros(np.shape(initialSeatList))


def findConvergedSeatListForAdjacentRule(initialSeatList):
    actualSeatList = np.array(initialSeatList)
    nextSeatList = np.zeros(np.shape(initialSeatList))

    numRows, numColumns = np.shape(initialSeatList)

    while True:
        for rowIndex in range(numRows):
            for columnIndex in range(numColumns):
                actualPosition = actualSeatList[rowIndex][columnIndex]
                positionUpperLeft = actualSeatList[rowIndex - 1][
                    columnIndex - 1] if 0 < rowIndex and 0 < columnIndex else 0
                positionUp = actualSeatList[rowIndex - 1][columnIndex] if 0 < rowIndex else 0
                positionUpperRight = actualSeatList[rowIndex - 1][
                    columnIndex + 1] if 0 < rowIndex and columnIndex < numColumns - 1 else 0
                positionLeft = actualSeatList[rowIndex][columnIndex - 1] if 0 < columnIndex else 0
                positionRight = actualSeatList[rowIndex][columnIndex + 1] if columnIndex < numColumns - 1 else 0
                positionLowerLeft = actualSeatList[rowIndex + 1][
                    columnIndex - 1] if rowIndex < numRows - 1 and 0 < columnIndex else 0
                positionDown = actualSeatList[rowIndex + 1][columnIndex] if rowIndex < numRows - 1 else 0
                positionLowerRight = actualSeatList[rowIndex + 1][
                    columnIndex + 1] if rowIndex < numRows - 1 and columnIndex < numColumns - 1 else 0
                sumAdjacentPositions = positionUp + positionDown + positionLeft + positionRight + positionLowerLeft + positionLowerRight + positionUpperLeft + positionUpperRight
                if actualPosition == 1:
                    if sumAdjacentPositions < 10:
                        nextSeatList[rowIndex][columnIndex] = 10
                    else:
                        nextSeatList[rowIndex][columnIndex] = 1
                if actualPosition == 10:
                    if sumAdjacentPositions >= 40:
                        nextSeatList[rowIndex][columnIndex] = 1
                    else:
                        nextSeatList[rowIndex][columnIndex] = 10

        if np.array_equal(actualSeatList, nextSeatList):
            return nextSeatList

        actualSeatList = nextSeatList
        nextSeatList = np.zeros(np.shape(initialSeatList))


convergedSeatList = findConvergedSeatListForAdjacentLineRule(getInitialSeatList())
secondConvergedSeatList = findConvergedSeatListForAdjacentLineRule(convergedSeatList)
print(np.sum(convergedSeatList == 10))
