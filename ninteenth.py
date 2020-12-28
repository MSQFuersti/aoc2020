import csv
import re


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
        return [specificRuleSet]

    allowedStringsOfIndex = []
    for rulesArray in specificRuleSet:
        decodedRulesArray = [getRuleForIndex(ruleIndex, rawRuleSet, decodedRuleSet) for ruleIndex in rulesArray]
        stringOfRulesArray = []
        for stringArray in decodedRulesArray:
            if not stringOfRulesArray:
                stringOfRulesArray = stringArray
            else:
                stringOfRulesArray = [first + second for first in stringOfRulesArray for second in stringArray]
        allowedStringsOfIndex.extend(stringOfRulesArray)

    decodedRuleSet[index] = allowedStringsOfIndex
    return allowedStringsOfIndex


csvFile = getCsv()
rawRuleSet, codes = parseRules(csvFile)
decodedRuleSet = {}
ruleOfZero = getRuleForIndex(0, rawRuleSet, decodedRuleSet)
for index, rule in enumerate(ruleOfZero):
    ruleOfZero[index] = '^' + rule + '$'
numberOfValidCodes = 0
for counter, code in enumerate(codes):
    print('code', counter)
    for count, rule in enumerate(ruleOfZero):
        print('rule', count)
        if re.findall(rule, code):
            numberOfValidCodes += 1
            break
print(numberOfValidCodes)
