array = [0, 20, 7, 16, 1, 18, 15]
lastIndizes = {}
for index in range(len(array) - 1):
    lastIndizes[array[index]] = index

recentElement = array[-1]
for index in range(len(array)-1, 30000000 - 1):
    if recentElement in lastIndizes.keys():
        nextRecentElement = index - lastIndizes[recentElement]
        lastIndizes[recentElement] = index
        recentElement = nextRecentElement
        continue
    nextRecentElement = 0
    lastIndizes[recentElement] = index
    recentElement = nextRecentElement

print(recentElement)




