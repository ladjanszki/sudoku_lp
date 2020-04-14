'''
This file contains the utility code for the linear programming sudoku solver
'''

import pulp
import numpy as np

def solutionToMatrix(var):

    # Putting the solution to integer supermatrix (collapsing value dimension)
    solution = np.zeros((3, 3, 3, 3), dtype=int)
    for hRow in range(3): # Hypermatrix rows indexing
        for hCol in range(3): # Hypermatrix column indexing
            for row in range(3): # Submatrix row indexing
                for col in range(3): # Submatrix column indexing
                    for val in range(1, 10): # All values (0 to 9)
                        actCell = int(var[hRow][hCol][row][col][val].varValue)
                        if actCell == 1:
                            solution[hRow, hCol, row, col] = int(val)

    return solution

def matrixPrettyPrinter(solution):

    # Pretty printing the solution
    solutionList = [] # Putting into this list formatted and joining at the end
    solutionList.append(' ' + '-' * 37 + '\n')
    for hRow in range(3): 
        for row in range(3):
            for hCol in range(3):
                solutionList.append(' | ')
                for col in range(3):
                    actCell = solution[hRow, hCol, row, col]
                    if actCell == 0:
                        solutionList.append(' . ')
                    else:
                        solutionList.append('{0:^3d}'.format(actCell))
    
            solutionList.append(' |\n')
        solutionList.append(' ' + '-' * 37 + '\n')

    return ''.join(solutionList)
 
