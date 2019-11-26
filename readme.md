Welcome to the simple sudoku_solver!

This is a very basic application, and currently doesn't solve any Sudoku at all... lol. But it should get closer as we improve it.

Currently if you run the program you should see this:

    > python sudoku_solver.py
    Hello World, let's solve some Sudoku!
    =PZL1===================================
    0 0 0 | 7 0 4 | 8 9 0
    1 0 0 | 0 0 8 | 0 6 0
    9 8 0 | 1 0 0 | 3 7 0
    ---------------------
    0 7 0 | 4 6 5 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 9 3 2 | 0 5 0
    ---------------------
    0 3 8 | 0 0 7 | 0 4 9
    0 4 0 | 2 0 0 | 0 0 3
    0 9 1 | 5 0 3 | 0 0 0
    =DATA===================================
    0 0 0 | 7 0 4 | 8 9 0
    1 0 0 | 0 0 8 | 0 6 0
    9 8 0 | 1 0 0 | 3 7 0
    ---------------------
    0 7 0 | 4 6 5 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 9 3 2 | 0 5 0
    ---------------------
    0 3 8 | 0 0 7 | 0 4 9
    0 4 0 | 2 0 0 | 0 0 3
    0 9 1 | 5 0 3 | 0 0 0
    ====================================
    Changing SudokuData
    =PZL1===================================
    0 0 0 | 7 0 4 | 8 9 0
    1 0 0 | 0 0 8 | 0 6 0
    9 8 0 | 1 0 0 | 3 7 0
    ---------------------
    0 7 0 | 4 6 5 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 9 3 2 | 0 5 0
    ---------------------
    0 3 8 | 0 0 7 | 0 4 9
    0 4 0 | 2 0 0 | 0 0 3
    0 9 1 | 5 0 3 | 0 0 0
    =DATA===================================
    5 0 3 | 7 0 4 | 8 9 0
    1 0 0 | 0 0 8 | 0 6 0
    9 8 0 | 1 0 0 | 3 7 0
    ---------------------
    0 7 0 | 4 6 5 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 9 3 2 | 0 5 0
    ---------------------
    0 3 8 | 0 0 7 | 0 4 9
    0 4 0 | 2 0 0 | 0 0 3
    0 9 1 | 5 0 3 | 0 0 0
    NOT SOLVED!!!

This simply illustrates show the SudokuPuzzle class keeps two copies of the original puzzle it is given, one called self.orig_data and the other called self.data.
The intent is to have our algorithms modify the contents of self.data as they attempt to solve the puzzle, and leave self.orig_data unmodified (just for comparisons sake)

