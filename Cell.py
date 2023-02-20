import time

from DEBUG import DEBUG, Format


class Cell:
    def __init__(self, position):
        self.position = position
        self.row = position[0]
        self.column = position[1]
        self.box = (self.row - 1) // 3 * 3 + (self.column - 1) // 3 + 1
        self.possible_values = set()
        self.combinations = []
        self.value = 0
        self.cage_id = -1

    def __str__(self):
        return f"cell: {self.position} " \
               f"cage: {self.cage_id} " \
               f"box: {self.box} "

    def add_value(self, value):
        self.possible_values = set()
        self.value = value
        DEBUG.print(Format.Info, 2, f"added the value {value} to {self.__str__()}")

    def add_combination(self, combination):
        if combination not in self.combinations:
            self.combinations.append(combination)
            self.update_possible_values()

    def update_possible_values(self):
        self.possible_values = set()
        for combination in self.combinations:
            [self.possible_values.add(value) for value in combination.possible_values]
