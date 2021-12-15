
from collections import OrderedDict 


def getEasySegment(entry:str) -> int:
    one = 2
    four = 4
    seven = 3
    eight = 7

    segments = entry.split(" ")
    for segment in segments:
        if len(segment) == one:
            return 1
        elif len(segment) == four:
            return 4
        elif len(segment) == seven:
            return 7
        elif len(segment) == eight:
            return 8
    return -1


def displayContainsNumber(display, sipher):
    for i in range(0, len(sipher)):
        if sipher[i] not in display:
            return False
    return True


def getFilledSegmentsBySipherPlusSipherLessDupes(sipher1, sipher2):
    return len("".join(OrderedDict.fromkeys(sipher1 + sipher2)))


def getKey(entry:str):
    segments = entry.split(" ")
    key = { 0: "", 
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: ""}

    for segment in segments:
        result = getEasySegment(segment)
        if result > -1:
            key[result] = segment
        
    for segment in segments:
        if segment in key.values():
            continue
        segmentLength = len(segment)

        # test for 3 (5 and has ONE)
        if segmentLength == 5 and displayContainsNumber(segment, key[1]):
            key[3] = segment
    
        # test for 9  (6 and has FOUR)
        if segmentLength == 6 and displayContainsNumber(segment, key[4]):
            key[9] = segment

    for segment in segments:
        if segment in key.values():
            continue
        segmentLength = len(segment)

        # test for 5 (SELF + NINE (LESS DUPES) = 6)
        if segmentLength == 5 and getFilledSegmentsBySipherPlusSipherLessDupes(segment, key[9]) == 6:
            key[5] = segment

        # test for 2 (SELF + NINE (LESS DUPES) = 7)
        if segmentLength == 5 and getFilledSegmentsBySipherPlusSipherLessDupes(segment, key[9]) == 7:
            key[2] = segment

        # test for 0 (6 and has ONE)
        if segmentLength == 6 and displayContainsNumber(segment, key[1]):
            key[0] = segment

    for segment in segments:
        if segment in key.values() or segment == "":
            continue
        key[6] = segment
    # print(key)
    return key


def isMatch(sipher: str, testVal: str):
    if len(sipher) != len(testVal):
        return False
    if sipher == testVal:
        return True
    for i in range(0, len(sipher)):
        if sipher[i] not in testVal:
            return False
    return True


def getValue(key, entry):
    segments = entry.split(" ")
    returnStr = ""
    for segment in segments:
        valToAdd = ""
        if isMatch(key[0], segment):
            valToAdd = "0"
        elif isMatch(key[1], segment):
            valToAdd = "1"
        elif isMatch(key[2], segment):
            valToAdd = "2"
        elif isMatch(key[3], segment):
            valToAdd = "3"
        elif isMatch(key[4], segment):
            valToAdd = "4"
        elif isMatch(key[5], segment):
            valToAdd = "5"
        elif isMatch(key[6], segment):
            valToAdd = "6"
        elif isMatch(key[7], segment):
            valToAdd = "7"
        elif isMatch(key[8], segment):
            valToAdd = "8"
        elif isMatch(key[9], segment):
            valToAdd = "9"
        returnStr = returnStr + valToAdd
    return returnStr


def day8(fileName: str):
    file = open(fileName, "r")
    allLines = file.read().splitlines()

    count = 0
    for line in allLines:
        segments = line.split("|")
        key = getKey(segments[0])
        currValue = int(getValue(key, segments[1]))
        print(f"{segments[1]}: {currValue}")
        count += currValue

    return f"Result is {count}"


print(day8("input.txt"))