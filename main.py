from global_imports import *
from DEBUG import DEBUG, Format
from Data import Data

def main():
    # create a new puzzle based on a single screenshot from a connected phone
    Puzzle = Data().fill_puzzle()
    for cell in Puzzle.cells:
        print(cell)
    # solve puzzle, new class Solver will be created
    pass


if __name__ == "__main__":
    main()

