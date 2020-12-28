import csv
import copy


def getCsv(txtFileName='twentyfirst.txt'):
    with open(txtFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        return list(csv_reader)


def parseFood(csvFile):
    parsedFoodList = []
    for row in csvFile:
        for index, word in enumerate(row):
            if 'contains' in word:
                ingredients = row[:index]
                allergens = row[index + 1:]
                for index, word in enumerate(allergens):
                    allergens[index] = allergens[index][:-1]
                parsedFoodList.append([ingredients, allergens])
                break
    return parsedFoodList


def getListOfAllergens(parsedFoodList):
    allergens = []
    for food in parsedFoodList:
        allergens.extend(food[1])
    return list(set(allergens))


def getListOfIngredients(parsedFoodList):
    ingredients = []
    for food in parsedFoodList:
        ingredients.extend(food[0])
    return list(set(ingredients))


def getIngredientsNotBeingAllergens(listOfAllPossibleIngredients, listOfAllPossibleAllergens, parsedFoodList):
    allergenIngredientDict = getAllergenIngredientDict(listOfAllPossibleAllergens, parsedFoodList)

    setOfPossibleIngredients = []
    [setOfPossibleIngredients.extend(array) for array in allergenIngredientDict.values()]
    setOfPossibleIngredients = list(set(setOfPossibleIngredients))
    listOfAllPossibleIngredients = copy.deepcopy(listOfAllPossibleIngredients)
    for possibleAllergenIngredient in setOfPossibleIngredients:
        listOfAllPossibleIngredients.remove(possibleAllergenIngredient)
    return listOfAllPossibleIngredients


def getAllergenIngredientDict(listOfAllPossibleAllergens, parsedFoodList):
    allergenIngredientDict = {}
    for allergen in listOfAllPossibleAllergens:
        allergenIngredientDict[allergen] = []
        for food in parsedFoodList:
            if allergen in food[1]:
                if not allergenIngredientDict[allergen]:
                    allergenIngredientDict[allergen] = food[0]
                else:
                    allergenIngredientDict[allergen] = list(
                        set(allergenIngredientDict[allergen]).intersection(set(food[0])))
    return allergenIngredientDict


def countOcurencesOfNonAllergenIngredients(setOfNonAllergenIngredients, parsedFoodList):
    counter = 0
    for ingredient in setOfNonAllergenIngredients:
        for food in parsedFoodList:
            for ingredientToCheck in food[0]:
                if ingredient == ingredientToCheck:
                    counter += 1
    return counter


def getUniqueAllergenIngredientDict(allergenIngredientDict):
    allergenIngredientDict = copy.deepcopy(allergenIngredientDict)
    uniqueAllergenIngredientDict = {}
    while True:
        if not allergenIngredientDict:
            break
        for allergen in allergenIngredientDict:
            if len(allergenIngredientDict[allergen]) == 1:
                removedIngredient = allergenIngredientDict[allergen][0]
                uniqueAllergenIngredientDict[allergen] = removedIngredient
                allergenIngredientDict.pop(allergen)
                for leftAllergen in allergenIngredientDict:
                    if removedIngredient in allergenIngredientDict[leftAllergen]:
                        allergenIngredientDict[leftAllergen].remove(removedIngredient)
                break

    return uniqueAllergenIngredientDict

csvFile = getCsv()
parsedFoodList = parseFood(csvFile)
listOfAllPossibleIngredients = getListOfIngredients(parsedFoodList)
listOfAllPossibleAllergens = getListOfAllergens(parsedFoodList)

nonAllergenIngredients = getIngredientsNotBeingAllergens(listOfAllPossibleIngredients, listOfAllPossibleAllergens,
                                                         parsedFoodList)
occurrencesOfNonAllergenIngredients = countOcurencesOfNonAllergenIngredients(nonAllergenIngredients, parsedFoodList)

print(occurrencesOfNonAllergenIngredients)

allergenIngredientDict = getAllergenIngredientDict(listOfAllPossibleAllergens, parsedFoodList)
uniqueAllergenIngredientDict = getUniqueAllergenIngredientDict(allergenIngredientDict)
sortedAllergens = list(uniqueAllergenIngredientDict.keys())
sortedAllergens.sort()
requestedIngredientList = [uniqueAllergenIngredientDict[allergen] for allergen in sortedAllergens]
print(','.join(requestedIngredientList))
