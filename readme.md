Welcome to the simple sudoku_solver!

This is a very basic application, and currently doesn't solve any Sudoku at all... lol. But it should get closer as we improve it.

Currently if you run the program you should see this:


    $ python sudoku_solver.py
    Hello World, let's solve some Sudoku!
    Puzzle: 1 SOLVED in 0:00:00.031250 seconds
    ==================================================
    5 6 3 | 7 2 4 | 8 9 1
    1 2 7 | 3 9 8 | 4 6 5
    9 8 4 | 1 5 6 | 3 7 2
    ---------------------
    3 7 9 | 4 6 5 | 1 2 8
    4 5 2 | 8 7 1 | 9 3 6
    8 1 6 | 9 3 2 | 7 5 4
    ---------------------
    2 3 8 | 6 1 7 | 5 4 9
    7 4 5 | 2 8 9 | 6 1 3
    6 9 1 | 5 4 3 | 2 8 7
    ==================================================
    1 is found 9 times
    2 is found 9 times
    3 is found 9 times
    4 is found 9 times
    5 is found 9 times
    6 is found 9 times
    7 is found 9 times
    8 is found 9 times
    9 is found 9 times
    ==================================================
    I'm SOLVED!
    ==================================================

    Puzzle: 2 SOLVED in 0:00:00.015624 seconds
    ==================================================
    9 7 6 | 2 3 5 | 4 8 1
    5 1 8 | 7 6 4 | 2 9 3
    2 3 4 | 1 9 8 | 7 5 6
    ---------------------
    4 6 9 | 8 5 2 | 3 1 7
    1 8 7 | 3 4 9 | 5 6 2
    3 5 2 | 6 7 1 | 9 4 8
    ---------------------
    6 2 5 | 9 1 7 | 8 3 4
    8 4 3 | 5 2 6 | 1 7 9
    7 9 1 | 4 8 3 | 6 2 5
    ==================================================
    1 is found 9 times
    2 is found 9 times
    3 is found 9 times
    4 is found 9 times
    5 is found 9 times
    6 is found 9 times
    7 is found 9 times
    8 is found 9 times
    9 is found 9 times
    ==================================================
    I'm SOLVED!
    ==================================================

    Puzzle: 3 SOLVED in 0:00:00 seconds
    ==================================================
    5 9 2 | 1 6 8 | 4 3 7
    6 1 3 | 4 9 7 | 5 8 2
    4 8 7 | 5 2 3 | 6 9 1
    ---------------------
    3 2 8 | 7 5 1 | 9 6 4
    9 5 6 | 8 4 2 | 1 7 3
    7 4 1 | 9 3 6 | 8 2 5
    ---------------------
    1 6 9 | 3 7 5 | 2 4 8
    8 3 4 | 2 1 9 | 7 5 6
    2 7 5 | 6 8 4 | 3 1 9
    ==================================================
    1 is found 9 times
    2 is found 9 times
    3 is found 9 times
    4 is found 9 times
    5 is found 9 times
    6 is found 9 times
    7 is found 9 times
    8 is found 9 times
    9 is found 9 times
    ==================================================
    I'm SOLVED!
    ==================================================

    Puzzle: 4 NOT SOLVED in 0:00:00.015624 seconds
    ==================================================
          | 3     |     2
      2 7 |       | 5
    5 4 3 | 8     |     1
    ---------------------
    7 9   | 4 8   |
        4 |   7   | 2
          |   9 1 |   7
    ---------------------
    3     |     8 | 9 4 5
    4   5 |       | 8 2
    2 8 9 |     4 |
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
    4 is found 6 times
    2 is found 5 times
    8 is found 5 times
    5 is found 4 times
    7 is found 4 times
    9 is found 4 times
    3 is found 3 times
    1 is found 2 times
    6 is found 0 times
    ==================================================
    I'm NOT SOLVED!


    
We have three "tactics" or "strategies" that we are using to try and solve the puzzles, it finds several solutions and solves the "Easy" and "Medium" puzzles we've tried, however it doesn't solve a "Hard" puzzle as you can see, so we need to look for the next strategy!


## Class Structure

We are organizing the classes in this application to mimic the same structures that are in the Sudoku puzzle, meaning Rows, Columns, Boxes, and Squares.

### SudokuPuzzle

The SudokuPuzzle class is the overaching class that contains all the other classes that will implement the specific functions needed to solve each task.  

For example, the SudokuPuzzle class has a function called `is_solved` that returns a boolean (true/false) telling whether or not the Puzzle is solved.  To do this, it simply asks all of the Boxes, Rows, and Columns if they are solved, and as long as all of them are solved, then the entire Puzzle is solved.

### SudokuBox


### SudokuRow


### SudokuColumn


### SudokuSquare
