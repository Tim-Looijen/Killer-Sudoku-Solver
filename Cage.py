from global_imports import itertools


class Cage:
    id_counter = itertools.count(1)

    def __init__(self, number, color):
        self.id = self.id_counter.__next__()
        self.cells = []
        self.number = number
        self.color = color
        self.size = 0

    def __str__(self):
        cells = ',\n'.join(cell.__str__() for cell in self.cells)
        return f"Cage: {self.id} " \
               f"Number: {self.number} " \
               f"Color: {self.color} " \
               f"Cells: \n{cells}"

    def add_cell(self, cell):
        cell.cage_id = self.id
        self.cells.append(cell)
        self.size += 1

    def update_all_cells_value(self, value):
        for cell in self.cells:
            cell.update_value(value)

    def update_all_cells_combinations(self, combinations):
        for cell in self.cells:
            cell.update_combinations(combinations)
