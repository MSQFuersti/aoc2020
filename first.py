import csv
import math
import time


def getNumbers():
    with open('input.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = list(csv_reader)
        return [int(item) for sublist in data for item in sublist]


def getKNumbersSummingUpTo(targetSum, numbers, k):
    for index, item in enumerate(numbers):
        remainingTarget = targetSum - item
        if k == 2:
            if remainingTarget in numbers:
                return [(targetSum - item), item]

        else:
            searchedNumbers = getKNumbersSummingUpTo(remainingTarget, numbers, k - 1)
            if searchedNumbers:
                searchedNumbers.append(item)
                return searchedNumbers


numbers = getNumbers()
numbers.extend([1, 2, 3, 4])
print((numbers))
start = time.time()
productOfTwoNumbersSummingUpTo2020 = math.prod(getKNumbersSummingUpTo(2020, numbers, 2))
timeTwo = time.time() - start
start = time.time()
productOfThreeNumbersSummingUpTo2020 = math.prod(getKNumbersSummingUpTo(2020, numbers, 3))
timeThree = time.time() - start
start = time.time()
productOfFiveNumbersSummingUpTo2020 = math.prod(getKNumbersSummingUpTo(2020, numbers, 5))
timeFive = time.time() - start
print(productOfTwoNumbersSummingUpTo2020, productOfThreeNumbersSummingUpTo2020, productOfFiveNumbersSummingUpTo2020)
print(timeTwo, timeThree, timeFive)
