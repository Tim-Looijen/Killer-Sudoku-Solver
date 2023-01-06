from constants import *


class Combination:
    def __init__(self, cells, possible_values):
        self.cells = cells
        self.possible_values = possible_values
        self.size = cells.__len__()
        self.sum = sum(possible_values)
        self.on_single_line = self._on_single_line()

    def __str__(self):
        return f"combination: {self.possible_values} " \
               f"sum: {self.sum}" \
               f"cells: \n{[cell.__str__() for cell in self.cells]}"

    # check if all cells in the combination are on the same line
    def _on_single_line(self):
        row = self.cells[0].row
        column = self.cells[0].column
        on_row = True
        on_column = True
        for cell in self.cells:
            if cell.row != row:
                on_row = False
                break
        for cell in self.cells:
            if cell.column != column:
                on_column = False
                break
        return on_row or on_column

    def remove_possible_value(self, value):
        self.possible_values.remove(value)