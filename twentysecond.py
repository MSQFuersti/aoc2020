import csv
import copy


def getCsv(txtFileName='twentysecond.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseCardDecks(csvFile):
    playerOne = []
    playerTwo = []

    isFirst = True
    for row in csvFile:
        if len(row) > 1:
            continue
        if not row:
            isFirst = False
            continue
        if isFirst:
            playerOne.append(int(row[0]))
        else:
            playerTwo.append(int(row[0]))

    return [playerOne, playerTwo]


def playGame(playerOne, playerTwo):
    playerOne = copy.deepcopy(playerOne)
    playerTwo = copy.deepcopy(playerTwo)

    while True:
        if not playerOne or not playerTwo:
            break

        cardOne = playerOne.pop(0)
        cardTwo = playerTwo.pop(0)
        if cardOne > cardTwo:
            playerOne.extend([cardOne, cardTwo])
        else:
            playerTwo.extend([cardTwo, cardOne])

    factors = list(range(50, 0, -1))
    if playerOne:
        points = [a * b for a, b in zip(playerOne, factors)]
    else:
        points = [a * b for a, b in zip(playerTwo, factors)]

    return sum(points)


def playGameRecursive(playerOne, playerTwo):
    playerOne = copy.deepcopy(playerOne)
    playerTwo = copy.deepcopy(playerTwo)
    oldConfigsPlayerOne = []
    oldConfigsPlayerTwo = []
    while True:
        if not playerOne or not playerTwo:
            return [playerOne, playerTwo]
        if playerOne in oldConfigsPlayerOne and playerTwo in oldConfigsPlayerTwo:
            return [playerOne, []]

        oldConfigsPlayerOne.append(copy.deepcopy(playerOne))
        oldConfigsPlayerTwo.append(copy.deepcopy(playerTwo))
        cardOne = playerOne.pop(0)
        cardTwo = playerTwo.pop(0)
        if cardOne <= len(playerOne) and cardTwo <= len(playerTwo):
            subPlayerOne, subPlayerTwo = playGameRecursive(playerOne[:cardOne], playerTwo[:cardTwo])
            if subPlayerOne:
                playerOne.extend([cardOne, cardTwo])
            else:
                playerTwo.extend([cardTwo, cardOne])
        else:
            if cardOne > cardTwo:
                playerOne.extend([cardOne, cardTwo])
            else:
                playerTwo.extend([cardTwo, cardOne])




def getPoints(finishedPlayerOne, finishedPlayerTwo):
    maxPoints = max(len(finishedPlayerOne), len(finishedPlayerTwo))
    factor = list(range(maxPoints, 0, -1))
    if finishedPlayerOne:
        pointsList = [a * b for a, b in zip(finishedPlayerOne, factor)]
    else:
        pointsList = [a * b for a, b in zip(finishedPlayerTwo, factor)]

    return sum(pointsList)


csvFiles = getCsv()
arrayPlayerOne, arrayPlayerTwo = parseCardDecks(csvFiles)
finishedPlayerOne, finishedPlayerTwo = playGameRecursive(arrayPlayerOne, arrayPlayerTwo)
points = getPoints(finishedPlayerOne, finishedPlayerTwo)
print(points)
pass
