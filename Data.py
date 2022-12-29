from global_imports import *
from constants import *
from Puzzle import Puzzle




# contains all data and functions to create a puzzle based on a screenshot
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app_log.txt', filemode='w')
class Data:
    def __init__(self):
        logging.info("Data init")
        _adb_server_path = "C:/Users/tim/Desktop/Programming/Python/Programs/Killer_Sudoku_New/scrcpy-win64-v1.24"
        subprocess.check_output("adb start-server", cwd=_adb_server_path, shell=True)
        client = AdbClient(host="127.0.0.1", port=5037)
        self.device = client.device(client.devices()[0].serial)
        self.image_cv2 = self.create_puzzle_image()
        cv2.imwrite("puzzle.png", self.image_cv2)

    # get screenshot from phone
    def create_puzzle_image(self):
        logging.info("create_puzzle_image")
        _screenshot = self.device.screencap()

        # convert image to numpy array
        _image_np = np.frombuffer(_screenshot, dtype=np.uint8)
        # convert numpy array to a cv2 image
        _image_cv2 = cv2.imdecode(_image_np, cv2.IMREAD_COLOR)

        # crops the image so that only the puzzle is in the screenshot
        return _image_cv2[433:1472, 20:1059]


    def fill_puzzle(self):
        logging.info("fill_puzzle")
        cells = self.create_cells()
        cages = self.create_cages(cells)
        self.fill_cages(cells, cages)
        return Puzzle(cells, cages)

    # fills the cells list with dummy cells, only containing their position
    def create_cells(self):
        logging.info("create_cells")
        cells = []
        column = 1
        row = 1
        cell_x = CELL_SIZE
        cell_y = CELL_SIZE
        for i in range(1, 82):
            cells.append(Cell((row, column)))
            DEBUG.write_to_file(0, "added cell: %s" % cells[i - 1].__str__())
            cell_x += CELL_DISTANCE

            # if the cell is in the last column, go to the next row
            if i % 9 == 0:
                cell_y += CELL_DISTANCE
                cell_x = 55
                column = 0
                row += 1
            column += 1
        DEBUG.write_to_file(1, "Added %d cells" % cells.__len__())
        return cells

    # loops through all cells and checks if a cage number is present in the cell, if so, it adds the number to the cage
    def create_cages(self, cells):
        logging.info("create_cages")
        cages = []
        for i in range(0, cells.__len__()):
            cage_size = self._read_cage_number(cells[i].position)
            cell_number_list = re.findall('[0-9]+', cage_size)
            if cell_number_list.__len__() != 0:
                cage_number = int(cell_number_list[0])
                cell = cells[i]
                cage_color = self._cell_color(cell.position)
                cage = Cage(cage_number, cage_color)
                cell.cage_id = cage.id
                cage.add_cell(cell)
                DEBUG.write_to_file(0, "added cage: %d with cell: (%s))" % (cage_number, cell.__str__()))
                logging.info("added cage: %d with cell: (%s))" % (cage_number, cell.__str__()))
                cages.append(cage)
        DEBUG.write_to_file(1, "Added %d cages" % cages.__len__())
        return cages

    # fills the cages with the cells that are contained in the cage
    def fill_cages(self, cells, cages):
        logging.info("fill_cages")
        # creates a copy of cells so that the original list is not modified
        cells_to_check = cells
        while cells_to_check.__len__() != 0:

            # DEBUG STUFF
            if (cells_to_check.__len__() == 22):
                for cell in cells:
                    print(cell)
                for cell in cells_to_check:
                    print(cell)
                print(cages[0].cells[0].__str__())

                time.sleep(120)
            try:
                for cell in cells_to_check:
                    cell_color = self._cell_color(cell.position)
                    for cage in cages:
                        for cage_cell in cage.cells:
                            if np.all(cell.position == cage_cell.position):
                                cells_to_check.remove(cell)
                                # raises an exception so that the loop is exited
                                raise Exception(cell)
                            if self._are_adjacent(cell.position, cage_cell.position):
                                if np.all(cell_color == cage.color):
                                    cage.add_cell(cell)
                                    cells_to_check.remove(cell)
                                    # raises an exception so that the loop is exited
                                    raise Exception(cell)
            except Exception as cell:
                DEBUG.write_to_file(0, "removed cell: %s" % (cell.__str__()))

        return cages

    def _cell_color(self, position):
        x = (position[0]-1) * CELL_DISTANCE + CELL_SIZE
        y = (position[1]-1) * CELL_DISTANCE + CELL_SIZE
        return self.image_cv2[y, x]

    def _are_adjacent(self, position_1, position_2):
        x1, y1 = position_1
        x2, y2 = position_2
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False

    def _read_cage_number(self, position):
        # -1 because the row and column start at 1
        x = position[0] - 1
        y = position[1] - 1
        puzzle_image = self.image_cv2[1 + CELL_DISTANCE * x:30 + CELL_DISTANCE * x,
                                                            0 + CELL_DISTANCE * y:36 + CELL_DISTANCE * y]
        # convert all non-pure-black pixels to white, since numbers in the image
        puzzle_image[puzzle_image != 0] = 255
        # adds a white border around the number, so that the number can be easily read by pytesseract
        puzzle_image = cv2.copyMakeBorder(puzzle_image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # OCR
        pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_PATH
        possible_cage_number = pytesseract.image_to_string(puzzle_image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        return possible_cage_number
