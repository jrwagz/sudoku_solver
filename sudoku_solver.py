from array import *
import copy
import math
import operator
import collections


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


def strForPuzzle (pzlData):
    rowCnt = 0
    colCnt = 0
    myStr = ""
    for r in pzlData:
        if rowCnt % 3 == 0 and rowCnt != 0:
            myStr = myStr + "---------------------\n"
        for c in r:
            colCnt = colCnt + 1
            if c == 0:
                p = " "
            else:
                p = c
            if colCnt % 3 == 0 and colCnt != 0 and colCnt != 9:
                myStr = myStr + str(p) + " | "
            else:
                myStr = myStr + str(p) + " "
        myStr = myStr + "\n"
        rowCnt = rowCnt + 1
        colCnt = 0

    return myStr

# This function is used to print out a Puzzle data structure so that it's easy to look at
# it takes the data structure as input, then prints it to std_out in a pretty format, like this:
#
#       | 7   4 | 8 9
# 1     |     8 |   6
# 9 8   | 1     | 3 7
# ---------------------
#   7   | 4 6 5 |
#       |       |
#       | 9 3 2 |   5
# ---------------------
#   3 8 |     7 |   4 9
#   4   | 2     |     3
#   9 1 | 5   3 |
def printPuzzle (pzlData):
    print(strForPuzzle(pzlData))

# This function takes a list as input, and then it determines if that list meets all the criteria for
# being a solved Sudoku list.  For example, a row is a list, a column is a list, and the elements of a 
# box also make a list.  Each of those classes simply put their data into a list format, then ask this
# function to tell them if it's solved or not
def isListSolved (pzlList):
    # Ensure all numbers are between 1 and 9
    for c in pzlList:
        if (c < 1) or (c > 9) :
            return False

    # Ensure there are no duplicates, and that there are exactly 9 items
    if not len(set(pzlList)) == 9:
        return False

    # If all numbers are between 1 and 9 (including 1 and 9), there are no duplicates,
    # and the count of all the numbers equals nine, then by definition we have the numbers
    # 1 through 9 exactly, and the list is solved
    return True


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
        # Our data is already a list, so send it to isListSolved directly
        return isListSolved(self.data[self.id])

    def count_of_number (self, number):
        return self.data[self.id].count(number)

    def contains_number (self, number):
        for r in self.data[self.id]:
            if r == number:
                return True

        return False

class SudokuColumn:
    def __init__ (self, id, data):
        self.id = id
        self.data = data

    def is_solved (self):
        list = []
        # Make a list that represents the column data, then send it to isListSolved
        for r in self.data:
            list.append(r[self.id])

        return isListSolved(list)

    def count_of_number (self, number):
        list = []
        # Make a list that represents the column data, then send it to isListSolved
        for r in self.data:
            list.append(r[self.id])

        return list.count(number)

    def contains_number (self, number):
        for r in self.data:
            if r[self.id] == number:
                return True

        return False


class SudokuBox:
    def __init__ (self, id, data):
        self.id = id
        self.data = data
        self.col_offset = (id % 3)*3
        self.row_offset = math.floor(id/3) * 3

    def __str__ (self):
        return "BOX: "+str(self.id)+" row_offset: "+str(self.row_offset)+" col_offset: "+str(self.col_offset)

    def is_solved (self):
        list = []
        # Make a list that represents the box data, then send it to isListSolved
        for r in self.data[self.row_offset:self.row_offset+3]:
            for c in r[self.col_offset:self.col_offset+3]:
                list.append(c)

        return isListSolved(list)

    def count_of_number (self, number):
        list = []
        # Make a list that represents the box data, then send it to isListSolved
        for r in self.data[self.row_offset:self.row_offset+3]:
            for c in r[self.col_offset:self.col_offset+3]:
                list.append(c)

        return list.count(number)
        
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
        
    def count_of_number (self, number):
        cnt = 0
        for r in self.rows:
            cnt = cnt + r.count_of_number(number)

        return cnt

    def counts_of_numbers (self):
        dict = {}
        # Figure out how many of each number exists in the puzzle
        for num in index_list:
            myNum = num + 1
            dict[myNum] = self.count_of_number(myNum)

        return dict

    def counts_of_numbers_sorted (self, reverse=True):
        return collections.OrderedDict(sorted(self.counts_of_numbers().items(), key=lambda kv: kv[1], reverse=reverse))

    def print_orig (self):
        printPuzzle(self.orig_data)

    def print_data (self):
        printPuzzle(self.data)

    def __str__ (self):
        myStr = "==================================================\n"
        myStr = myStr + strForPuzzle(self.data)
        for r in self.rows:
            if not r.is_solved():
                myStr = myStr + "Row "+str(r.id)+" is NOT SOLVED!\n"
        for c in self.columns:
            if not c.is_solved():
                myStr = myStr + "Col "+str(c.id)+" is NOT SOLVED!\n"
        for b in self.boxes:
            if not b.is_solved():
                myStr = myStr + "Box "+str(b.id)+" is NOT SOLVED!\n"

        myStr = myStr + "==================================================\n"

        cnts = self.counts_of_numbers_sorted()
        for num in cnts:
            myStr = myStr + str(num)+" is found "+str(cnts[num])+" times\n"


        myStr = myStr + "==================================================\n"

        if self.is_solved():
            myStr = myStr + "I'm SOLVED!\n"
        else:
            myStr = myStr + "I'm NOT SOLVED!\n"

        myStr = myStr + "==================================================\n"

        return myStr


print("Hello World, let's solve some Sudoku!")
myPzl = SudokuPuzzle(SudokuPZL1)

print("==PZL 1==================================")
print(myPzl)

# To see whether or not each box contains each number un-comment (remove the # at the beginning of the line) these lines and run
#for i in index_list:
#    for j in index_list:
#        print("Box "+str(j)+" Contains "+str(i+1)+"? "+str(myPzl.boxes[j].contains_number(i+1)))

myPzlSolved = SudokuPuzzle(SudokuPZL1Solution)
print("==PZL 1 SOLUTION========================")
print(myPzlSolved)

myPzlBadSolution = SudokuPuzzle(SudokuBADSOLUTION)
print("==PZL WITH BAD SOLUTION=================")
print(myPzlBadSolution)

