puzzleInput = '614752839'
# puzzleInput = '389125467'
labels = [int(char) for char in puzzleInput]
labels.extend(list(range(10, 1000001)))

successors = {}
for index, label in enumerate(labels):
    successors[label] = labels[index + 1] if index + 1 < len(labels) else labels[0]

currentCup = labels[0]
for _ in range(10000000):

    cupOne = successors[currentCup]
    cupTwo = successors[cupOne]
    cupThree = successors[cupTwo]
    takenCups = [cupOne, cupTwo, cupThree]

    successors[currentCup] = successors[cupThree]

    destinationCup = currentCup - 1
    while True:
        if destinationCup < 1:
            destinationCup = 1000000
            continue
        if destinationCup in takenCups:
            destinationCup = destinationCup - 1
            continue
        break

    successors[cupThree] = successors[destinationCup]
    successors[destinationCup] = cupOne

    currentCup = successors[currentCup]

print(successors[1] * successors[successors[1]])
