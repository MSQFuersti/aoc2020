import csv


def getSeats(txtFileName='fifth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def extractSeatId(seatString):
    translation = seatString.maketrans("FBLR", "0101")
    binaryString = seatString.translate(translation)
    return int(binaryString, 2)



def getMissingSeat(seatIds):
    for seatId in seatIds:
        if seatId + 1 in seatIds:
            continue
        if seatId + 2 in seatIds:
            return seatId + 1


seatList = getSeats('fifth.txt')
seatIds = sorted([extractSeatId(seatString[0]) for seatString in seatList])
missingSeat = getMissingSeat(seatIds)

print(missingSeat)
