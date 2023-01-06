from DEBUG import DEBUG, Format
from global_imports import *


def add_cages_combinations(puzzle):
    DEBUG.print(Format.Function)
    for cage in puzzle.cages:
        if _single_cage_size(cage):
            continue
        DEBUG.print(Format.Function)
        DEBUG.print(Format.Info, 1, f"filling cage {cage.id} with combinations...")
        # create a list of all possible combinations for the cage

        cage_combinations = []
        _sum = cage.sum
        size = cage.size

        # create combinations based on sum and size and NUMBERS
        for combination in itertools.combinations_with_replacement(NUMBERS, size):
            combination = Combination(cage.cells, combination)
            if combination.sum == _sum \
                    and (combination not in puzzle.combinations)  \
                    and set(combination.possible_values).__len__() == size:
                cage_combinations.append(combination)
                puzzle.add_combination(combination)
                DEBUG.print(Format.Info, 2, f"added combination {combination.possible_values} to cage {cage.id}")
        DEBUG.print(Format.Transition, 1, f"filled cage {cage.id} with {cage_combinations.__len__()} combinations")
    DEBUG.print(Format.Transition, 2, f"added all possible combinations for each cage")


def _single_cage_size(cage):
    if cage.size == 1:
        cage.cells[0].add_value(cage.sum)
        return True


# checks if the same value(s) are/is present in all the cage_combinations
def add_certain_values(cage, cage_combinations):
    DEBUG.print(Format.Function)
    pass


