# contains all cells and cages
# should not contain double code
class Puzzle:
    def __init__(self, cells, cages):
        self.cells = cells
        self.cages = cages
        self.column_cages = self.add_column_cages()
        self.row_cages = self.add_row_cages()

    # checks if the entire cage is solely contained in one column and adds it to the column_cages dictionary
    def add_column_cages(self):
        columns = {}
        for cage in self.cages:
            x = cage.cells[0].get_x_cord()
            column = []
            for cell in cage.cells:
                if cell.get_x_cord() == x:
                    column.append(cage)
                else:
                    column = []
                    break
            for cage in column:
                columns[x].append(cage)
        return columns

    # checks if the entire cage is solely contained in one row and adds it to the row_cages dictionary
    def add_row_cages(self):
        rows = {}
        for cage in self.cages:
            y = cage.cells[0].get_y_cord()
            row = []
            for cell in cage.cells:
                if cell.get_y_cord() == y:
                    row.append(cage)
                else:
                    row = []
                    break
            for cage in row:
                rows[y].append(cage)
        return rows