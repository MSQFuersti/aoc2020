import csv

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = list(csv_reader)
    flattenData = [int(item) for sublist in data for item in sublist]
    print(flattenData)

for item in flattenData:
    if 2020 - item in flattenData:
        print((2020 - item) * item)
        break

for outerIndex, outerValue in enumerate(flattenData):
    for innerIndex, innerValue in enumerate(flattenData[outerIndex + 1:]):
        if 2020 - outerValue - innerValue in flattenData[innerIndex + 1:]:
            print(outerValue * innerValue * (2020 - outerValue - innerValue))
            break
