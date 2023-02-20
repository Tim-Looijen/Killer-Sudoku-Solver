from basic_algoritmes import *


class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.cells = puzzle.cells
        self.cages = puzzle.cages
        self.combinations = puzzle.combinations
        self.column_cages = puzzle.column_cages
        self.row_cages = puzzle.row_cages
        self.solved = False
        self.solve()

    def solve(self):
        DEBUG.print(Format.Function)
        add_cages_combinations(self.puzzle)
        # runs every algorithm till it is done!
        while not self.solved:
            self.validate_combinations()
            break

            pass

    # runs all the combination algorithms to check if each combination is still valid
    def validate_combinations(self):
        DEBUG.print(Format.Function)
        #update_on_single_value_cells(self.puzzle)
