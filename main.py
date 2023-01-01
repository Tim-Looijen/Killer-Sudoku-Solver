from global_imports import *
from DEBUG import DEBUG, Format
from Data import Data
import random


def main(start_time):
    # create a new puzzle based on a single screenshot from a connected phone
    puzzle = Data().fill_puzzle()
    # prints how long it took for the puzzle to be created in milliseconds
    DEBUG.print(Format.Transition, 1, "Puzzle created in %d milliseconds" % ((time.time() - start_time) * 1000))
    DEBUG.print(Format.Info, 2, "Created %d cages" % puzzle.cages.__len__())
    for cage in puzzle.cages:
        DEBUG.print(Format.Info, 2, cage.__str__())
    for cell, combination in puzzle.combinations.items():
        DEBUG.print(Format.Info, 2, f"{combination.__str__()} for {cell.__str__()}")

    # solve puzzle, new class Solver will be created
    pass


if __name__ == "__main__":
    start_time = time.time()
    main(start_time)

