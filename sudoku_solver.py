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

class SudokuSquare:
    def __init__ (self, id):
        self.id = id


class SudokuRow:
    def __init__ (self, id, data):
        self.id = id
        self.puzzleData = data

    def is_solved (self):
        solved = True
        for c in self.puzzleData[self.id]:
            if c == 0:
                solved = False
                break

        return solved

class SudokuColumn:
    def __init__ (self, id, data):
        self.id = id
        self.puzzleData = data

    def is_solved (self):
        solved = True
        for r in self.puzzleData:
            if r[self.id] == 0:
                solved = False
                break

        return solved


class SudokuBox:
    def __init__ (self, id, data):
        self.id = id
        self.puzzleData = data


class SudokuPuzzle:
    rows = []
    columns = []
    boxes = []
    data = [[]]
    orig_data = [[]]
    def __init__ (self, puzzleData):
        rowCnt = 0
        colCnt = 0
        self.data = copy.deepcopy(puzzleData)
        self.orig_data = copy.deepcopy(puzzleData)
        for r in self.data:
            self.rows.append(SudokuRow(rowCnt, self.data))
            self.boxes.append(SudokuBox(rowCnt, self.data))
            for c in r:
                self.columns.append(SudokuColumn(colCnt, self.data))
                colCnt = colCnt + 1
            rowCnt = rowCnt + 1
            colCnt = 0

    def is_solved (self):
        solved = True

        if solved:
            for r in self.rows:
                if not r.is_solved():
                    solved = False
                    break

        if solved:
            for c in self.columns:
                if not c.is_solved():
                    solved = False
                    break

        if solved:
            for b in self.boxes:
                if not b.is_solved():
                    solved = False
                    break

        return solved

    def print_orig (self):
        printPuzzle(self.orig_data)

    def print_data (self):
        printPuzzle(self.data)


print("Hello World, let's solve some Sudoku!")
myPzl = SudokuPuzzle(SudokuPZL1)

print("=PZL1===================================")
myPzl.print_orig()

print("=DATA===================================")
myPzl.print_data()


print("====================================")
print("Changing SudokuData")
myPzl.data[0][2] = 3
myPzl.data[0][0] = 5

print("=PZL1===================================")
myPzl.print_orig()

print("=DATA===================================")
myPzl.print_data()

if myPzl.is_solved():
    print("WE SOLVED IT!!!!")
else:
    print("NOT SOLVED!!!")
