import logging
import datetime
from enum import Enum
import inspect
# Used to easily toggle debug output
GLOBAL_DEBUG_LEVEL = 2


# Used to change the debug write Format
class Format(Enum):
    Info = 1
    Function = 2
    Transition = 3
    Error = 4


# get the current time to see how long each section of the program takes to run
def _current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


class DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    f = open("app_log.txt", "w")
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.write("   new run at: %s" % _current_time())
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.close()

    @staticmethod
    def print(_format, debug_level, debug=None):
        if debug_level >= GLOBAL_DEBUG_LEVEL:
            return

        f = open("app_log.txt", "a")
        if _format == Format.Info:
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
