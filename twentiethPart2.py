import csv
import numpy as np
import copy
import math


class Neighbors:
    east = None
    west = None
    north = None
    south = None

    def getNumberOfNeighbors(self):
        return int(self.east != None) + int(self.west != None) + (self.north != None) + int(self.south != None)

    def flipud(self):
        self.north, self.south = self.south, self.north

    def fliplr(self):
        self.east, self.west = self.west, self.east

    def rot90(self, times):
        if times % 4 == 1:
            self. north, self.west, self.south, self.east = self.east, self. north, self.west, self.south

        elif times % 4 == 2:
            self.flipud()
            self.fliplr()

        elif times % 4 == 3:
            self.north, self.west, self.south, self.east = self.west, self.south, self.east, self.north


class Tile:
    id = None
    array: np.ndarray = None
    neighbors = None

    def __init__(self):
        self.neighbors = Neighbors()

    def flipud(self):
        self.array = np.flipud(self.array)
        self.neighbors.flipud()

    def fliplr(self):
        self.array = np.fliplr(self.array)
        self.neighbors.fliplr()

    def rot90(self, times):
        self.array = np.rot90(self.array, times)
        self.neighbors.rot90(times)

    def getNumberOfNeighbors(self):
        return self.neighbors.getNumberOfNeighbors()

    def getEastBorder(self):
        return self.array[:, -1]

    def getWestBorder(self):
        return self.array[:, 0]

    def getSouthBorder(self):
        return self.array[-1, :]

    def getNorthBorder(self):
        return self.array[0, :]

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
        array = np.array(tileDict[index])
        tile = Tile()
        tile.array = array
        tile.id = index
        tileDict[index] = tile
    return tileDict


def determineNeighborsOfTiles(tiles):
    tilesList = list(tiles.values())
    for index, tileToCheck in enumerate(tilesList):
        northBorderToCheck = tileToCheck.getNorthBorder()
        westBorderToCheck = tileToCheck.getWestBorder()
        southBorderToCheck = tileToCheck.getSouthBorder()
        eastBorderToCheck = tileToCheck.getEastBorder()
        for tileToCompare in tilesList[index + 1:]:
            northBorderToCompare = tileToCompare.getNorthBorder()
            westBorderToCompare = tileToCompare.getWestBorder()
            southBorderToCompare = tileToCompare.getSouthBorder()
            eastBorderToCompare = tileToCompare.getEastBorder()
            if np.array_equal(northBorderToCheck, northBorderToCompare) or np.array_equal(northBorderToCheck, np.flip(northBorderToCompare)):
                tileToCheck.neighbors.north = tileToCompare.id
                tileToCompare.neighbors.north = tileToCheck.id
                continue
            if np.array_equal(northBorderToCheck, westBorderToCompare) or np.array_equal(northBorderToCheck, np.flip(westBorderToCompare)):
                tileToCheck.neighbors.north = tileToCompare.id
                tileToCompare.neighbors.west = tileToCheck.id
                continue
            if np.array_equal(northBorderToCheck, southBorderToCompare) or np.array_equal(northBorderToCheck, np.flip(southBorderToCompare)):
                tileToCheck.neighbors.north = tileToCompare.id
                tileToCompare.neighbors.south = tileToCheck.id
                continue
            if np.array_equal(northBorderToCheck, eastBorderToCompare) or np.array_equal(northBorderToCheck, np.flip(eastBorderToCompare)):
                tileToCheck.neighbors.north = tileToCompare.id
                tileToCompare.neighbors.east = tileToCheck.id
                continue

            if np.array_equal(westBorderToCheck, northBorderToCompare) or np.array_equal(westBorderToCheck, np.flip(northBorderToCompare)):
                tileToCheck.neighbors.west = tileToCompare.id
                tileToCompare.neighbors.north = tileToCheck.id
                continue
            if np.array_equal(westBorderToCheck, westBorderToCompare) or np.array_equal(westBorderToCheck, np.flip(westBorderToCompare)):
                tileToCheck.neighbors.west = tileToCompare.id
                tileToCompare.neighbors.west = tileToCheck.id
                continue
            if np.array_equal(westBorderToCheck, southBorderToCompare) or np.array_equal(westBorderToCheck, np.flip(southBorderToCompare)):
                tileToCheck.neighbors.west = tileToCompare.id
                tileToCompare.neighbors.south = tileToCheck.id
                continue
            if np.array_equal(westBorderToCheck, eastBorderToCompare) or np.array_equal(westBorderToCheck, np.flip(eastBorderToCompare)):
                tileToCheck.neighbors.west = tileToCompare.id
                tileToCompare.neighbors.east = tileToCheck.id
                continue

            if np.array_equal(southBorderToCheck, northBorderToCompare) or np.array_equal(southBorderToCheck, np.flip(northBorderToCompare)):
                tileToCheck.neighbors.south = tileToCompare.id
                tileToCompare.neighbors.north = tileToCheck.id
                continue
            if np.array_equal(southBorderToCheck, westBorderToCompare) or np.array_equal(southBorderToCheck, np.flip(westBorderToCompare)):
                tileToCheck.neighbors.south = tileToCompare.id
                tileToCompare.neighbors.west = tileToCheck.id
                continue
            if np.array_equal(southBorderToCheck, southBorderToCompare) or np.array_equal(southBorderToCheck, np.flip(southBorderToCompare)):
                tileToCheck.neighbors.south = tileToCompare.id
                tileToCompare.neighbors.south = tileToCheck.id
                continue
            if np.array_equal(southBorderToCheck, eastBorderToCompare) or np.array_equal(southBorderToCheck, np.flip(eastBorderToCompare)):
                tileToCheck.neighbors.south = tileToCompare.id
                tileToCompare.neighbors.east = tileToCheck.id
                continue

            if np.array_equal(eastBorderToCheck, northBorderToCompare) or np.array_equal(eastBorderToCheck, np.flip(northBorderToCompare)):
                tileToCheck.neighbors.east = tileToCompare.id
                tileToCompare.neighbors.north = tileToCheck.id
                continue
            if np.array_equal(eastBorderToCheck, westBorderToCompare) or np.array_equal(eastBorderToCheck, np.flip(westBorderToCompare)):
                tileToCheck.neighbors.east = tileToCompare.id
                tileToCompare.neighbors.west = tileToCheck.id
                continue
            if np.array_equal(eastBorderToCheck, southBorderToCompare) or np.array_equal(eastBorderToCheck, np.flip(southBorderToCompare)):
                tileToCheck.neighbors.east = tileToCompare.id
                tileToCompare.neighbors.south = tileToCheck.id
                continue
            if np.array_equal(eastBorderToCheck, eastBorderToCompare) or np.array_equal(eastBorderToCheck, np.flip(eastBorderToCompare)):
                tileToCheck.neighbors.east = tileToCompare.id
                tileToCompare.neighbors.east = tileToCheck.id
                continue
    pass

