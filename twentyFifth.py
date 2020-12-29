import csv
import copy


def getCsv(txtFileName='twentyfifth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def getPublicKeys(csvFile):
    cardPublicKey = int(csvFile[0][0])
    doorPublicKey = int(csvFile[1][0])

    return [cardPublicKey, doorPublicKey]


def getSecretLoopSize(publicKey):
    counter = 0
    value = 1
    subjectNumber = 7
    while True:
        if value == publicKey:
            return counter
        value = value * subjectNumber
        value = value % 20201227
        counter += 1


assert getSecretLoopSize(5764801) == 8
assert getSecretLoopSize(17807724) == 11


def getEncryptionKey(onesPublicKey, othersSecretLoopSize):
    value = 1
    for _ in range(othersSecretLoopSize):
        value = value * onesPublicKey
        value = value % 20201227
    return value


assert getEncryptionKey(17807724, 8) == 14897079
assert getEncryptionKey(5764801, 11) == 14897079

csvFile = getCsv()
cardPublicKey, doorPublicKey = getPublicKeys(csvFile)
cardSecretLoopSize = getSecretLoopSize(cardPublicKey)
doorSecretLoopSize = getSecretLoopSize(doorPublicKey)
encryptionKey = getEncryptionKey(cardPublicKey, doorSecretLoopSize)
encryptionKey2 = getEncryptionKey(doorPublicKey, cardSecretLoopSize)
print(encryptionKey)
print(encryptionKey2)
