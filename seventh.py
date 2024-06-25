import csv


def getRules(txtFileName='seventh.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseRule(textRow):
    rule = []
    bag =  textRow[0] + ' ' + textRow[1]
    rule.append([bag])

    if textRow[4] == 'no':
        rule.append([])
        return rule

    containedBags = []
    index = 5
    while textRow[index]:
        containedBag = [textRow[index] + ' ' + textRow[index + 1]]
        containedBags.append(containedBag)
        index +=4
        if index >= len(textRow):
            break

    rule.append(containedBags)
    return rule


def findBagsContaining(rules, bagColor = ['shiny gold']):
    validBags = []
    invalidBags = []

    for rule in rules:
        containedBags = rule[1]
        if bagColor in containedBags:
            validBags.append(rule)
        else:
            invalidBags.append(rule)

    tempInvalidBags = []
    while(True):
        for invalidBag in invalidBags:
            if any(bag[0] in invalidBag[1] for bag in validBags):
                validBags.append(invalidBag)
            else:
                tempInvalidBags.append(invalidBag)

        if invalidBags == tempInvalidBags:
            break
        invalidBags = tempInvalidBags
        tempInvalidBags = []

    return validBags


rowRules = getRules('seventh.txt')
rules = [parseRule(rowRule) for rowRule in rowRules]
for rule in rules:
    print(rule)
    print(['shiny gold'] in rule[1])

validBags = findBagsContaining(rules)
print(len(validBags))

