from typing import List
from dataclasses import dataclass


@dataclass
class coordinate:
    x: int = -1
    y: int = -1


    def __init__(self, coordString: str):
        coords = coordString.split(",")
        self.x = int(coords[0])
        self.y = int(coords[1])

    def printCoordinate(self, prefix):
        print(f"{prefix}: {self.x},{self.y}")


@dataclass
class lineSegment:
    coord1: coordinate
    coord2: coordinate


    def __init__(self, coordsString: str):
        coords = coordsString.split(" -> ")
        self.coord1 = coordinate(coords[0])
        self.coord2 = coordinate(coords[1])


    def printLine(self):
        print(f"\nLine: {self.coord1.x},{self.coord1.y} -> {self.coord2.x},{self.coord2.y}")


    def isStraightAlongX(self):
        if self.coord1.y == self.coord2.y:
            return True
        return False


    def isStraightAlongY(self):
        if self.coord1.x == self.coord2.x:
            return True
        return False


    def getFurthestNeededCoordinate(self):
        biggestX = self.coord1.x
        if self.coord2.x > biggestX:
            biggestX = self.coord2.x
        
        biggestY = self.coord1.y
        if self.coord2.y > biggestY:
            biggestY = self.coord2.y
        
        biggestCoordinate = coordinate(f"{biggestX},{biggestY}")        
        biggestCoordinate.printCoordinate("FURTHEST COORD")
        return biggestCoordinate


@dataclass
class diagram:
    diagramArrays = [] #rows of columns (row = y, column = x)


    def printDiagram(self):
        print("\nDIAGRAM")
        for row in self.diagramArrays:
            rowStr = ""
            for col in row:
                if col == 0:
                    rowStr += "."
                else:
                    rowStr += f"{col}"
            print(rowStr)


    def ensureBigEnough(self, line: lineSegment):
        furthestNeededCoordinate = line.getFurthestNeededCoordinate()

        rowCount = len(self.diagramArrays)
        if rowCount <= furthestNeededCoordinate.y:
            for addRow in range(rowCount, furthestNeededCoordinate.y + 1):
                self.diagramArrays.append([])

        for rowIndex, row in enumerate(self.diagramArrays):
            columnsInRow = len(row)
            if columnsInRow <= furthestNeededCoordinate.x:
                for addColumn in range(columnsInRow, furthestNeededCoordinate.x + 1):
                    self.diagramArrays[rowIndex].append(0)
        
        print(f"rows: {len(self.diagramArrays)}")
        print(f"columns: {len(self.diagramArrays[0])}")


    def addLine(self, line: lineSegment):
        self.ensureBigEnough(line)

        line.printLine()
        if line.isStraightAlongX() is True:
            print("ROW")
            biggerX = line.coord2.x if line.coord2.x > line.coord1.x else line.coord1.x
            smallerX = line.coord1.x if line.coord1.x < line.coord2.x else line.coord2.x

            for i in range(smallerX, biggerX + 1):
                self.diagramArrays[line.coord1.y][i] += 1
                
        elif line.isStraightAlongY() is True:
            print("COLUMN")
            biggerY = line.coord2.y if line.coord2.y > line.coord1.y else line.coord1.y
            smallerY = line.coord1.y if line.coord1.y < line.coord2.y else line.coord2.y

            for i in range(smallerY, biggerY + 1):
                self.diagramArrays[i][line.coord1.x] += 1
            
        else:
            print("DIAGONAL?")
            biggerY = line.coord2.y if line.coord2.y > line.coord1.y else line.coord1.y
            smallerY = line.coord1.y if line.coord1.y < line.coord2.y else line.coord2.y

            xIsIncreasing = True
            if biggerY == line.coord2.y:
                xIsIncreasing = True if line.coord1.x < line.coord2.x else False
                currX = line.coord1.x
            elif biggerY == line.coord1.y:
                xIsIncreasing = True if line.coord1.x > line.coord2.x else False
                currX = line.coord2.x


            xDiff = abs(line.coord1.x - line.coord2.x)
            yDiff = abs(line.coord1.y - line.coord2.y)
            if xDiff == yDiff: # 45 degree angles only
                for yChange in range(smallerY, biggerY + 1):
                    self.diagramArrays[yChange][currX] += 1
                    currX = currX + 1 if xIsIncreasing else currX - 1
                        
        # self.printDiagram()

    
    def getNumberOfPointsToAvoid(self):
        count = 0
        for row in self.diagramArrays:
            for col in row:
                if col >= 2:
                    count += 1
        return count



def day5(fileName: str):
    result = 0

    file = open(fileName, "r")
    allLines = file.read().splitlines()

    currDiagram: diagram = None
    

    for line in allLines:
        currLine = lineSegment(line)
        if currDiagram == None:
            currDiagram = diagram()
        
        currDiagram.addLine(currLine)

    result = currDiagram.getNumberOfPointsToAvoid()
    print(f"Points to avoid: {result}")
    return result

print(day5("input.txt"))