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

SudokuPZL9 = [[0, 7, 0, 0, 0, 0, 4, 0, 0],
              [5, 1, 8, 0, 0, 4, 0, 0, 0],
              [0, 3, 0, 1, 0, 0, 0, 5, 0],
              [0, 0, 9, 8, 5, 0, 0, 1, 7],
              [0, 0, 7, 3, 0, 9, 5, 0, 0],
              [3, 5, 0, 0, 7, 1, 9, 0, 0],
              [0, 2, 0, 0, 0, 7, 0, 3, 0],
              [0, 0, 0, 5, 0, 0, 1, 7, 9],
              [0, 0, 1, 0, 0, 0, 0, 2, 0]]


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

index_list = (0, 1, 2, 3, 4, 5, 6, 7, 8)


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
    def __init__ (self, id, column_index, row_index, puzzle):
        self.id = id
        self.column_index = column_index
        self.row_index = row_index
        self.puzzle = puzzle


class SudokuRow:
    def __init__ (self, id, data, puzzle):
        self.id = id
        self.data = data
        self.puzzle = puzzle

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
    def __init__ (self, id, data, puzzle):
        self.id = id
        self.data = data
        self.puzzle = puzzle

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
    def __init__ (self, id, data, puzzle):
        self.id = id
        self.data = data
        self.col_offset = (id % 3)*3
        self.row_offset = math.floor(id/3) * 3
        self.puzzle = puzzle

    def __str__ (self):
        myStr = "BOX: "+str(self.id)+" row_offset: "+str(self.row_offset)+" col_offset: "+str(self.col_offset)+"\n"
        row_offset = 0
        myStr = myStr + "    row["+str(row_offset)+"] has "+str(len(self.indices_of_blanks_in_row(row_offset)))+" blanks in it\n"
        row_offset = 1
        myStr = myStr + "    row["+str(row_offset)+"] has "+str(len(self.indices_of_blanks_in_row(row_offset)))+" blanks in it\n"
        row_offset = 2
        myStr = myStr + "    row["+str(row_offset)+"] has "+str(len(self.indices_of_blanks_in_row(row_offset)))+" blanks in it\n"
        col_offset = 0
        myStr = myStr + "    col["+str(col_offset)+"] has "+str(len(self.indices_of_blanks_in_column(col_offset)))+" blanks in it\n"
        col_offset = 1
        myStr = myStr + "    col["+str(col_offset)+"] has "+str(len(self.indices_of_blanks_in_column(col_offset)))+" blanks in it\n"
        col_offset = 2
        myStr = myStr + "    col["+str(col_offset)+"] has "+str(len(self.indices_of_blanks_in_column(col_offset)))+" blanks in it\n"

        return myStr

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

    def rows (self):
        my_rows = []
        my_rows.append(self.puzzle.rows[self.row_offset+0])
        my_rows.append(self.puzzle.rows[self.row_offset+1])
        my_rows.append(self.puzzle.rows[self.row_offset+2])
        return my_rows

    def columns (self):
        my_cols = []
        my_cols.append(self.puzzle.columns[self.col_offset+0])
        my_cols.append(self.puzzle.columns[self.col_offset+1])
        my_cols.append(self.puzzle.columns[self.col_offset+2])
        return my_cols

    def indices_of_blanks_in_row (self, row_index):
        blank_indices = []
        if self.data[self.row_offset+row_index][self.col_offset+0] == 0:
            blank_indices.append(0)
        if self.data[self.row_offset+row_index][self.col_offset+1] == 0:
            blank_indices.append(1)
        if self.data[self.row_offset+row_index][self.col_offset+2] == 0:
            blank_indices.append(2)
        
        return blank_indices

    def indices_of_blanks_in_column (self, column_index):
        blank_indices = []
        if self.data[self.row_offset+0][self.col_offset+column_index] == 0:
            blank_indices.append(0)
        if self.data[self.row_offset+1][self.col_offset+column_index] == 0:
            blank_indices.append(1)
        if self.data[self.row_offset+2][self.col_offset+column_index] == 0:
            blank_indices.append(2)
        
        return blank_indices


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
            self.rows.append(SudokuRow(i, self.data, self))
            self.columns.append(SudokuColumn(i, self.data, self))
            self.boxes.append(SudokuBox(i, self.data, self))
            for j in index_list:
                self.squares.append(SudokuSquare(i*j,i,j,self))

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

    # Go through a sorted list of number with the highest count
    #   ask each box if it doesn't have that number, if so proceed
    #       go through each row in that box and ask if it doesn't have that number, if so proceed
    #           look at the 3 squares in our box for this row, and see if there are blanks, if so proceed
    #               for each of the blanks, see if their column already contains the number, if not remember that column index
    #                   remember all of the row/col indices that are possible solutions in this box
    #       If the list of possible solutions is 1, then fill in that location
    #               
    def solving_tactic_1 (self,debug=False):
        print("...performing solving tactic 1")
        cnts = self.counts_of_numbers_sorted();
        solved_squares = 0
        for num in cnts:
            for b in self.boxes:
                if not b.contains_number(num):
                    if debug: print("Box "+str(b.id)+" doesn't contain "+str(num))
                    poss_solution_spots = []
                    for r in b.rows():
                        if not r.contains_number(num):
                            if debug: print("  Row "+str(r.id)+" doesn't contain "+str(num))
                            for c_idx in b.indices_of_blanks_in_row(r.id-b.row_offset):
                                if debug: print("    Col offset "+str(c_idx)+" is blank")
                                if not b.columns()[c_idx].contains_number(num):
                                    if debug: print("      Col offset "+str(c_idx)+" doesn't contain "+str(num))
                                    poss_solution_spots.append((r.id,b.col_offset+c_idx))

                    if len(poss_solution_spots) == 1:
                        print("    WE FOUND A SOLUTION! Box: "+str(b.id)+" Row: "+str(poss_solution_spots[0][0])+" Col: "+str(poss_solution_spots[0][1])+" = "+str(num))
                        self.data[poss_solution_spots[0][0]][poss_solution_spots[0][1]] = num
                        solved_squares = solved_squares + 1
                        if debug: return solved_squares
                    else:
                        if debug: print("    NO SOLUTION in this box, there are "+str(len(poss_solution_spots))+" possibilities "+str(poss_solution_spots))

        return solved_squares

    def attempt_to_solve (self):
        print("Attempting to solve the puzzle!")
        #self.solving_tactic_1(True)
        solved_squares = 1
        while solved_squares > 0:
            solved_squares = self.solving_tactic_1()

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

myPzl.attempt_to_solve()

print("==PZL 1 attempted solution===============")

print(myPzl)


myPzl9 = SudokuPuzzle(SudokuPZL9)
print("==PZL 9==================================")
print(myPzl9)

myPzl9.attempt_to_solve()

print("==PZL 9 attempted solution===============")

print(myPzl9)



# To see whether or not each box contains each number un-comment (remove the # at the beginning of the line) these lines and run
#for i in index_list:
#    for j in index_list:
#        print("Box "+str(j)+" Contains "+str(i+1)+"? "+str(myPzl.boxes[j].contains_number(i+1)))
#
#myPzlSolved = SudokuPuzzle(SudokuPZL1Solution)
#print("==PZL 1 SOLUTION========================")
#print(myPzlSolved)
#
#myPzlBadSolution = SudokuPuzzle(SudokuBADSOLUTION)
#print("==PZL WITH BAD SOLUTION=================")
#print(myPzlBadSolution)

