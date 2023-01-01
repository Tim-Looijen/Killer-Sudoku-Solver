from enum import Enum
import logging
import datetime
import inspect
import os

# Used to easily toggle debug output
GLOBAL_DEBUG_LEVEL = 1
AMOUNT_LOG_FILES = 5


def _current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


def _create_debug_file():
    if not os.path.exists("DEBUG"):
        os.makedirs("DEBUG")
    files = os.listdir("DEBUG")
    if files.__len__() >= AMOUNT_LOG_FILES:
        files.sort()
        os.remove("debug/" + files[0])
    return "debug/debug_%s.txt" % _current_time().replace(":", "-")


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
            debug_level = 2
        if debug_level <= GLOBAL_DEBUG_LEVEL or debug_level == 0:
            f = open(current_file, "a")
            # makes sure that any fancy debug output is only printed if the debug_level is high enough
            if _format == Format.Info or debug_level <= 1:
                f.write(_current_time() + ": " + debug + "\n")
                logging.debug(debug)
                f.close()
                return

            elif _format == Format.Function:
                f.write("\n" + _current_time() + ": Function: " + inspect.stack()[1][3] + "\n")
                logging.debug("Function: " + inspect.stack()[1][3])
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
