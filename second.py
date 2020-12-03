import csv

with open('second.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    policies = list(csv_reader)
    # print(policies)

# correctPasswords = 0
# for policy in policies:
#     password = policy[2]
#
#     policyLetter = (policy[1])[0]
#
#     policyRange = policy[0]
#     policyFirst, policySecond = policyRange.split('-')
#     policyFirst = int(policyFirst)
#     policySecond = int(policySecond)
#     print(policyFirst, policySecond)
#     policyLetterOccurance = password.count(policyLetter)
#     # print(policyLetterOccurance)
#     if policyFirst <= policyLetterOccurance <= policySecond:
#         correctPasswords = correctPasswords +1
#     print(password, policyLetter, policyRange, policyLetterOccurance)
#     print(correctPasswords)

correctPasswords = 0


def parseRowOfPasswordPolicyArray():
    global password, policyLetter, policyRange, policyFirst, policySecond
    password = policy[2]
    policyLetter = (policy[1])[0]
    policyRange = policy[0]
    policyFirst, policySecond = policyRange.split('-')
    policyFirst = int(policyFirst)
    policySecond = int(policySecond)


def increaseCounterIfXorConditionIsMet():
    global correctPasswords
    firstOccurrence = password[policyFirst - 1] == policyLetter
    secondOccurrence = password[policySecond - 1] == policyLetter
    if firstOccurrence != secondOccurrence:
        correctPasswords = correctPasswords + 1


for policy in policies:
    parseRowOfPasswordPolicyArray()
    increaseCounterIfXorConditionIsMet()
