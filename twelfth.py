import csv
import numpy as np
import cmath


def getCsv(txtFileName='twelfth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def getCommands():
    csvFile = getCsv('twelfth.txt')
    return [[row[0][0], int(row[0][1:])] for row in csvFile]

def getPositionAfterCommands(commandList):
    orientation = complex(1,0)
    position = complex(0,0)
    for command in commandList:
        if command[0] == 'F':
            position = position + orientation * command[1]
        if command[0] == 'R':
            changeOrientation = cmath.rect(1, -1 * np.deg2rad(command[1]))
            changeOrientation = complex(int(changeOrientation.real), int(changeOrientation.imag))
            orientation = orientation * changeOrientation
        if command[0] == 'L':
            changeOrientation = cmath.rect(1, np.deg2rad(command[1]))
            changeOrientation = complex(int(changeOrientation.real), int(changeOrientation.imag))
            orientation = orientation * changeOrientation
        if command[0] == 'E':
            position = position + complex(command[1], 0)
        if command[0] == 'W':
            position = position + complex(-1*command[1], 0)
        if command[0] == 'N':
            position = position + complex(0, command[1])
        if command[0] == 'S':
            position = position + complex(0, -1 * command[1])

    return position


def getPositionAfterCommandsWithWayPoint(commandList):
    wayPoint = complex(10, 1)
    position = complex(0, 0)
    for command in commandList:
        if command[0] == 'F':
            position = position + wayPoint * command[1]
        if command[0] == 'R':
            changeOrientation = cmath.rect(1, -1 * np.deg2rad(command[1]))
            changeOrientation = complex(int(changeOrientation.real), int(changeOrientation.imag))
            wayPoint = wayPoint * changeOrientation
        if command[0] == 'L':
            changeOrientation = cmath.rect(1, np.deg2rad(command[1]))
            changeOrientation = complex(int(changeOrientation.real), int(changeOrientation.imag))
            wayPoint = wayPoint * changeOrientation
        if command[0] == 'E':
            wayPoint = wayPoint + complex(command[1], 0)
        if command[0] == 'W':
            wayPoint = wayPoint + complex(-1*command[1], 0)
        if command[0] == 'N':
            wayPoint = wayPoint + complex(0, command[1])
        if command[0] == 'S':
            wayPoint = wayPoint + complex(0, -1 * command[1])

    return position



commandList = getCommands()
finalPosition = getPositionAfterCommandsWithWayPoint(commandList)
print(int(abs(finalPosition.real) + abs(finalPosition.imag)))