def getIdsOfCornerTiles(tiles):
    return [tiles[index].id for index in tiles if tiles[index].getNumberOfNeighbors() == 2]


def getProductOfCornerIds():
    cornerIds = getIdsOfCornerTiles(tiles)
    for index in range(1, len(cornerIds)):
        cornerIds[index] = cornerIds[index] * cornerIds[index - 1]
    print(cornerIds[-1])


def getFirstCornerTile(tiles):
    for index in tiles:
        if tiles[index].getNumberOfNeighbors() == 2:
            return tiles[index]


def getInitialArray(sideLength):
    return [[None for _ in range(sideLength)] for _ in range(sideLength)]


assert getInitialArray(2) == [[None, None], [None, None]]


def getArrayOfOrderOfTiles(tiles):
    sideLength = int(math.sqrt(len(tiles)))
    arrayOfOrderedTiles = getInitialArray(sideLength)
    firstCornerTile = getFirstCornerTile(tiles)

    for rowIndex in range(sideLength):
        for columnIndex in range(sideLength):

            if rowIndex == 0 and columnIndex == 0:
                arrayOfOrderedTiles[rowIndex][columnIndex] = firstCornerTile
                if firstCornerTile.neighbors.east == None:
                    firstCornerTile.fliplr()
                if firstCornerTile.neighbors.south == None:
                    firstCornerTile.flipud()
                continue
            previousTileWest = arrayOfOrderedTiles[rowIndex][columnIndex - 1]
            previousIndexWest = previousTileWest.id
            thisTileIndex = previousTileWest.neighbors.east
            thisTile = tiles[thisTileIndex]
            if thisTile.neighbors.east =
            arrayOfOrderedTiles[rowIndex][columnIndex] = tiles[thisTileIndex]
            pass


csvFile = getCsv()
tiles = parseTiles(csvFile)
numberOfTiles = len(tiles)
print(numberOfTiles)
determineNeighborsOfTiles(tiles)
getProductOfCornerIds()
arrayOfOrderedTiles = getArrayOfOrderOfTiles(tiles)
pass
