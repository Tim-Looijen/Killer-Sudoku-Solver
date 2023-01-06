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
            for combination in self.combinations:
                DEBUG.print(Format.Info, 1, f"{combination}")
            break

            pass

    # runs all the combination algorithms to check if each combination is still valid
    def validate_combinations(self):
        DEBUG.print(Format.Function)
        self.update_combination_on_cell_value()
        # self.update_combination_on_singe_line()

    def update_combination_on_cell_value(self):
        for cell in self.cells:
            if cell.value:
                for combination in self.combinations:
                    pass
