class Combination:
    def __init__(self, cells, possible_values):
        self.cells = cells
        self.possible_values = possible_values
        self.size = cells.__len__()
        self.sum = sum(possible_values)

    def __str__(self):
        return f"Combination: {self.possible_values} " \
               f"Sum: {self.sum}"
