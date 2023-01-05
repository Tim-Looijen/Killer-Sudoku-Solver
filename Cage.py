from DEBUG import DEBUG, Format
from global_imports import itertools


class Cage:
    id_counter = itertools.count(1)

    def __init__(self, number, color):
        self.id = self.id_counter.__next__()
        self.cells = []
        self.sum = number
        self.color = color
        self.size = self.cells.__len__()

    def __str__(self):
        cells = ',\n'.join(cell.__str__() for cell in self.cells)
        return f"cage: {self.id} " \
               f"number: {self.sum} " \
               f"color: {self.color} " \
               f"\n{cells}"

    def add_cell(self, cell):
        cell.cage_id = self.id
        self.cells.append(cell)