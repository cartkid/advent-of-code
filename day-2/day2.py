def pilot():
    directionForward = "forward"
    directionDown = "down"
    directionUp = "up"

    depth = 0
    horizontal = 0
    aim = 0

    file = open("input.txt", "r")
    allLines = file.readlines()
    for line in allLines:
        resultLine = line.split(" ")
        direction = resultLine[0]
        amount = int(resultLine[1])
        if direction == directionUp:
            # depth -= amount
            aim -= amount
        elif direction == directionDown:
            # depth += amount
            aim += amount
        elif direction == directionForward:
            horizontal += amount
            depth += (amount * aim)
    
    print(f"horizontal: {horizontal}\ndepth: {depth}")
    result = horizontal * depth
    print(f"result: {result}")
    return result

print(pilot())