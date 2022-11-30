def getFishBreedCadenceForWholeCycle(n):
    # on the 6th day it breeds another fish, but a new fish takes 9 days to do anything (8 + the current day because it only starts on the next day)
    seedBreedCadence = [0, 0, 0, 0, 0, 1, 0, 0, 0]
    countFishies = [1]  # zero iterations, count = 1
    for iteration in range(n):
        zerothsSpot = seedBreedCadence[0]
        seedBreedCadence = seedBreedCadence[1:]  # move start down 1
        seedBreedCadence.append(zerothsSpot)  # New fish needs to go the distance before breeding
        seedBreedCadence[6] += zerothsSpot  # Old fish needs to only go 6 spots
        countFishies.append(sum(seedBreedCadence)) # add it up
        
    return countFishies


# (DaysNeeded + 6 (regular breed cycle for an adult))
breedCadence = getFishBreedCadenceForWholeCycle(262)


def getChildrenCountForFish(age, daysLeft):
    return breedCadence[int(daysLeft) + int(5) - int(age)]
            

def day6Math(fileName: str, days):
    file = open(fileName, "r")
    allLines = file.read().splitlines()

    ages = allLines[0].split(",")
    totalFish = 0
    for age in ages:
        currCount = getChildrenCountForFish(age, days)
        totalFish += currCount

    return f"After {days} days there are: {totalFish}"


print(day6Math("input.txt", 256))