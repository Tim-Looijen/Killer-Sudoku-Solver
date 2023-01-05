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
        # runs every algorithm till it is done!
        while not self.solved:
            fill_cages_combinations(self.puzzle)
            DEBUG.print(Format.Transition, 2, f"filled all cages with combinations")
            # prints all cage combinations
            for combination in self.combinations:
                DEBUG.print(Format.Info, 1, f"{combination}")
            break

            pass

