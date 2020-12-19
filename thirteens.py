import csv


def getCsv(txtFileName='thirteenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


def getMinTime(csvFile):
    return int(csvFile[0][0])


def getLineIds(csvFile):
    return csvFile[1]


def getLineIdsOnly(listIds):
    listWithoutX = []
    for id in listIds:
        if id != 'x':
            listWithoutX.append(int(id))
    return listWithoutX


def getEarliestId(minTime, lineIds):
    timeStamp = minTime
    while True:
        for lineId in lineIds:
            if timeStamp % lineId == 0:
                return lineId * (timeStamp - minTime)


def getEarliestTimeStamp(lineIds):
    factor = int(lineIds[0])
    timeStamp = 0
    for index, value in enumerate(lineIds[1:]):
        if value == 'x':
            continue
        while (timeStamp+index+1) % int(value) != 0:
            timeStamp = timeStamp + factor
            print(timeStamp)
        factor = factor * int(value)

    return timeStamp


csvFile = getCsv('thirteenth.txt')
minTime = getMinTime(csvFile)
lineIds = getLineIds(csvFile)
#lineIdsOnly = getLineIdsOnly(lineIds)
#print(getEarliestId(minTime, lineIdsOnly))
print(getEarliestTimeStamp(lineIds))
