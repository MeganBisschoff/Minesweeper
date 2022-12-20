# Minesweeper

A Python game featuring a grid with hidden mines.

## Description

This program is a classic and simple demonstration of the minesweeper game logic.The program defines a function that takes a grid (2D array) of ``#`` and ``-``, where each hash ``#`` represents a mine and each dash ``-`` represents a mine-free spot.

(The number of rows and columns in the grid are hardcoded in, however, it can be adjusted to take any input by using the alternative commented-out code provided in line 42 and 43. The mine locations are also predefined, however, it can be randomly generated using Pythons random library.)

The function returns and prints the grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).

## Programming principles

This program employs the programming principles of conditional logic, comparison operators, list comprehension, 2-dimentional arrays and nested loops.

## Running the program

Run the minesweeper.py file in Visual Studio Code.

## Function preview

```python
# Define function to count the number of mines in the minesweeper grid.
def minecount(mines, num_rows, num_cols):

    # Take in function parameters to
    #   declare and create 2D list for the minesweeper 'grid'
    grid = [[0 for row in range(num_rows)] for col in range(num_cols)]

    # Iterate through the indexed variables in the 'mines' list.
    # Apply the 'mine_row's and 'mine_col'umn indexes 
    #   to the grid to indicate the positions of "#"
    for mine_row, mine_col in mines:
        grid[mine_row][mine_col] = "#"

        # Then iterate through each cell in the grid, but
        #   index the range for the surrounding cell checks from
        #   -1 to +2 for a 3x3 boundary around the current 'row' and 'col' position.
        for row in range(mine_row -1, mine_row +2) :         
            for col in range(mine_col -1, mine_col +2): 

                # Check 'if' the adjacent positionn is not a "#"
                #   and that the 'rol' and 'col' positions are 
                #   no smaller nor bigger than the grid size.               
                # If all three conjunctions are true, the adjacent cell is counted.
                if ( (row >= 0 and row < num_rows) and (col >= 0 and col < num_cols) and grid[row][col] != "#" ):
                    grid[row][col] += 1

    return grid
```

## Output preview

```
[[1, 1, 2, '#', '#'], [1, '#', 3, 3, 2], [2, 4, '#', 2, 0], [1, '#', '#', 2, 0], [1, 2, 2, 1, 0]]
```

## References
[Learn python with minesweeper](https://www.youtube.com/watch?v=ptMMa-SDSeE)

&nbsp;
***
_The art of simplicity is a puzzle of complexity._ ~ Douglas Horton
***
&nbsp;

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Author

**Megan Bisschoff** 2022

Project submitted for Software Engineering learnership Level 1 Task 24 at [HyperionDev](https://www.hyperiondev.com/)

[View](https://www.hyperiondev.com/portfolio/86596/) submission results.  
