from global_imports import *
from Puzzle import Puzzle
from Data import Data

def main():
    # create a new puzzle based on a single screenshot from a connected phone
    data = Data()
    Puzzle = data.fill_puzzle()
    for cell in Puzzle.cells:
        print(cell)
    # solve puzzle, new class Solver will be created
    pass


if __name__ == "__main__":
    main()

