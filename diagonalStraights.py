import numpy as np


def diagonalStraights(matrix):
    lengthRows, lengthColumns = np.shape(matrix)

    for indexRow in range(lengthRows):
        for indexColumn in range(lengthColumns):
            lowerRight = matrix[range(indexRow +1, lengthRows), range(indexColumn +1, indexColumn +1 + lengthRows -indexRow -1)] if lengthRows - indexRow <= lengthColumns - indexColumn else matrix[range(indexRow +1, indexRow +1 + lengthColumns - indexColumn -1), range(indexColumn +1, lengthColumns)]
            upperRight = matrix[range(indexRow), range(indexColumn + indexRow, indexColumn, -1)] if indexRow <= lengthColumns - indexColumn -1 else matrix[range(indexRow,indexRow-(lengthColumns-1-indexColumn), -1),range(indexColumn + 1, lengthColumns)]
            lowerLeft = matrix[range(indexRow+1,lengthRows), range(indexColumn -1, indexColumn -1 -(lengthRows-1-indexRow),-1)] if lengthRows-1-indexRow <= indexColumn else matrix[range(indexRow+indexColumn,indexRow,-1),range(indexColumn)]
            print(upperRight)
            print(lowerRight)
            print(lowerLeft)


matrix = np.array(range(1,37)).reshape([6,6])
print(matrix)
diagonalStraights(matrix)
