from global_imports import *
from DEBUG import DEBUG, Format
from Data import Data
from Solver import Solver
from Export import Export


def main(start_time):

    # create a new puzzle based on a single screenshot from a connected phone
    puzzle = Data().fill_puzzle()

    # solve the puzzle
    Solver(puzzle)
    Export(puzzle)
    pass


if __name__ == "__main__":
    start_time = time.time()
    main(start_time)

