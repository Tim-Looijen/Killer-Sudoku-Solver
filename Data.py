from global_imports import *


# contains all data and functions to create a puzzle based on a screenshot
class Data:
    def __init__(self):
        subprocess.check_output("adb start-server", cwd=adb_server_path, shell=True)
        Client = AdbClient(host="127.0.0.1", port=5037)
        self.device = Client.device(Client.devices()[0].serial)
        self.screenshot = None

        # get screenshot
    def make_screenshot(self):
        self.screenshot = self.device.screencap()

        # crops the image so that only the puzzle is in the screenshot
    def crop_screenshot(self):
        self.screenshot = cv2.imread(self.screenshot)[433:1472, 20:1059]
        pass