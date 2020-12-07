import csv
import math


def getAnswers(txtFileName='sixth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)

def extractAnswersPerGroup(answers):
    answersOfAllGroups = []
    groupAnswers = []
    for row in answers:
        if row:
            groupAnswers.extend(list(row[0]))
            continue

        answersOfAllGroups.append(groupAnswers)
        groupAnswers = []

    return answersOfAllGroups


def extractCommonAnswersPerGroup(answers):
    commonAnswersOfAllGroups = []
    commonGroupAnswers = list('abcdefghijklmnopqrstuvwxyz')
    for row in answers:
        if row:
            answersOfMember = list(row[0])
            commonGroupAnswers = list(set(commonGroupAnswers).intersection(set(answersOfMember)))
            continue

        commonAnswersOfAllGroups.append(commonGroupAnswers)
        commonGroupAnswers = list('abcdefghijklmnopqrstuvwxyz')

    return commonAnswersOfAllGroups


def extractNumberOfAnswersOfEachGroup(answersOfGroups):
    return [len(list(dict.fromkeys(answersOfSingleGroup))) for answersOfSingleGroup in answersOfGroups]

answers = getAnswers('sixth.txt')
answersOfGroups = extractCommonAnswersPerGroup(answers)
numberOfAnswersOfGroups = [len(answersOfSingleGroup) for answersOfSingleGroup in answersOfGroups]
print(sum(numberOfAnswersOfGroups))





groupedAnswers = extractAnswersPerGroup(answers)