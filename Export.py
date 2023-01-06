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

    def export(self):
        DEBUG.print(Format.Function)
        self._enable_notes()
        self._export_combinations()
        self._export_values()

    def _enable_notes(self):
        DEBUG.print(Format.Function)
        # check if the Noted mode on the phone is enabled
        if not self.Notes:
            # if not, enable it

            # get the coordinates on the Notes button and store it in constants.py

            # store the Notes.png file in a variable in constants.py so that there is no need to load it every time

            Notes = pyautogui.locateOnScreen('images/Notes.png')
            self.Notes = True