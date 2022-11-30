from dataclasses import dataclass
from typing import List


@dataclass
class bingoBoard:
    numbers = []
    boardSize: int = 5
    rows = []
    columns = []
    scoreWhenWon = -1


    def __init__(self, numbers):
        self.numbers = numbers
        self.rows = self.getRows()
        self.columns = self.getColumns()
        print("ROWS")
        for row in self.rows:
            print(row)
        print("COLUMNS")
        for col in self.columns:
            print(col)
        print("BOARD LOADED")


    def getRows(self) -> List[List[int]]:
        tempNumbers = self.numbers.copy()
        rows = []
        for i in range(0, self.boardSize):
            rows.append(tempNumbers[:self.boardSize])
            tempNumbers = tempNumbers[self.boardSize:]
        return rows


    def getColumns(self) -> List[List[int]]:
        columns = []
        for colIndex in range(0, self.boardSize):
            columns.append([])
        for colIndex in range(0, self.boardSize):
            for row in self.rows:
                if columns[colIndex] == []:
                    columns[colIndex]=[row[colIndex]]
                else:
                    columns[colIndex].append(row[colIndex])
        return columns


    def hasBingo(self, numbersPickedSoFar: List[int]) -> bool:
        hasBingo = False
        currBingo = []
        for r in self.rows:
            currBingo = []
            for c in r:
                if c in numbersPickedSoFar:
                    currBingo.append(c)
                    if len(currBingo) == self.boardSize:
                        hasBingo = True
                        print(f"BINGO: {currBingo}")
                        return hasBingo

        for c in self.columns:
            currBingo = []
            for r in c:
                if r in numbersPickedSoFar:
                    currBingo.append(r)
                    if len(currBingo) == self.boardSize:
                        hasBingo = True
                        print(f"BINGO: {currBingo}")
                        return hasBingo
        
        return hasBingo

    
    def getBoardScore(self, numbersPicked: List[int], winningNumberCalled: int) -> int:
        currSum = 0
        for boardNumber in self.numbers:
            if boardNumber not in numbersPicked:
                currSum += boardNumber
        
        print(f"unwinning total: {currSum}")
        print(f"winning number: {winningNumberCalled}")
        print(f"board score: {currSum * winningNumberCalled}")
        return currSum * winningNumberCalled


def day4Calc(fileName: str) -> int:
    result = 0

    boardSize = 5

    file = open(fileName, "r")
    allLines = file.read().splitlines()

    bingoBoards: List[bingoBoard] = []
    bingoWinningNumbersString = allLines.pop(0)
    print(bingoWinningNumbersString)
    bingoWinningNumbers = []
    print(allLines.pop(0)) # blank line

    # load all boards into bingoBoards
    currBoard = []
    while len(allLines) > 0:
        for row in range(0, boardSize):
            rowString = allLines.pop(0)
            rowString = rowString.replace("  ", " ")
            numList = rowString.split(" ")
            for num in numList:
                if num == "":
                    continue
                currBoard.append(int(num))

        print(currBoard)
        bingoBoards.append(bingoBoard(currBoard))
        currBoard = []
        if len(allLines) > 0:
            allLines.pop(0) # blank line

    lastBoardToWin: bingoBoard = None
    for winningNumber in bingoWinningNumbersString.split(","):
        currWinningNumber = int(winningNumber)
        bingoWinningNumbers.append(currWinningNumber)
        if len(bingoWinningNumbers) < boardSize:
            continue
        else:
            for board in bingoBoards:
                if board.scoreWhenWon == -1:
                    hasBingo = board.hasBingo(bingoWinningNumbers)
                    if hasBingo is True:
                        result = board.getBoardScore(bingoWinningNumbers, currWinningNumber)
                        print(f"num: {currWinningNumber} | {board.rows[0]} | {result}")
                        board.scoreWhenWon = result
                        lastBoardToWin = board

    return lastBoardToWin.scoreWhenWon

result = day4Calc(fileName="input.txt")
print(result)