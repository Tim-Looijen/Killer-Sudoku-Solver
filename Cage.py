from Global_Imports import *

# should only contain code for cages
class Cage:
    newid = itertools.count()

    def __init__(self, cells, value):
        self.id = Cage.newid
        self.cells = cells
        self.value = value
        self.size = cells.count()-1

    def add_cells(self, cells):
        self.cells = cells

    def update_cells_value(self, value):
        for cell in self.cells:
            cell.update_value(value)

    def update_cells_combinations(self, combinations):
        for cell in self.cells:
            cell.update_combinations(combinations)
