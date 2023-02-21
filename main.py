from global_imports import *
from DEBUG import DEBUG, Format
from Data import Data
from Solver import Solver
from Export import Export


def main():

    # create a new puzzle based on a single screenshot from a connected phone
    puzzle = Data().puzzle

    # solve the puzzle
    Solver(puzzle)

    # export the cells possible values to the phone
    Export(puzzle)
    pass


if __name__ == "__main__":
    main()

