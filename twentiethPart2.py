import csv
import numpy as np
import copy


def getCsv(txtFileName='twentiethTest.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseChars(char):
    if char == '#':
        return 1

    return 0


def parseTiles(csvFile):
    tileDict = {}
    recentTileId = None
    for row in csvFile:
        if not row:
            continue

        if len(row) > 1:
            recentTileId = int(row[1][:-1])
            tileDict[recentTileId] = []
            continue

        numberRow = [parseChars(char) for char in row[0]]
        tileDict[recentTileId].append(numberRow)

    for index in tileDict:
        tileDict[index] = np.array(tileDict[index])
    return tileDict


def getIndexMatchingDict(tiles):
    tiles = copy.deepcopy(tiles)
    tileIds = list(tiles.keys())
    indexMatchingDict = {}

    for index in tileIds:
        if index not in indexMatchingDict:
            indexMatchingDict[index] = {}
        tileToCheck = tiles.pop(index)
        upperEdge = tileToCheck[0, :]
        lowerEdge = tileToCheck[-1, :]
        leftEdge = tileToCheck[:, 0]
        rightEdge = tileToCheck[:, -1]
        for compareTileId in tiles:
            compareTile = tiles[compareTileId]
            if np.array_equal(upperEdge, compareTile[0, :]):
                indexMatchingDict[index]['upperEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdge'] = index
                continue
            if np.array_equal(upperEdge, compareTile[0, ::-1]):
                indexMatchingDict[index]['upperEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdgeFlipped'] = index
                continue
            if np.array_equal(upperEdge, compareTile[-1, :]):
                indexMatchingDict[index]['upperEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdge'] = index
                continue
            if np.array_equal(upperEdge, compareTile[-1, ::-1]):
                indexMatchingDict[index]['upperEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdgeFlipped'] = index
                continue
            if np.array_equal(upperEdge, compareTile[:, 0]):
                indexMatchingDict[index]['upperEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdge'] = index
                continue
            if np.array_equal(upperEdge, compareTile[::-1, 0]):
                indexMatchingDict[index]['upperEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdgeFlipped'] = index
                continue
            if np.array_equal(upperEdge, compareTile[:, -1]):
                indexMatchingDict[index]['upperEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdge'] = index
                continue
            if np.array_equal(upperEdge, compareTile[::-1, -1]):
                indexMatchingDict[index]['upperEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdgeFlipped'] = index
                continue

            if np.array_equal(lowerEdge, compareTile[0, :]):
                indexMatchingDict[index]['lowerEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdge'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[0, ::-1]):
                indexMatchingDict[index]['lowerEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdgeFlipped'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[-1, :]):
                indexMatchingDict[index]['lowerEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdge'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[-1, ::-1]):
                indexMatchingDict[index]['lowerEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdgeFlipped'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[:, 0]):
                indexMatchingDict[index]['lowerEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdge'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[::-1, 0]):
                indexMatchingDict[index]['lowerEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdgeFlipped'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[:, -1]):
                indexMatchingDict[index]['lowerEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdge'] = index
                continue
            if np.array_equal(lowerEdge, compareTile[::-1, -1]):
                indexMatchingDict[index]['lowerEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdgeFlipped'] = index
                continue

            if np.array_equal(leftEdge, compareTile[0, :]):
                indexMatchingDict[index]['leftEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdge'] = index
                continue
            if np.array_equal(leftEdge, compareTile[0, ::-1]):
                indexMatchingDict[index]['leftEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdgeFlipped'] = index
                continue
            if np.array_equal(leftEdge, compareTile[-1, :]):
                indexMatchingDict[index]['leftEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdge'] = index
                continue
            if np.array_equal(leftEdge, compareTile[-1, ::-1]):
                indexMatchingDict[index]['leftEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdgeFlipped'] = index
                continue
            if np.array_equal(leftEdge, compareTile[:, 0]):
                indexMatchingDict[index]['leftEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdge'] = index
                continue
            if np.array_equal(leftEdge, compareTile[::-1, 0]):
                indexMatchingDict[index]['leftEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdgeFlipped'] = index
                continue
            if np.array_equal(leftEdge, compareTile[:, -1]):
                indexMatchingDict[index]['leftEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdge'] = index
                continue
            if np.array_equal(leftEdge, compareTile[::-1, -1]):
                indexMatchingDict[index]['leftEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdgeFlipped'] = index
                continue

            if np.array_equal(rightEdge, compareTile[0, :]):
                indexMatchingDict[index]['rightEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdge'] = index
                continue
            if np.array_equal(rightEdge, compareTile[0, ::-1]):
                indexMatchingDict[index]['rightEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['upperEdgeFlipped'] = index
                continue
            if np.array_equal(rightEdge, compareTile[-1, :]):
                indexMatchingDict[index]['rightEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdge'] = index
                continue
            if np.array_equal(rightEdge, compareTile[-1, ::-1]):
                indexMatchingDict[index]['rightEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['lowerEdgeFlipped'] = index
                continue
            if np.array_equal(rightEdge, compareTile[:, 0]):
                indexMatchingDict[index]['rightEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdge'] = index
                continue
            if np.array_equal(rightEdge, compareTile[::-1, 0]):
                indexMatchingDict[index]['rightEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['leftEdgeFlipped'] = index
                continue
            if np.array_equal(rightEdge, compareTile[:, -1]):
                indexMatchingDict[index]['rightEdge'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdge'] = index
                continue
            if np.array_equal(rightEdge, compareTile[::-1, -1]):
                indexMatchingDict[index]['rightEdgeFlipped'] = compareTileId
                if compareTileId not in indexMatchingDict:
                    indexMatchingDict[compareTileId] = {}
                indexMatchingDict[compareTileId]['rightEdgeFlipped'] = index

    return indexMatchingDict


csvFile = getCsv()
tiles = parseTiles(csvFile)
print(len(tiles))
indexMatchingIds = getIndexMatchingDict(tiles)
print(indexMatchingIds)