from global_imports import *

from DEBUG import DEBUG, Format
# contains all logic needed to properly export values and combinations to the phone


class Export:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.cells = puzzle.cells
        # used to check if the Noted mode on the phone is enabled
        self.Notes = False
        self.export()

    def export(self):
        self._enable_notes()
        for cell in self.cells:
            self._select_cell(cell)
            self._export_values(cell)

    def _enable_notes(self):
        # check if the Notes mode is enabled
        if not self.Notes:
            self._tab(NOTES_BUTTON)
            self.Notes = True

    @staticmethod
    def _tab(cord):
        x, y = cord
        subprocess.call([ADB_PATH, "shell", "input", "tap", x.__str__(), y.__str__()])

    @staticmethod
    def _select_cell(cell):
        position = cell.position
        x = (position[1] - 1) * CELL_DISTANCE + CELL_SIZE + 20
        y = (position[0] - 1) * CELL_DISTANCE + CELL_SIZE + 417
        subprocess.call([ADB_PATH, "shell", "input", "tap", x.__str__(), y.__str__()])

    @staticmethod
    def _export_values(cell):
        if cell.value != 0:
            subprocess.call([ADB_PATH, "shell", "input", "text", cell.value.__str__()])
        else:
            for value in cell.possible_values:
                subprocess.call([ADB_PATH, "shell", "input", "text", value.__str__()])
