from DEBUG import DEBUG, Format, inspect

class Cell:
    def __init__(self, position):
        self.position = position
        self.row = position[0]
        self.column = position[1]
        self.value = 0
        self.cage_id = -1

    def __str__(self):
        return f"cell: {self.position} " \
               f"cage: {self.cage_id}"

    def add_value(self, value):
        self.combinations = None
        self.value = value
        DEBUG.print(Format.Info, 2, f"added the value {value} to {self.__str__()}")
