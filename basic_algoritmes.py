from DEBUG import DEBUG, Format
from global_imports import *


def add_cages_combinations(puzzle):
    for cage in puzzle.cages:
        if cage.size == 1:
            cage.cells[0].value = cage.sum
            continue

        # create a list of all possible combinations for the cage
        cage_combinations = []
        _sum = cage.sum
        size = cage.size

        # create combinations based on sum, size and NUMBERS
        for possible_values in itertools.combinations_with_replacement(NUMBERS, size):
            possible_values = list(possible_values)
            combination = Combination(cage.cells, possible_values)
            # check if the combination is valid based on the killer sudoku rules and if it is not already in the cage
            if combination.sum == _sum \
                    and combination not in cage_combinations \
                    and set(combination.possible_values).__len__() == size:
                cage_combinations.append(combination)
                combination.add_combination_to_cells()


# ----------------------------------------Single value cells algorithm--------------------------------------------------
