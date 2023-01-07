from DEBUG import DEBUG, Format, inspect

class Cell:
    def __init__(self, position):
        self.position = position
        self.row = position[0]
        self.column = position[1]
        self.possible_values = set()
        self.value = 0
        self.cage_id = -1

    def __str__(self):
        return f"cell: {self.position} " \
               f"cage: {self.cage_id}"

    def add_value(self, value):
        self.possible_values = None
        self.value = value
        DEBUG.print(Format.Info, 2, f"added the value {value} to {self.__str__()}")

    def add_possible_values(self, values):
        [self.possible_values.add(value) for value in values]
