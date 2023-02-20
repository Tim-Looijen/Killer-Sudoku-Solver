from DEBUG import DEBUG, Format
from global_imports import itertools


class Cage:
    id_counter = itertools.count(1)

    def __init__(self, number, color):
        self.id = self.id_counter.__next__()
        self.cells = []
        self.sum = number
        self.color = color
        self.size = 0
        self.certain_values = []
        self.row = -1
        self.column = -1

    def __str__(self):
        cells = ',\n'.join(cell.__str__() for cell in self.cells)
        return f"cage: {self.id} " \
               f"sum: {self.sum} " \
               f"color: {self.color} " \
               f"size: {self.size} " \
               f"\n{cells}"

    def add_cell(self, cell):
        cell.cage_id = self.id
        self.cells.append(cell)
        self.size += 1

    def add_certain_values(self, values):
        self.certain_values = values
