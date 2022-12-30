# should only contain code for cells
class Cell:
    def __init__(self, position):
        self.position = position
        self.column = position[0]
        self.row = position[1]
        self.value = 0
        self.combinations = []
        self.cage_id = -1

    def __str__(self):
        return f"Cell: {self.position} " \
               f"Cage: {self.cage_id}"
    def add_value(self, value):
        if self.value == value:
            return
        self.value = value

    def add_combination(self, combinations):
        self.combinations == combinations
