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
    ==PZL 1 attempted solution===============
    ==================================================
          | 7   4 | 8 9 1
    1   7 | 3 9 8 |   6
    9 8 4 | 1   6 | 3 7
    ---------------------
      7   | 4 6 5 |
          | 8 7 1 |
      1   | 9 3 2 |   5
    ---------------------
      3 8 | 6 1 7 |   4 9
      4   | 2 8 9 |     3
      9 1 | 5 4 3 |
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
    1 is found 7 times
    9 is found 7 times
    3 is found 6 times
    4 is found 6 times
    7 is found 6 times
    8 is found 6 times
    6 is found 4 times
    5 is found 3 times
    2 is found 2 times
    ==================================================
    I'm NOT SOLVED!
    ==================================================
    
    ==PZL 9==================================
    ==================================================
      7   |       | 4
    5 1 8 |     4 |
      3   | 1     |   5
    ---------------------
        9 | 8 5   |   1 7
        7 | 3   9 | 5
    3 5   |   7 1 | 9
    ---------------------
      2   |     7 |   3
          | 5     | 1 7 9
        1 |       |   2
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
    1 is found 6 times
    5 is found 6 times
    7 is found 6 times
    3 is found 4 times
    9 is found 4 times
    2 is found 2 times
    4 is found 2 times
    8 is found 2 times
    6 is found 0 times
    ==================================================
    I'm NOT SOLVED!
    ==================================================
    
    Attempting to solve the puzzle!
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 2 Row: 0 Col: 8 = 1
        WE FOUND A SOLUTION! Box: 3 Row: 4 Col: 0 = 1
        WE FOUND A SOLUTION! Box: 7 Row: 6 Col: 4 = 1
        WE FOUND A SOLUTION! Box: 1 Row: 0 Col: 5 = 5
        WE FOUND A SOLUTION! Box: 6 Row: 6 Col: 2 = 5
        WE FOUND A SOLUTION! Box: 8 Row: 8 Col: 8 = 5
        WE FOUND A SOLUTION! Box: 1 Row: 1 Col: 3 = 7
        WE FOUND A SOLUTION! Box: 2 Row: 2 Col: 6 = 7
        WE FOUND A SOLUTION! Box: 6 Row: 8 Col: 0 = 7
        WE FOUND A SOLUTION! Box: 5 Row: 3 Col: 6 = 3
        WE FOUND A SOLUTION! Box: 6 Row: 7 Col: 2 = 3
        WE FOUND A SOLUTION! Box: 8 Row: 6 Col: 8 = 4
        WE FOUND A SOLUTION! Box: 3 Row: 4 Col: 1 = 8
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 2 Row: 1 Col: 8 = 3
    ...performing solving tactic 1
        WE FOUND A SOLUTION! Box: 1 Row: 0 Col: 4 = 3
        WE FOUND A SOLUTION! Box: 7 Row: 8 Col: 5 = 3
    ...performing solving tactic 1
    ==PZL 9 attempted solution===============
    ==================================================
      7   |   3 5 | 4   1
    5 1 8 | 7   4 |     3
      3   | 1     | 7 5
    ---------------------
        9 | 8 5   | 3 1 7
    1 8 7 | 3   9 | 5
    3 5   |   7 1 | 9
    ---------------------
      2 5 |   1 7 |   3 4
        3 | 5     | 1 7 9
    7   1 |     3 |   2 5
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
    1 is found 9 times
    3 is found 9 times
    5 is found 9 times
    7 is found 9 times
    9 is found 4 times
    4 is found 3 times
    8 is found 3 times
    2 is found 2 times
    6 is found 0 times
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
