Welcome to the simple sudoku_solver!

This is a very basic application, and currently doesn't solve any Sudoku at all... lol. But it should get closer as we improve it.

Currently if you run the program you should see this:


    $ python sudoku_solver.py
    Hello World, let's solve some Sudoku!
    ==PZL 1==================================
    ==================================================
          | 7   4 | 8 9
    1     |     8 |   6
    9 8   | 1     | 3 7
    ---------------------
      7   | 4 6 5 |
          |       |
          | 9 3 2 |   5
    ---------------------
      3 8 |     7 |   4 9
      4   | 2     |     3
      9 1 | 5   3 |
    Row 0 is NOT SOLVED!
    Row 1 is NOT SOLVED!
    Row 2 is NOT SOLVED!
    Row 3 is NOT SOLVED!
    Row 4 is NOT SOLVED!
    Row 5 is NOT SOLVED!
    Row 6 is NOT SOLVED!
    Row 7 is NOT SOLVED!
    Row 8 is NOT SOLVED!
    Col 0 is NOT SOLVED!
    Col 1 is NOT SOLVED!
    Col 2 is NOT SOLVED!
    Col 3 is NOT SOLVED!
    Col 4 is NOT SOLVED!
    Col 5 is NOT SOLVED!
    Col 6 is NOT SOLVED!
    Col 7 is NOT SOLVED!
    Col 8 is NOT SOLVED!
    Box 0 is NOT SOLVED!
    Box 1 is NOT SOLVED!
    Box 2 is NOT SOLVED!
    Box 3 is NOT SOLVED!
    Box 4 is NOT SOLVED!
    Box 5 is NOT SOLVED!
    Box 6 is NOT SOLVED!
    Box 7 is NOT SOLVED!
    Box 8 is NOT SOLVED!
    ==================================================
    3 is found 5 times
    9 is found 5 times
    4 is found 4 times
    7 is found 4 times
    8 is found 4 times
    1 is found 3 times
    5 is found 3 times
    2 is found 2 times
    6 is found 2 times
    ==================================================
    I'm NOT SOLVED!
    ==================================================
    
    Attempting to solve the puzzle!
      Round 1
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 1 Row: 1 Col: 3 = 3
        WE FOUND A SOLUTION! Box: 1 Row: 1 Col: 4 = 9
        WE FOUND A SOLUTION! Box: 7 Row: 7 Col: 5 = 9
        WE FOUND A SOLUTION! Box: 7 Row: 8 Col: 4 = 4
        WE FOUND A SOLUTION! Box: 0 Row: 1 Col: 2 = 7
        WE FOUND A SOLUTION! Box: 4 Row: 4 Col: 4 = 7
        WE FOUND A SOLUTION! Box: 4 Row: 4 Col: 3 = 8
        WE FOUND A SOLUTION! Box: 7 Row: 7 Col: 4 = 8
        WE FOUND A SOLUTION! Box: 2 Row: 0 Col: 8 = 1
        WE FOUND A SOLUTION! Box: 4 Row: 4 Col: 5 = 1
        WE FOUND A SOLUTION! Box: 7 Row: 6 Col: 4 = 1
        WE FOUND A SOLUTION! Box: 1 Row: 2 Col: 5 = 6
        WE FOUND A SOLUTION! Box: 7 Row: 6 Col: 3 = 6
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 3 Row: 5 Col: 1 = 1
        WE FOUND A SOLUTION! Box: 0 Row: 2 Col: 2 = 4
    ...performing solving tactic 1
        Tactic 1 Solved 15 squares
    ...performing solving tactic 2
          WE FOUND A SOLUTION! SQUARE: 47 row_index: 5 column_index: 2 value: 6
          WE FOUND A SOLUTION! SQUARE: 65 row_index: 7 column_index: 2 value: 5
          WE FOUND A SOLUTION! SQUARE: 70 row_index: 7 column_index: 7 value: 1
    ...performing solving tactic 2
          WE FOUND A SOLUTION! SQUARE: 54 row_index: 6 column_index: 0 value: 2
          WE FOUND A SOLUTION! SQUARE: 60 row_index: 6 column_index: 6 value: 5
    ...performing solving tactic 2
        Tactic 2 Solved 5 squares
      Round 2
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 5 Row: 3 Col: 6 = 1
        WE FOUND A SOLUTION! Box: 5 Row: 4 Col: 6 = 9
        WE FOUND A SOLUTION! Box: 5 Row: 4 Col: 8 = 6
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 3 Row: 3 Col: 2 = 9
    ...performing solving tactic 1
        Tactic 1 Solved 4 squares
    ...performing solving tactic 2
        Tactic 2 Solved 0 squares
      Round 3
    ...performing solving tactic 1
        Tactic 1 Solved 0 squares
    ...performing solving tactic 2
        Tactic 2 Solved 0 squares
    ...performing solving tactic 2
    Row 0 isn't solved
      Row 0 needs these numbers solved: [2, 3, 5, 6]
      Row 0 has 4 blank squares.
        Square 0 has these possible solutions: [3, 5, 6]
        Square 1 has these possible solutions: [2, 5, 6]
        Square 2 has these possible solutions: [2, 3]
        Square 4 has these possible solutions: [2, 5]
    Row 1 isn't solved
      Row 1 needs these numbers solved: [2, 4, 5]
      Row 1 has 3 blank squares.
        Square 10 has these possible solutions: [2, 5]
        Square 15 has these possible solutions: [2, 4]
        Square 17 has these possible solutions: [2, 4, 5]
    Row 2 isn't solved
      Row 2 needs these numbers solved: [2, 5]
      Row 2 has 2 blank squares.
        Square 22 has these possible solutions: [2, 5]
        Square 26 has these possible solutions: [2, 5]
    Row 3 isn't solved
      Row 3 needs these numbers solved: [2, 3, 8]
      Row 3 has 3 blank squares.
        Square 27 has these possible solutions: [3, 8]
        Square 34 has these possible solutions: [2, 3, 8]
        Square 35 has these possible solutions: [2, 8]
    Row 4 isn't solved
      Row 4 needs these numbers solved: [2, 3, 4, 5]
      Row 4 has 4 blank squares.
        Square 36 has these possible solutions: [3, 4, 5]
        Square 37 has these possible solutions: [2, 5]
        Square 38 has these possible solutions: [2, 3]
        Square 43 has these possible solutions: [2, 3]
    Row 5 isn't solved
      Row 5 needs these numbers solved: [4, 7, 8]
      Row 5 has 3 blank squares.
        Square 45 has these possible solutions: [4, 8]
        Square 51 has these possible solutions: [4, 7]
        Square 53 has these possible solutions: [4, 7, 8]
    Row 7 isn't solved
      Row 7 needs these numbers solved: [6, 7]
      Row 7 has 2 blank squares.
        Square 63 has these possible solutions: [6, 7]
        Square 69 has these possible solutions: [6, 7]
    Row 8 isn't solved
      Row 8 needs these numbers solved: [2, 6, 7, 8]
      Row 8 has 4 blank squares.
        Square 72 has these possible solutions: [6, 7]
        Square 78 has these possible solutions: [2, 6, 7]
        Square 79 has these possible solutions: [2, 8]
        Square 80 has these possible solutions: [2, 7, 8]
    ==PZL 1 attempted solution===============
    ==================================================
          | 7   4 | 8 9 1
    1   7 | 3 9 8 |   6
    9 8 4 | 1   6 | 3 7
    ---------------------
      7 9 | 4 6 5 | 1
          | 8 7 1 | 9   6
      1 6 | 9 3 2 |   5
    ---------------------
    2 3 8 | 6 1 7 | 5 4 9
      4 5 | 2 8 9 |   1 3
      9 1 | 5 4 3 |
    Row 0 is NOT SOLVED!
    Row 1 is NOT SOLVED!
    Row 2 is NOT SOLVED!
    Row 3 is NOT SOLVED!
    Row 4 is NOT SOLVED!
    Row 5 is NOT SOLVED!
    Row 7 is NOT SOLVED!
    Row 8 is NOT SOLVED!
    Col 0 is NOT SOLVED!
    Col 1 is NOT SOLVED!
    Col 2 is NOT SOLVED!
    Col 4 is NOT SOLVED!
    Col 6 is NOT SOLVED!
    Col 7 is NOT SOLVED!
    Col 8 is NOT SOLVED!
    Box 0 is NOT SOLVED!
    Box 1 is NOT SOLVED!
    Box 2 is NOT SOLVED!
    Box 3 is NOT SOLVED!
    Box 5 is NOT SOLVED!
    Box 6 is NOT SOLVED!
    Box 8 is NOT SOLVED!
    ==================================================
    1 is found 9 times
    9 is found 9 times
    3 is found 6 times
    4 is found 6 times
    6 is found 6 times
    7 is found 6 times
    8 is found 6 times
    5 is found 5 times
    2 is found 3 times
    ==================================================
    I'm NOT SOLVED!
    ==================================================


    
We have a single "tactic" or "strategy" that we are using to try and solve the puzzle, it finds several solutions, but as you can see, it doesn't solve it all the way.  More tactics to come!


## Class Structure

We are organizing the classes in this application to mimic the same structures that are in the Sudoku puzzle, meaning Rows, Columns, Boxes, and Squares.

### SudokuPuzzle

The SudokuPuzzle class is the overaching class that contains all the other classes that will implement the specific functions needed to solve each task.  

For example, the SudokuPuzzle class has a function called `is_solved` that returns a boolean (true/false) telling whether or not the Puzzle is solved.  To do this, it simply asks all of the Boxes, Rows, and Columns if they are solved, and as long as all of them are solved, then the entire Puzzle is solved.

### SudokuBox


### SudokuRow


### SudokuColumn


### SudokuSquare
