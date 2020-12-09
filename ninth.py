import csv
import itertools

lengthPreamble = 25


def getCsv(txtFileName='ninth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def getNumbers():
    return [int(row[0]) for row in (getCsv('ninth.txt'))]


def findInvalidEntry(code):
    index = lengthPreamble
    while (index < len(code)):
        preamble = code[index - lengthPreamble: index]
        sumsInPreamble = [sum(set) for set in itertools.product(preamble, preamble)]
        if code[index] not in sumsInPreamble:
            return code[index]
        index += 1


def findContiguousSet(code, target = 133015568):
    firstIndex = 0
    secondIndex = 1
    while(firstIndex < len(code)):
        contiguousSet = code[firstIndex:secondIndex+1]
        sumContiguousSet = sum(contiguousSet)
        if sumContiguousSet == target:
            return contiguousSet
        elif sumContiguousSet < target:
            secondIndex += 1
        else:
            firstIndex += 1
            secondIndex = firstIndex + 1


code = getNumbers()
invalidEntry = findInvalidEntry(code)
contiguousSet = findContiguousSet(code, invalidEntry)
print(min(contiguousSet) + max(contiguousSet))