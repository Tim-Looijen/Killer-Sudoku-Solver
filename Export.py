from global_imports import *

from DEBUG import DEBUG, Format
# contains all logic needed to properly export values and combinations to the phone

class Export:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.combinations = puzzle.combinations
        self.cells = puzzle.cells
        # used to check if the Noted mode on the phone is enabled
        self.Notes = False
        self.export()

    def export(self):
        DEBUG.print(Format.Function)
        self._enable_notes()
        #self._export_values()

    def _enable_notes(self):
        DEBUG.print(Format.Function)
        # check if the Noted mode on the phone is enabled
        if not self.Notes:
            self._tab(NOTES_BUTTON)
            self.Notes = True
    @staticmethod
    def _tab(cord):
        x, y = cord
        subprocess.call([ADB_PATH, "shell", "input", "tap", x.__str__(), y.__str__()])