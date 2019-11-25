from array import *
import copy


SudokuPZL1 = [[0, 0, 0, 7, 0, 4, 8, 9, 0],
              [1, 0, 0, 0, 0, 8, 0, 6, 0],
              [9, 8, 0, 1, 0, 0, 3, 7, 0],
              [0, 7, 0, 4, 6, 5, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 9, 3, 2, 0, 5, 0],
              [0, 3, 8, 0, 0, 7, 0, 4, 9],
              [0, 4, 0, 2, 0, 0, 0, 0, 3],
              [0, 9, 1, 5, 0, 3, 0, 0, 0]]

class SudokuSquare:
    def __init__ (self, id):
        self.id = id


class SudokuRow:
    def __init__ (self, id):
        self.id = id


class SudokuColumn:
    def __init__ (self, id):
        self.id = id


class SudokuBox:
    def __init__ (self, id):
        self.id = id

def printPuzzle (pzlData):
    rowCnt = 0
    colCnt = 0
    for r in pzlData:
        if rowCnt % 3 == 0 and rowCnt != 0:
            print("---------------------")
        for c in r:
            colCnt = colCnt + 1
            if colCnt % 3 == 0 and colCnt != 0 and colCnt != 9:
                print(c,end = " | ")
            else:
                print(c,end = " ")
        print()
        rowCnt = rowCnt + 1
        colCnt = 0


print("Hello World, let's solve some Sudoku!")
SudokuData = copy.deepcopy(SudokuPZL1)

print("=PZL1===================================")
printPuzzle(SudokuPZL1)

print("=DATA===================================")
printPuzzle(SudokuData)


print("====================================")
print("Changing SudokuData")
SudokuData[0][2] = 3
SudokuData[0][0] = 5

print("=PZL1===================================")
printPuzzle(SudokuPZL1)

print("=DATA===================================")
printPuzzle(SudokuData)

