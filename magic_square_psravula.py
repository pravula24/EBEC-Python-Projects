"""
Author: Prathyush Ravula, psravula@purdue.edu
Assignment: 07.4 - Magic Square
Date: 3.28/2022

Description:
    This program prints three by three matrices as output
    and also determines if they are magic squares.

Contributors:

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
#Function to print grid output
def print_square(grid):
    print(f"  {grid[0][0]} {grid[0][1]} {grid[0][2]}\n  {grid[1][0]} {grid[1][1]} {grid[1][2]}\n  {grid[2][0]} {grid[2][1]} {grid[2][2]}")

#Function to check extra condition
def checker(grid):
    var = True
    for i in grid:
        for k in i:
            if k > 9 or k < 1:
                var = False
                break
    return var


#Function to see if magic square
def is_magic(grid):
    magic = True
    var_list = []
    var1 = grid[0].count(5)
    var2 = grid[1].count(5)
    var3 = grid[2].count(5)
    totalvar = var1+var2+var3
    if totalvar > 1:
        magic = False
    
    #Iterates through all matrix combinations to check
    for i in range(8):
        var_list.append(False)
    if grid[0][0] + grid[1][1] + grid[2][2] == 15:
        var_list[0] = True
    if grid[0][0] + grid[0][1] + grid[0][2] == 15:
        var_list[1] = True
    if grid[1][0] + grid[1][1] + grid[1][2] == 15:
        var_list[2] = True
    if grid[2][0] + grid[2][1] + grid[2][2] == 15:
        var_list[3] = True
    if grid[0][0] + grid[1][0] + grid[2][0] == 15:
        var_list[4] = True
    if grid[0][1] + grid[1][1] + grid[2][1] == 15:
        var_list[5] = True
    if grid[0][2] + grid[1][2] + grid[2][2] == 15:
        var_list[6] = True
    if grid[0][2] + grid[1][1] + grid[2][0] == 15:
        var_list[7] = True
    
    #Final check
    for j in var_list:
        if j == False:
            magic = j
    return magic



def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Grid Initialization
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grid2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    grid3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    
    #Iterating through grids and function calls
    grids = [grid1, grid2, grid3]
    for i in grids:
        print("Your square is:")
        print_square(i)
        #Checks to see if magic
        decider = is_magic(i)
        check = checker(i)
        #Output statements

        if decider == True and check == True:
            print("It is a Lo Shu magic square!")
        else:
            print("It is not a Lo Shu magic square.")
        print('')
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
