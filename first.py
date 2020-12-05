import csv
import math

def getNumbers():
    with open('input.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = list(csv_reader)
        return [int(item) for sublist in data for item in sublist]


def getTwoNumbersSummingUpTo(targetSum, numbers):
    for item in numbers:
        if targetSum - item in numbers:
            return [(targetSum - item), item]


def getThreeNumbersSummingUpTo(targetSum, numbers):
    for item in numbers:
        remainingTarget = targetSum - item
        searchedNumbers = getTwoNumbersSummingUpTo(remainingTarget, numbers)
        if searchedNumbers:
            searchedNumbers.append(item)
            return searchedNumbers


numbers = getNumbers()
productOfTwoNumbersSummingUpTo2020 = math.prod(getTwoNumbersSummingUpTo(2020, numbers))
productOfThreeNumbersSummingUpTo2020 = math.prod(getThreeNumbersSummingUpTo(2020, numbers))
print(productOfTwoNumbersSummingUpTo2020, productOfThreeNumbersSummingUpTo2020)
