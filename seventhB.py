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
        containedBag = [textRow[index] + ' ' + textRow[index + 1], textRow[index - 1]]
        containedBags.append(containedBag)
        index +=4
        if index >= len(textRow):
            break

    rule.append(containedBags)
    return rule

def extractNumberOfBagsContainedIn(bagKey, rules):
    bag = rules[bagKey]
    bags = 0
    for containedBag in bag:
        numberOfBags = int(containedBag[1])
        nameOfContainedBag = containedBag[0]
        bags = bags + numberOfBags + numberOfBags*extractNumberOfBagsContainedIn(nameOfContainedBag, rules)

    return bags



rawRules = getRules('seventh.txt')
rules = {parseRule(rowRule)[0][0] : parseRule(rowRule)[1] for rowRule in rawRules}
for rule in rules:
    print(rule, ':', rules[rule])

bagsInShinyGold = extractNumberOfBagsContainedIn('shiny gold', rules)
print(bagsInShinyGold)
