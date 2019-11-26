Welcome to the simple sudoku_solver!

This is a very basic application, and currently doesn't solve any Sudoku at all... lol. But it should get closer as we improve it.

Currently if you run the program you should see this:

    > python sudoku_solver.py
    Hello World, let's solve some Sudoku!
    ==PZL 1==================================
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
    NOT SOLVED!!!
    ==PZL 1 SOLUTION========================
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
    WE SOLVED IT!!!!

Well, we didn't really solve it, but instead our code was able to accurately tell us that the first puzzle wasn't solved, and that the second puzzle (the solution) was solved! So that's a good starting point.


## Class Structure

We are organizing the classes in this application to mimic the same structures that are in the Sudoku puzzle, meaning Rows, Columns, Boxes, and Squares.

### SudokuPuzzle

The SudokuPuzzle class is the overaching class that contains all the other classes that will implement the specific functions needed to solve each task.  

For example, the SudokuPuzzle class has a function called `is_solved` that returns a boolean (true/false) telling whether or not the Puzzle is solved.  To do this, it simply asks all of the Boxes, Rows, and Columns if they are solved, and as long as all of them are solved, then the entire Puzzle is solved.

### SudokuBox


### SudokuRow


### SudokuColumn


### SudokuSquare
