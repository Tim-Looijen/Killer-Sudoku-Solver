from constants import *


class Combination:
    def __init__(self, cells, possible_values):
        self.cells = cells
        self.possible_values = possible_values
        self.size = cells.__len__()
        self.sum = sum(possible_values)

    def __str__(self):
        return f"combination: {self.possible_values} " \
               f"sum: {self.sum}" \
               f"\n{[cell.__str__() for cell in self.cells]}"

