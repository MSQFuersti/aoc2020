import csv
import copy


def getCsv(txtFileName='sixteenth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def getBlocks():
    csvFile = getCsv('sixteenth.txt')
    blocks = []
    firstIndex = 0
    for index, value in enumerate(csvFile):
        if value == []:
            blocks.append(csvFile[firstIndex:index])
            firstIndex = index + 1
    blocks.append(csvFile[firstIndex:])
    return blocks


def getAllValidValuesForTicketValues(rules):
    values = []
    for row in rules:
        for entry in row:
            if '-' in entry:
                numbers = entry.split('-')
                values.extend(list(range(int(numbers[0]), int(numbers[1]) + 1)))

    return list(set(values))


def getRangeRules(rawRules):
    rules = []
    for row in rawRules:
        ruleArray = []
        for entry in row:
            if '-' in entry:
                numbers = entry.split('-')
                ruleArray.extend(list(range(int(numbers[0]), int(numbers[1]) + 1)))
        rules.append(list(set(ruleArray)))

    return rules


def getSumOfInvalidValues(neighborTickets, rangeRules):
    invalidValues = []
    for row in neighborTickets[1:]:
        values = row[0].split(',')
        for value in values:
            if int(value) not in rangeRules:
                invalidValues.append(int(value))
    return sum(invalidValues)


def getValidNeighborTickets(neighborTickets, rangeRules):
    validNeighborTickets = []
    for ticket in neighborTickets[1:]:
        values = ticket[0].split(',')
        valid = True
        for value in values:
            if int(value) not in rangeRules:
                valid = False
                break
        if valid:
            validNeighborTickets.append(ticket)

    return validNeighborTickets


def determineCorrespondingPositionToRule(validNeighborTickets, rangeRules):
    rulePositionMatch = {}
    for position in range(len(validNeighborTickets[0][0].split(','))):
        possibleRuleIndizes = list(range(len(rangeRules)))
        for ticket in validNeighborTickets:
            ticketValues = ticket[0].split(',')
            rulesPerTicket = list()
            for ruleIndex in possibleRuleIndizes:
                actualTicketValue = int(ticketValues[position])
                actualRangeRule = rangeRules[ruleIndex]
                if actualTicketValue in actualRangeRule:
                    rulesPerTicket.append(ruleIndex)
            possibleRuleIndizes = list(set(possibleRuleIndizes).intersection(set(rulesPerTicket)))
            if len(possibleRuleIndizes) == 1:
                break
        rulePositionMatch[position] = possibleRuleIndizes

    return rulePositionMatch


def getUniqueRulePositionMatch(positionRuleMatch):
    rulePositionMatchCopy = copy.deepcopy(positionRuleMatch)
    uniqueRulePositionMatch = {}

    while True:
        for position in rulePositionMatchCopy:
            if len(rulePositionMatchCopy[position]) == 1:
                uniqueRulePositionMatch[rulePositionMatchCopy[position][0]] = position
                ruleIndexToRemove = rulePositionMatchCopy.pop(position)[0]
                for position in rulePositionMatchCopy:
                    if ruleIndexToRemove in rulePositionMatchCopy[position]:
                        rulePositionMatchCopy[position].remove(ruleIndexToRemove)
                break
        if not rulePositionMatchCopy:
            break

    return uniqueRulePositionMatch


rules, myTicket, neighborTickets = getBlocks()
rangeRules = getAllValidValuesForTicketValues(rules)
validNeighborTickets = getValidNeighborTickets(neighborTickets, rangeRules)
rangeRules = getRangeRules(rules)
positionRuleMatch = determineCorrespondingPositionToRule(validNeighborTickets, rangeRules)
uniqueRulePositionMatch = getUniqueRulePositionMatch(positionRuleMatch)
myTicket = myTicket[1][0].split(',')
finalValue = int(myTicket[uniqueRulePositionMatch[0]])
finalValue = finalValue * int(myTicket[uniqueRulePositionMatch[1]])
finalValue = finalValue * int(myTicket[uniqueRulePositionMatch[2]])
finalValue = finalValue * int(myTicket[uniqueRulePositionMatch[3]])
finalValue = finalValue * int(myTicket[uniqueRulePositionMatch[4]])
finalValue = finalValue * int(myTicket[uniqueRulePositionMatch[5]])
print(finalValue)
