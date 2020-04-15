# How to solve a Sudoku with linear programming
## Content
In this repository the code and the documentation can be found for the project that have been written for the Operations Research course taught at the Budapest Corvinus Univerity in the 2020 fall semester.
The code for the task can be found in the two py files. Currently no test code have been added to this repository.
If you encounter this repository as a downloaded zip version the newest version can be found online at my GitHub page
```
https://github.com/ladjanszki/sudoku_lp
```

## Dependencies
The code uses numpy and the frequently used Python linear programming package Pulp. The development and thes environment can be recreated by using the conda environment.
The repository contains the `environment.yml` file from which the development and testing environment can be rebuilt by invoking the following command
```
conda create -f environment.yml
```

## Usage
The code can be invoked by the following commanfd from the linux command line. 

```
python sudoku_lp.py
```

This should print an output similar to the following.
```
Generating...
Difficulty: 9/10

The Puzzle: 
 -------------------------------------
 |  5  .  6  |  .  .  .  |  .  .  .  |
 |  .  .  .  |  .  2  .  |  .  .  .  |
 |  .  1  .  |  .  .  .  |  .  .  .  |
 -------------------------------------
 |  .  .  .  |  .  .  .  |  .  .  .  |
 |  .  .  .  |  .  .  8  |  .  .  .  |
 |  .  .  .  |  .  .  .  |  .  .  .  |
 -------------------------------------
 |  .  .  .  |  .  .  .  |  .  .  8  |
 |  .  .  .  |  .  .  .  |  .  .  .  |
 |  .  .  .  |  .  .  .  |  .  .  .  |
 -------------------------------------

The SOLUTION: 
 -------------------------------------
 |  5  2  6  |  8  1  7  |  4  9  3  |
 |  8  3  4  |  9  2  5  |  7  6  1  |
 |  9  1  7  |  4  3  6  |  8  5  2  |
 -------------------------------------
 |  3  9  8  |  1  5  4  |  6  2  7  |
 |  6  7  5  |  2  9  8  |  1  3  4  |
 |  1  4  2  |  7  6  3  |  5  8  9  |
 -------------------------------------
 |  4  5  3  |  6  7  2  |  9  1  8  |
 |  2  8  9  |  5  4  1  |  3  7  6  |
 |  7  6  1  |  3  8  9  |  2  4  5  |
 -------------------------------------
```
The difficulty of the Sudoku table can be set in the code by setting the `difficulty` parameter to a number between 1 and 9.  

## Internals
The code works as follows.
* The script attempts to generate a random Sudoku table by generating a linear program
* The sudoku can be solved as a linear program by doing the following
* We generate 9x9x9 binary variables.
* 9x9 for the cells of the Sudoku table and 9 for every value
* We add the constraints to the linear problem
* Every cell can have exactly one value in it
* Every row should have every value once
* Every column should have every value onece
* Every sub-matrix should have every value once
* After this we add `preFilledCells` number of random entries into the empty sudoku table (as constraints)
* The LP then solved
* If there is no valid solution for the linear initial state a new generation is started
* If there is a valid solution the puzzle and the solution is printed to the terminal.
* The puzzle is generated from the solution by deleting some entries from the solved table
* The number of deleted elemnts can be set by the `difficulty` parameter from 1 to 9





