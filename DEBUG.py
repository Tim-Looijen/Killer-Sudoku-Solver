from enum import Enum
import logging
import datetime
import inspect
import os
import cv2
from constants import *
# Used to easily toggle debug output
GLOBAL_DEBUG_LEVEL = 2
AMOUNT_LOG_FILES = 5
DEBUG_IMAGE = False


# return current time in the format [HH:MM:SS.MS]
def _current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


# returns current date in the format [YYYY_MM_DD HH:MM:SS]
def _current_date():
    return datetime.datetime.now().strftime("%Y_%m_%d %H!%M!%S")


def _create_debug_file():
    if not os.path.exists("DEBUG"):
        os.makedirs("DEBUG")
    files = os.listdir("DEBUG")

    # if there are more than AMOUNT_LOG_FILES files in the DEBUG folder, delete the oldest one
    if files.__len__() >= AMOUNT_LOG_FILES:
        files.sort()
        os.remove("debug/" + files[0])
    return f"debug/debug_{_current_date()}.txt"


# used to format the debug output
class Format(Enum):
    Info = 1
    Function = 2
    Transition = 3
    Error = 4


current_file = _create_debug_file()


class DEBUG:
    logging.basicConfig(level=logging.DEBUG)

    f = open(current_file, "w")
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.write("   new run at: %s" % _current_time())
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.close()

    @staticmethod
    def print(_format, debug_level=0, debug=None):
        if _format == Format.Error:
            debug_level = 0
        if _format == Format.Function:
            debug_level = 3
        if debug_level <= GLOBAL_DEBUG_LEVEL or debug_level == 0:
            f = open(current_file, "a")
            # makes sure that any fancy debug output is only printed if the debug_level is high enough
            if _format == Format.Info or GLOBAL_DEBUG_LEVEL <= 1:
                f.write(_current_time() + ": " + debug + "\n")
                logging.debug(debug)
                f.close()
                return

            elif _format == Format.Function:
                f.write("\n" + _current_time() + ": function: " + inspect.stack()[1][3] + "\n")
                logging.debug("function: " + inspect.stack()[1][3])
                f.close()
                return

            elif _format == Format.Transition:
                f.write("\n" + _current_time() + ": " + debug)
                logging.debug(debug)
                f.write("\n_______________________________________________________\n\n")
                f.close()
                return

            elif _format == Format.Error:
                f.write("ERROR: " + debug + "\n")
                logging.error(debug)
                f.close()
                return

    # shows the cell corner at the specified position, so that I can see why a cell's number is not being read
    @staticmethod
    def show_image(position):
        if DEBUG_IMAGE:
            x = position[0] - 1
            y = position[1] - 1

            # copies the image so that the original image isn't changed
            copied_image = cv2.imread("puzzle.png").copy()
            cell_corner_image = copied_image[1 + CELL_DISTANCE * x:30 + CELL_DISTANCE * x,
                                             1 + CELL_DISTANCE * y:36 + CELL_DISTANCE * y]

            # convert all non-pure-black pixels to white, since numbers in the image
            cell_corner_image[cell_corner_image != 0] = 255

            # adds a white border around the number, so that the number can be easily read by pytesseract
            cell_corner_image = cv2.copyMakeBorder(cell_corner_image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

            cv2.imshow("image", cell_corner_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
