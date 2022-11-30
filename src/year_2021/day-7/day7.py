from typing import List


def getGasCost(n: int):
    temp = 0
    for i in range(1, n+1):
        temp += i
    return temp


def calcGasCost(crabs: List[int] = [], toPosition: int = 0):
    gasCost = 0
    for crab in crabs:
        gasCost += getGasCost(abs(crab - toPosition))

    return gasCost


def day7(fileName: str):
    file = open(fileName, "r")
    allLines = file.read().splitlines()

    crabs = allLines[0].split(",")
    for i in range(0, len(crabs)):
        crabs[i] = int(crabs[i])

    minCrabSpot = min(crabs)
    maxCrabSpot = max(crabs)

    minGasCost = -1
    position = -1
    for spot in range(minCrabSpot, maxCrabSpot):
        gasCost = calcGasCost(crabs, spot)
        print(f"Result is {gasCost} at {spot}")
        if minGasCost == -1 or gasCost < minGasCost:
            minGasCost = gasCost
            position = spot

    result = minGasCost
    return f"Result is {result} at {position}"


print(day7("input.txt"))