from DEBUG import DEBUG, Format


class Puzzle:
    def __init__(self, cells, cages):
        self.cells = cells
        self.cages = cages
        self.column_cages = self.add_column_cages()
        self.row_cages = self.add_row_cages()

    # checks if the entire cage is solely contained in one column and adds it to the column_cages dictionary
    def add_column_cages(self):
        DEBUG.print(Format.Function)
        columns = {row: [] for row in range(1, 10)}
        for cage in self.cages:
            x = cage.cells[0].column
            if all(x == cell.column for cell in cage.cells):
                columns[x].append(cage)
                DEBUG.print(Format.Info, 2, f"Added cage {(cage.id, cage.number)} to column {x}")
        DEBUG.print(Format.Transition, 2, "Filled %d columns" % [column for column in columns.values() if column].__len__())
        return columns

    # checks if the entire cage is solely contained in one row and adds it to the row_cages dictionary
    def add_row_cages(self):
        DEBUG.print(Format.Function)
        rows = {row: [] for row in range(1, 10)}
        for cage in self.cages:
            y = cage.cells[0].row
            if all(y == cell.row for cell in cage.cells):
                rows[y].append(cage)
                DEBUG.print(Format.Info, 2, f"Added cage {(cage.id, cage.number)} to row {y}")
        # prints the amount of rows which have cages
        DEBUG.print(Format.Transition, 2, "Filled %d rows" % [row for row in rows.values() if row].__len__())
        return rows
