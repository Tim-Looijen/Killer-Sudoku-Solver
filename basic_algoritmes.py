from DEBUG import DEBUG, Format
from global_imports import *


def add_cages_combinations(puzzle):
    DEBUG.print(Format.Function)
    for cage in puzzle.cages:
        if cage.size == 1:
            cage.cells[0].value = cage.sum
            continue
        DEBUG.print(Format.Function)
        DEBUG.print(Format.Info, 1, f"filling cage {cage.id} with combinations...")
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
                puzzle.add_combination(combination)
                DEBUG.print(Format.Info, 2, f"added combination {combination.possible_values} to cage {cage.id}")
        DEBUG.print(Format.Transition, 1, f"filled cage {cage.id} with {cage_combinations.__len__()} combinations")
    DEBUG.print(Format.Transition, 2, f"added all possible combinations for each cage")


# ----------------------------------------Single value cells algorithm--------------------------------------------------
