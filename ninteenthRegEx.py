import csv
import re
import itertools

def getCsv(txtFileName='ninteenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseRules(csvFile):
    rulesDict = {}
    codes = []
    rules = True
    for row in csvFile:
        if not row:
            rules = False
            continue
        if not rules:
            codes.append(row[0])
            continue

        ruleNumber = int(row[0][:-1])
        rulesDict[ruleNumber] = []
        ruleSet = []
        for element in row[1:]:
            if element == 'a' or element == 'b':
                rulesDict[ruleNumber] = element
                break
            if element == '|':
                rulesDict[ruleNumber].append(ruleSet)
                ruleSet = []
                continue

            ruleSet.append(int(element))

        if ruleSet:
            rulesDict[ruleNumber].append(ruleSet)

    return [rulesDict, codes]


def getRuleForIndex(index, rawRuleSet, decodedRuleSet):
    if index in decodedRuleSet:
        return decodedRuleSet[index]

    specificRuleSet = rawRuleSet[index]
    if specificRuleSet == 'a' or specificRuleSet == 'b':
        return specificRuleSet

    if index in list(itertools.chain(*specificRuleSet)):
        pass

    expressionToReturn = '('
    for counter, rulesArray in enumerate(specificRuleSet):
        for ruleIndex in rulesArray:
            expressionToReturn = expressionToReturn + getRuleForIndex(ruleIndex, rawRuleSet, decodedRuleSet)
        if counter != len(specificRuleSet) - 1:
            expressionToReturn = expressionToReturn + '|'
    expressionToReturn = expressionToReturn + ')'
    return expressionToReturn


csvFile = getCsv()
rawRuleSet, codes = parseRules(csvFile)
decodedRuleSet = {}
ruleOfZero = '^' + getRuleForIndex(0, rawRuleSet, decodedRuleSet) + '$'
print(ruleOfZero)
numberOfValidCodes = 0
for code in codes:
    if re.findall(ruleOfZero, code):
        numberOfValidCodes += 1
print(numberOfValidCodes)