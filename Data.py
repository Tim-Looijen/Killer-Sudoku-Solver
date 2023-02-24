from global_imports import *
from DEBUG import DEBUG, Format
from Puzzle import Puzzle


# Fills the Puzzle object based on a screenshot from a connected phone
class Data:
    def __init__(self):
        self.device = self.connect_phone()
        self.move_selection()
        self.image_cv2 = self.create_puzzle_image()
        # saves the screenshot to a file for debugging purposes
        cv2.imwrite("temp/puzzle.png", self.image_cv2)
        self.puzzle = self.fill_puzzle()

    # connects to the phone and returns the device
    @staticmethod
    def connect_phone():
        _adb_folder_path = "scrcpy-win64-v1.24"
        subprocess.check_output("adb start-server", cwd=_adb_folder_path, shell=True)
        client = AdbClient(host="127.0.0.1", port=5037)
        try:
            device = client.device(client.devices()[0].serial)
            return device
        except:
            sys.exit()

    # moves the selected blue square out of the way
    @staticmethod
    def move_selection():
        x = (BOTTOM_LEFT_CELL[1] - 1) * CELL_DISTANCE + CELL_SIZE + 20
        y = (BOTTOM_LEFT_CELL[0] - 1) * CELL_DISTANCE + CELL_SIZE + 417
        subprocess.call([ADB_PATH, "shell", "input", "tap", x.__str__(), y.__str__()])

    # get screenshot from phone
    def create_puzzle_image(self):
        DEBUG.print(Format.Function)
        _screenshot = self.device.screencap()

        # saves the screenshot to a file for debugging purposes
        with open("temp/phone_screen.png", "wb") as f:
            f.write(_screenshot)

        # convert image to numpy array
        _image_np = np.frombuffer(_screenshot, dtype=np.uint8)
        # convert numpy array to a cv2 image
        _image_cv2 = cv2.imdecode(_image_np, cv2.IMREAD_COLOR)

        # crops the image so that only the puzzle is in the screenshot
        return _image_cv2[433:1472, 20:1059]

    def fill_puzzle(self):
        DEBUG.print(Format.Function)
        cells = self.create_cells()
        cages = self.create_cages(cells)
        self.fill_cages(cells, cages)
        return Puzzle(cells, cages)

    # fills the cells list with dummy cells, only containing their position
    @staticmethod
    def create_cells():
        DEBUG.print(Format.Function)
        cells = []
        column = 1
        row = 1
        for i in range(1, 82):
            cells.append(Cell((row, column)))

            # if the cell is in the last column, go to the next row
            if i % 9 == 0:
                column = 0
                row += 1
            column += 1

        return cells

    # loops through all cells and checks if a cage number is present in the cell, if so, it adds the number to the cage
    def create_cages(self, cells):
        cages = []
        for cell in cells:

            # display the image to see why it cant read the cage number
            if cell.position == (2, 1):
                DEBUG.show_image(cell.position)

            cell_number_list = re.findall('[0-9]+', self._read_cage_number(cell.position))
            if cell_number_list.__len__() != 0:
                cage_color = self._cell_color(cell.position)
                cage_number = int(cell_number_list[0])
                cage = Cage(cage_number, cage_color)
                cage.add_cell(cell)
                cages.append(cage)
        return cages

    def fill_cages(self, cells, cages):
        cells_to_check = cells.copy()
        for i in range(0, cells_to_check.__len__()):
            if cells[i].cage_id != -1:
                cells_to_check.remove(cells[i])
        # checks if a cell from the cells list is adjacent to any cell in the cage and has the same cage color
        while cells_to_check.__len__() != 0:
            # raises an exception so that when a cell is removed from the list, the loop doesn't skip a cell
            try:
                for i in range(0, cages.__len__()):
                    cage = cages[i]
                    for j in range(0, cells_to_check.__len__()):
                        cell = cells_to_check[j]
                        cell_color = self._cell_color(cell.position)
                        for cage_cell in cage.cells:
                            if self._are_adjacent(cell.position, cage_cell.position) and np.all(
                                    cell_color == cage.color):
                                cage.add_cell(cell)
                                cells_to_check.remove(cell)
                                raise StopIteration(cell)
            except StopIteration as cell:
                pass
        return cages

    def _cell_color(self, position):
        x = (position[0] - 1) * CELL_DISTANCE + CELL_SIZE
        y = (position[1] - 1) * CELL_DISTANCE + CELL_SIZE
        return self.image_cv2[x, y]

    @staticmethod
    def _are_adjacent(position_1, position_2):
        x1, y1 = position_1
        x2, y2 = position_2
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False

    def _read_cage_number(self, position):
        # -1 because the row and column start at 1
        x = position[0] - 1
        y = position[1] - 1




        # copies the image so that the original image isn't changed
        copied_image = self.image_cv2.copy()
        cell_corner_image = copied_image[1 + CELL_DISTANCE * x:30 + CELL_DISTANCE * x,
                                         5 + CELL_DISTANCE * y:36 + CELL_DISTANCE * y]

        # convert all non-pure-black pixels to white, since numbers in the image
        cell_corner_image[cell_corner_image != 0] = 255

        # adds a white border around the number, so that the number can be easily read by pytesseract
        cell_corner_image = cv2.copyMakeBorder(cell_corner_image, 5, 5, 5, 5, cv2.BORDER_CONSTANT,
                                               value=[255, 255, 255])

        # converts the image to a string
        pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH
        possible_cage_number = pytesseract.image_to_string(cell_corner_image,
                                                           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        return possible_cage_number
