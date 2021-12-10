from typing import List


def binaryDiagnostic():
    powerConsumption = 0
    gammaRate = 0
    epsilonRate = 0
    lifeSupportRating = 0
    oxygenGeneratorRating = 0
    co2ScrubberRating = 0

    file = open("input.txt", "r")
    allLines = file.read().splitlines() 
    result = ""
    for i, val in enumerate(allLines[0]):
        result += getMaxOccurringCharInPosition(allLines, i)
    
    # for oxygen
    remainingLines = allLines.copy()
    for i, val in enumerate(allLines[0]):
        lookFor = getMaxOccurringCharInPosition(remainingLines, i)
        remainingLines = filterLines(remainingLines, lookFor, i)
    oxygenGeneratorRatingBinary = remainingLines[0]
    print(f"oxygenGeneratorRatingBinary: {oxygenGeneratorRatingBinary}")
    oxygenGeneratorRating = binaryToDecimal(int(oxygenGeneratorRatingBinary))
    print(f"oxygenGeneratorRating: {oxygenGeneratorRating}")
        
    # for scrubber
    remainingLines = allLines.copy()
    for i, val in enumerate(allLines[0]):
        lookFor = getMinOccurringCharInPosition(remainingLines, i)
        remainingLines = filterLines(remainingLines, lookFor, i)
    co2ScrubberRatingBinary = remainingLines[0]
    print(f"co2ScrubberRatingBinary: {co2ScrubberRatingBinary}")
    co2ScrubberRating = binaryToDecimal(int(co2ScrubberRatingBinary))
    print(f"co2ScrubberRating: {co2ScrubberRating}")

    lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating
    print(f"lifeSupportRating: {lifeSupportRating}")
    return lifeSupportRating

    # gammaRate = binaryToDecimal(int(result))
    # print(f"gammaRate: {gammaRate}")
    # epsilonRateStr = flipResult(result)
    # epsilonRate = binaryToDecimal(int(epsilonRateStr))
    # print(f"epsilonRate: {epsilonRate}")
    # powerConsumption = gammaRate * epsilonRate
    # print(f"powerConsumption: {powerConsumption}")
    # return powerConsumption

def getMaxOccurringCharInPosition(lines, position) -> any:
    result = ""
    totalLines = len(lines)
    currTotal = 0
    for line in lines:
        currTotal += int(line[position])
    result = "1" if currTotal >= (totalLines/2) else "0"
    return result


def getMinOccurringCharInPosition(lines, position) -> any:
    zeroCount = len([1 for line in lines if line[position] == "0"])
    oneCount = len([1 for line in lines if line[position] == "1"])
    if zeroCount == 0:
        result = "1"
    elif oneCount == 0:
        result = "0"
    else:
        result = "0" if zeroCount <= oneCount else "1"
    return result


def filterLines(lines, lookFor, position) -> List:
    result = []
    for line in lines:
        if line[position] == lookFor:
            result.append(line)
    return result


def flipResult(binary) -> any:
    result = ""
    for curr in binary:
        if curr == "1":
            result += "0"
        else:
            result += "1"
    return result

def binaryToDecimal(binary) -> any:
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

print(binaryDiagnostic())
