puzzleInput = '614752839'
# puzzleInput = '389125467'
labels = [int(char) for char in puzzleInput]
labels.extend(list(range(10, 1000001)))

currentCup = labels[0]
for counter in range(10000000):
    if counter % 1000 == 0:
        print(counter)
    indexCurrentCup = labels.index(currentCup)
    takenCups = []
    for counter in range(3):
        takenCups.append(labels.pop(indexCurrentCup + 1)) if indexCurrentCup + 1 < len(labels) else takenCups.append(
            labels.pop(0))
    destinationCup = currentCup - 1
    while True:
        if destinationCup in labels:
            break
        elif destinationCup > 1:
            destinationCup -= 1
        else:
            destinationCup = 1000000
    destinationCupIndex = labels.index(destinationCup)
    labels[destinationCupIndex + 1: destinationCupIndex + 1] = takenCups
    indexCurrentCup = labels.index(currentCup)
    currentCup = labels[indexCurrentCup + 1] if indexCurrentCup + 1 < len(labels) else labels[0]
