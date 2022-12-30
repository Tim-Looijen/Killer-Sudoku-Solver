from DEBUG import DEBUG, Format
class Puzzle:
    def __init__(self, cells, cages):
        DEBUG.print(Format.Info, 1, "Creating puzzle...")
        self.cells = cells
        self.cages = cages
        self.column_cages = self.add_column_cages()
        self.row_cages = self.add_row_cages()
        DEBUG.print(Format.Transition, 1, "Puzzle created")

    # checks if the entire cage is solely contained in one column and adds it to the column_cages dictionary
    def add_column_cages(self):
        DEBUG.print(Format.Function, 1)
        columns = {row: [] for row in range(1, 10)}
        for cage in self.cages:
            x = cage.cells[0].column
            if all(x == cell.column for cell in cage.cells):
                columns[x].append(cage)
                DEBUG.print(Format.Info, 1, f"Added cage {(cage.id, cage.number)} to column {x}")
        DEBUG.print(Format.Transition, 1, "Added %d column cages" % [column for column in columns.values() if column].__len__())
        return columns

    # checks if the entire cage is solely contained in one row and adds it to the row_cages dictionary
    def add_row_cages(self):
        DEBUG.print(Format.Function, 1)
        rows = {row: [] for row in range(1, 10)}
        for cage in self.cages:
            y = cage.cells[0].row
            if all(y == cell.row for cell in cage.cells):
                rows[y].append(cage)
                DEBUG.print(Format.Info, 1, f"Added cage {(cage.id, cage.number)} to row {y}")
        # prints the amount of rows which have cages
        DEBUG.print(Format.Transition, 1, "Added %d row cages" % [row for row in rows.values() if row].__len__())
        return rows