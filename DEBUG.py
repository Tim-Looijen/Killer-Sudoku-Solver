import datetime
class DEBUG:
    f = open("app_log.txt", "w")
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.write("   new run at: %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n-----------------------------------------------------------------------------------------------\n")
    f.close()

    @staticmethod
    def write_to_file(format, debug):
        f = open("app_log.txt", "a")
        if format == 0:
            f.write(": " + debug + "\n")
            f.close()
        if format == 1:
            f.write("\n" + debug)
            f.write("\n_______________________________________________________\n")
            f.close()
        if format == 2:
            f.write("!!!" + debug + "!!!\n")
            f.close()
    @staticmethod
    def new_line():
        f = open("app_log.txt", "a")
        f.write("\n")
        f.close()


