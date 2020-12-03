import csv
import math


def getHill(txtFileName='third.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def treesOnSlope(hill, rightShift):
    trees = [treeInRow(index, rightShift, row) for index, row in enumerate(hill)]
    return sum(trees)


def treeInRow(index, rightShift, row):
    rowLength = len(row[0])
    columnIndex = (rightShift * index) % rowLength
    rowPosition = row[0][columnIndex]
    return rowPosition == '#'


hill = getHill('third.txt')
numberOfTrees = []
for rightShift in [1, 3, 5, 7]:
    numberOfTrees.append(treesOnSlope(hill, rightShift))

fastHill = hill[0::2]
numberOfTrees.append(treesOnSlope(fastHill, 1))

print(math.prod(numberOfTrees))
