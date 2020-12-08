import csv
import math


def getProgram(txtFileName='eighth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def executeProgram(sourceProgram):
    program = [row.copy() for row in sourceProgram]
    accumulator = 0
    index = 0

    while (True):
        if index >= len(program):
            break

        line = program[index]
        if line[2]:
            break
        elif line[0] == 'acc':
            accumulator += line[1]
            index += 1
            line[2] = True
        elif line[0] == 'nop':
            index += 1
            line[2] = True
        elif line[0] == 'jmp':
            index += line[1]
            line[2] = True

    return [index, accumulator]


def doesProgramTerminate(program):
    newProgram = [row.copy() for row in program]
    return executeProgram(newProgram)[0] >= len(newProgram)

def returnResultOfFixedProgram(program):
    for index, line in enumerate(program):
        if line[0] == 'nop' or line[0] =='jmp':
            newProgram = [row.copy() for row in program]
            newProgram[index] = ['nop' if line[0] == 'jmp' else 'jmp', line[1], False]
            if doesProgramTerminate(newProgram):
                return executeProgram(newProgram)


program = getProgram()
program = [[line[0], int(line[1]), False] for line in program]
newProgram = program.copy()
print(executeProgram(program)[1])
print(returnResultOfFixedProgram(program)[1])
