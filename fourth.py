import csv
import re


def getPassports(txtFileName='fourth.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parsePassports(passportList):
    passports = []
    tempPassport = []

    for row in passportList:
        if row:
            tempPassport.extend(row)
            continue
        passports.append(tempPassport)
        tempPassport = []

    return passports


def getPassportsWithRequiredFields(passports):
    passportsWithRequiredFields = []
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passportFields = [passportEntry.split(':')[0] for passportEntry in passport]
        isRequiredFieldInPassport = [requiredField in passportFields for requiredField in required]
        if all(isRequiredFieldInPassport):
            passportsWithRequiredFields.append(passport)

    return passportsWithRequiredFields


def validatePassports(passports):
    validPassports = []
    for passport in passports:
        valid = True
        for passportEntry in passport:
            passportField, passportValue = passportEntry.split(':')

            if passportField == 'byr':
                if len(passportValue) != 4:
                    valid = False
                    break
                if not (1920 <= int(passportValue) <= 2002):
                    valid = False
                    break

            if passportField == 'iyr':
                if len(passportValue) != 4:
                    valid = False
                    break
                if not (2010 <= int(passportValue) <= 2020):
                    valid = False
                    break

            if passportField == 'eyr':
                if len(passportValue) != 4:
                    valid = False
                    break
                if not (2020 <= int(passportValue) <= 2030):
                    valid = False
                    break

            if passportField == 'hgt':
                unit = passportValue[-2:]
                if unit != 'cm' and unit != 'in':
                    valid = False
                    break

                size = passportValue[:-2]
                if unit == 'cm' and not (150 <= int(size) <= 193):
                    valid = False
                    break
                if unit == 'in' and not (59 <= int(size) <= 76):
                    valid = False
                    break

            if passportField == 'ecl':
                if passportValue not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid = False
                    break

            if passportField == 'hcl':
                if passportValue[0] != '#':
                    valid = False
                    break
                if len(re.findall("[0-9a-f]", passportValue[1:])) != 6:
                    valid = False
                    break

            if passportField == 'pid':
                if len(re.findall("[0-9]", passportValue)) != 9:
                    valid = False
                    break

        if valid:
            validPassports.append(passport)

    return validPassports


passportList = getPassports('fourth.txt')
passports = parsePassports(passportList)
passportsWithRequiredFields = getPassportsWithRequiredFields(passports)
validPassports = validatePassports(passportsWithRequiredFields)

print(len(validPassports))

