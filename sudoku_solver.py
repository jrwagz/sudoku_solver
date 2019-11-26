from array import *
import copy
import math


SudokuPZL1 = [[0, 0, 0, 7, 0, 4, 8, 9, 0],
              [1, 0, 0, 0, 0, 8, 0, 6, 0],
              [9, 8, 0, 1, 0, 0, 3, 7, 0],
              [0, 7, 0, 4, 6, 5, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 9, 3, 2, 0, 5, 0],
              [0, 3, 8, 0, 0, 7, 0, 4, 9],
              [0, 4, 0, 2, 0, 0, 0, 0, 3],
              [0, 9, 1, 5, 0, 3, 0, 0, 0]]


SudokuPZL1Solution = [[5, 6, 3, 7, 2, 4, 8, 9, 1],
                      [1, 2, 7, 3, 9, 8, 4, 6, 5],
                      [9, 8, 4, 1, 5, 6, 3, 7, 2],
                      [3, 7, 9, 4, 6, 5, 1, 2, 8],
                      [4, 5, 2, 8, 7, 1, 9, 3, 6],
                      [8, 1, 6, 9, 3, 2, 7, 5, 4],
                      [2, 3, 8, 6, 1, 7, 5, 4, 9],
                      [7, 4, 5, 2, 8, 9, 6, 1, 3],
                      [6, 9, 1, 5, 4, 3, 2, 8, 7]]


SudokuBADSOLUTION = [[5, 6, 3, 7, 2, 4, 8, 9, 1],
                     [1, 2, 7, 3, 9, 8, 4, 6, 5],
                     [9, 6, 4, 1, 5, 6, 3, 7, 2],  # <--- the second column on this row shouldn't be a 6, it should be an 8!
                     [3, 7, 9, 4, 6, 5, 1, 2, 8],
                     [4, 5, 2, 8, 7, 1, 9, 3, 6],
                     [8, 1, 6, 9, 3, 2, 7, 5, 4],
                     [2, 3, 8, 6, 1, 7, 5, 4, 9],
                     [7, 4, 5, 2, 8, 9, 6, 1, 3],
                     [6, 9, 1, 5, 4, 3, 2, 8, 7]]

index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def printPuzzle (pzlData):
    rowCnt = 0
    colCnt = 0
    for r in pzlData:
        if rowCnt % 3 == 0 and rowCnt != 0:
            print("---------------------")
        for c in r:
            colCnt = colCnt + 1
            if c == 0:
                p = " "
            else:
                p = c
            if colCnt % 3 == 0 and colCnt != 0 and colCnt != 9:
                print(p,end = " | ")
            else:
                print(p,end = " ")
        print()
        rowCnt = rowCnt + 1
        colCnt = 0

class SudokuSquare:
    def __init__ (self, id, column_index, row_index):
        self.id = id
        self.column_index = column_index
        self.row_index = row_index


class SudokuRow:
    def __init__ (self, id, data):
        self.id = id
        self.data = data

    def is_solved (self):
        for c in self.data[self.id]:
            if c == 0:
                return False

        return True

class SudokuColumn:
    def __init__ (self, id, data):
        self.id = id
        self.data = data

    def is_solved (self):
        solved = True
        for r in self.data:
            if r[self.id] == 0:
                solved = False
                break

        return solved


class SudokuBox:
    def __init__ (self, id, data):
        self.id = id
        self.data = data
        self.col_offset = (id % 3)*3
        self.row_offset = math.floor(id/3) * 3

    def __str__ (self):
        return "BOX: "+str(self.id)+" row_offset: "+str(self.row_offset)+" col_offset: "+str(self.col_offset)

    def is_solved (self):
        for r in self.data[self.row_offset:self.row_offset+3]:
            for c in r[self.col_offset:self.col_offset+3]:
                if c == 0:
                    return False

        return True
        
    def contains_number (self, number):
        for r in self.data[self.row_offset:self.row_offset+3]:
            for c in r[self.col_offset:self.col_offset+3]:
                if c == number:
                    return True

        return False



class SudokuPuzzle:
    def __init__ (self, puzzleData):
        self.data = copy.deepcopy(puzzleData)
        self.orig_data = copy.deepcopy(puzzleData)
        self.rows = []
        self.columns = []
        self.boxes = []
        self.squares = []

        rowCnt = len(self.data)
        colCnt = len(self.data[0])
        if not rowCnt == len(index_list):
            print("ERROR! received data doesn't have enough rows!")
        if not colCnt == len(index_list):
            print("ERROR! received data doesn't have enough columns!")

        for i in index_list:
            self.rows.append(SudokuRow(i, self.data))
            self.columns.append(SudokuColumn(i, self.data))
            self.boxes.append(SudokuBox(i, self.data))
            for j in index_list:
                self.squares.append(SudokuSquare(i*j,i,j))

    def is_solved (self):
        for r in self.rows:
            if not r.is_solved():
                return False

        for c in self.columns:
            if not c.is_solved():
                return False

        for b in self.boxes:
            if not b.is_solved():
                return False

        return True

    def print_orig (self):
        printPuzzle(self.orig_data)

    def print_data (self):
        printPuzzle(self.data)

    def __str__ (self):
        return "Boxes   : "+str(len(self.boxes)) + "\n" + \
               "Rows    : "+str(len(self.rows)) + "\n" + \
               "Columns : "+str(len(self.columns)) + "\n" + \
               "Squares : "+str(len(self.squares))


print("Hello World, let's solve some Sudoku!")
myPzl = SudokuPuzzle(SudokuPZL1)

print("==PZL 1==================================")
myPzl.print_data()

# To see whether or not each box contains each number un-comment (remove the # at the beginning of the line) these lines and run
#for i in index_list:
#    for j in index_list:
#        print("Box "+str(j)+" Contains "+str(i+1)+"? "+str(myPzl.boxes[j].contains_number(i+1)))


if myPzl.is_solved():
    print("WE SOLVED IT!!!!")
else:
    print("NOT SOLVED!!!")


myPzlSolved = SudokuPuzzle(SudokuPZL1Solution)
print("==PZL 1 SOLUTION========================")
myPzlSolved.print_data()
if myPzlSolved.is_solved():
    print("WE SOLVED IT!!!!")
else:
    print("NOT SOLVED!!!")

myPzlBadSolution = SudokuPuzzle(SudokuBADSOLUTION)
print("==PZL WITH BAD SOLUTION=================")
myPzlBadSolution.print_data()
if myPzlBadSolution.is_solved():
    print("OOPS!!!! This puzzle isn't solved, but we think it is!!! Time to fix that")
else:
    print("NOT SOLVED!!!")

