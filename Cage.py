from global_imports import *

# should only contain code for cages
class Cage:
    newid = itertools.count()

    def __init__(self, cells, value):
        self.id = Cage.newid
        self.cells = []
        self.value = value
        self.size = cells.count()-1

    def add_cell(self, cell):
        cell.cage_id = self.id
        self.cells.append(cell)

    def update_all_cells_value(self, value):
        for cell in self.cells:
            cell.update_value(value)
    def update_all_cells_combinations(self, combinations):
        for cell in self.cells:
            cell.update_combinations(combinations)
