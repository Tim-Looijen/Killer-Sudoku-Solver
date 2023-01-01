class Cell:
    def __init__(self, position):
        self.position = position
        self.row = position[0]
        self.column = position[1]
        self.value = 0
        self.cage_id = -1

    def __str__(self):
        return f"Cell: {self.position} " \
               f"Cage: {self.cage_id}"

    def add_value(self, value):
        if self.value == value:
            return
        self.value = value
