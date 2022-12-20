# ------- INSTRUCTIONS ------- #
# Create a function that takes a grid of '#' and '-', 
# where each hash '#' represents a mine and each dash '-' represents a mine-free spot.
# Return a grid, where each dash is replaced by a digit, 
# indicating the number of mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).

# ------- TASK ------- #

# -- Function -- #

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

# -- Parameters -- #

# Initialise number of rows and columns for the grid size.
num_rows = 5    # alternative: len(grid)
num_cols = 5    # alternative: len(grid[0])

# Determine indexes of the 'input_mines' to pass to the function.
input_mines = [["-", "-", "-", "#", "#"],
             ["-", "#", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "#", "#", "-", "-"],
             ["-", "-", "-", "-", "-"]]

# Iterate through each cell in the range of 'input_mines'.
# The indexed cell is added to empty 'mines' list if it contains a "#"      
mines =[] 

for row in range(len(input_mines)):
	for col in range(len(input_mines[row])):
	    if input_mines[row][col] == "#":
	        mines.append([row, col])

# Call and print minecount() with grid parameters.
print (minecount(mines, num_rows, num_cols))
