'''
This file contains my solution for the Sodoku problem.
The code were written for the Operations Research course 
taught in the 2020 fall semester at the Budapest Corvinus University

'''
import pulp
import numpy as np

import util


# How many cells to pre-fill in the sudoku table
preFilledCells = 15

validGenerated = False
attempts = 1

while not validGenerated:

    # Creating the problem
    problem = pulp.LpProblem('Sudoku', pulp.LpMinimize)
    
    # VARIABLES 
    var = {}
    for hRow in range(3): # Hypermatrix rows indexing
        var[hRow] = {}
        for hCol in range(3): # Hypermatrix column indexing
            var[hRow][hCol] = {}
            for row in range(3): # Submatrix row indexing
                var[hRow][hCol][row] = {}
                for col in range(3): # Submatrix column indexing
                    var[hRow][hCol][row][col] = {}
                    for val in range(1, 10): # All values (0 to 9)
                        varName = '_'.join(['cell', str(hRow), str(hCol), str(row), str(col), str(val)])
                        var[hRow][hCol][row][col][val] = pulp.LpVariable(varName, 0, 1, cat = 'Integer')
    
    # CONSTRAINTS
    # Every cell can only have one value
    for hRow in range(3): 
        for hCol in range(3):
            for row in range(3):
                for col in range(3):
    
                    constraint = []
                    for val in range(1, 10):
                        constraint.append(var[hRow][hCol][row][col][val])
                    problem += pulp.lpSum(constraint) == 1 , 'Val_{0:05d}_{1:05d}_{2:05d}_{3:05d}'.format(hRow, hCol, row, col)
     
    # Every value can only appear onece in every column
    for hRow in range(3): 
        for row in range(3):
            for val in range(1, 10):
    
                constraint = []
                for hCol in range(3):
                    for col in range(3):
                            constraint.append(var[hRow][hCol][row][col][val])
                problem += pulp.lpSum(constraint) == 1 , 'Row_{0:05d}_{1:05d}_{2:05d}'.format(hRow, row, val)
    
    # Every value can only appear onece in every column
    for hCol in range(3): 
        for col in range(3):
            for val in range(1, 10):
    
                constraint = []
                for hRow in range(3):
                    for row in range(3):
                            constraint.append(var[hRow][hCol][row][col][val])
                problem += pulp.lpSum(constraint) == 1, 'Col_{0:05d}_{1:05d}_{2:05d}'.format(hCol, col, val)
    
    # Every value can only appear one in every sub-matrix
    for hCol in range(3): 
        for hRow in range(3):
            for val in range(1, 10):
    
                constraint = []
                for col in range(3):
                    for row in range(3):
                            constraint.append(var[hRow][hCol][row][col][val])
                problem += pulp.lpSum(constraint) == 1, 'Sub_{0:05d}_{1:05d}_{2:05d}'.format(hCol, hRow, val)
    
    # Some random values so we do not get the same table every time
    initial = np.zeros((3, 3, 3, 3), dtype=int)
    for i in range(preFilledCells):
        rhCol = np.random.randint(3)
        rhRow = np.random.randint(3)
        rrow = np.random.randint(3)
        rcol = np.random.randint(3)
        rval = np.random.randint(1, 10)
    
        problem += var[rhRow][rhCol][rrow][rcol][rval] == 1, 'Rnd_{0:05d}'.format(i)
        initial[rhRow, rhCol, rrow, rcol] = rval 
    
    # OBJECTIVE FUNCTION
    problem += 0, 'All solutions are equally good'
    
    # Solve and print
    problem.solve()
    
    #print(problem.status)
    #print(pulp.LpStatus[problem.status])
    print(str(attempts) + ' attempt to generate...')
    attempts = attempts + 1
  
    if problem.status == 1:
        validGenerated = True


mx = util.solutionToMatrix(var)

print('')
print('The Puzzle: ')
print(util.matrixPrettyPrinter(initial))
print('The SOLUTION: ')
print(util.matrixPrettyPrinter(mx))
 



                    
 




