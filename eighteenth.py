import csv
import numpy as np
from scipy import signal
import copy


def getCsv(txtFileName='eighteenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)


def solveEquationSimple(row):
    level = 0
    charList = list(row)
    result = [None]
    recentOperation = [None]
    for element in charList:
        if element == ' ':
            continue
        if element == '(':
            level = level + 1
            result.append(None)
            recentOperation.append(None)
            continue
        if element == ')':
            level = level - 1
            recentOperation.pop()
            innerResult = result.pop()
            if result[level] is None:
                result[level] = innerResult
            else:
                if recentOperation[level] == '+':
                    result[level] = result[level] + innerResult
                elif recentOperation[level] == '*':
                    result[level] = result[level] * innerResult
            continue
        if element == '*' or element == '+':
            recentOperation[level] = element
            continue

        number = int(element)
        if result[level] is None:
            result[level] = number
        else:
            if recentOperation[level] == '+':
                result[level] = result[level] + number
            elif recentOperation[level] == '*':
                result[level] = result[level] * number
    return result[0]


def solveEquationAdvanced(row):
    level = 0
    charList = list(row)
    result = [None]
    recentOperation = [None]
    intermediateSummation = [None]
    for element in charList:
        if element == '(':
            level = level + 1
            result.append(None)
            recentOperation.append(None)
            intermediateSummation.append(None)
            continue
        if element == ')':
            level = level - 1
            lastResult = result.pop()
            lastIntermediateSummation = intermediateSummation.pop()
            lastOperation = recentOperation.pop()
            if lastIntermediateSummation is not None:
                if lastResult is None:
                    lastResult = lastIntermediateSummation
                else:
                    lastResult = lastResult * lastIntermediateSummation
            if intermediateSummation[level] is None:
                intermediateSummation[level] = lastResult
            else:
                intermediateSummation[level] = lastResult + intermediateSummation[level]
            continue
        if element == ' ' or element == '(' or element == ')':
            continue
        if element == '*':
            if result[level] is None:
                result[level] = intermediateSummation[level]
            else:
                result[level] = result[level] * intermediateSummation[level]
            intermediateSummation[level] = None
            recentOperation[level] = '*'
            continue
        if element == '+':
            # Do something before
            recentOperation[level] = '+'
            continue

        number = int(element)
        if intermediateSummation[level] is None:
            intermediateSummation[level] = number
        else:
            intermediateSummation[level] += number

    if intermediateSummation[0] is not None:
        if result[0] is None:
            result[0] = intermediateSummation[0]
        else:
            result[0] = result[0] * intermediateSummation[0]
    return result[0]




def solveEquationsSimple(csvFile):
    return [solveEquationSimple(row[0]) for row in csvFile]


def solveEquationsAdvanced(csvFile):
    return [solveEquationAdvanced(row[0]) for row in csvFile]


solutions = solveEquationsAdvanced(getCsv())
print(sum(solutions))

