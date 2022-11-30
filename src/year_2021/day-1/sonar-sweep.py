def calculateIncreases():
    file = open("input.txt", "r")
    allLines = file.readlines()
    sweepInput = []
    for line in allLines:
        depth = int(line)
        sweepInput.append(depth)

    lengthOfSweepInput = len(sweepInput)
    print(lengthOfSweepInput)

    threeValueSweep = []
    for i, depth in enumerate(sweepInput):
        if (i + 2) < (lengthOfSweepInput):
            threeSum = sweepInput[i] + sweepInput[i+1] + sweepInput[i+2]
            threeValueSweep.append(threeSum)

    print(len(threeValueSweep))
    previous = None
    countIncreases = 0
    for x in threeValueSweep:
        if previous == None:
            previous = x
            continue
        if previous < x:
            countIncreases += 1
        
        previous = x
    return countIncreases

print(calculateIncreases())