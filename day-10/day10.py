import math
from dataclasses import dataclass
from typing import List


@dataclass
class coordinates:
    r: int = -1
    c: int = -1
    fromDirection: str = "A"

spotsChecked: List[coordinates] = []


def getCorruptionPoints(line: str) -> int:
    result = 0

    pointsPerChar = { ")": 3, 
                      "]": 57,
                      "}": 1197,
                      ">": 25137}

    pointsForCompletion = { ")": 1, 
                            "]": 2,
                            "}": 3,
                            ">": 4}

    
    matchingChar = { "(": ")",
                     "[": "]",
                     "{": "}",
                     "<": ">" }

    lookingFor: List[str] = []

    for i in range(0, len(line)):
        currChar = line[i]
        if currChar in matchingChar.keys():
            lookingFor.append(matchingChar[currChar])
        else:
            if len(lookingFor) > 0 and currChar == lookingFor[len(lookingFor)-1]:
                lookingFor.pop()
            else:
                return 0
                result = pointsPerChar[currChar]
                return result

    if len(lookingFor) > 0:
        # incomplete
        while len(lookingFor) > 0:
            result = result * 5
            poppedVal = lookingFor.pop()
            result = result + pointsForCompletion[poppedVal]
        result = result

    return result


def day10(fileName: str):
    file = open(fileName, "r")
    allLines = file.read().splitlines()

    pointsOfCorruption = 0
    pointsOfIncompletion = []
    for line in allLines:
        val = getCorruptionPoints(line)
        if val != 0:
            pointsOfIncompletion.append(val)
    
    pointsOfIncompletion.sort()
    midSpot = math.floor((len(pointsOfIncompletion) - 1)/2)
    print(pointsOfIncompletion)
    print(midSpot)
    result = pointsOfIncompletion[midSpot]

    return f"Result is {result}"


print(day10("input.txt"))