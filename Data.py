from global_imports import *
from constants import *
from Puzzle import Puzzle


# contains all data and functions to create a puzzle based on a screenshot
class Data:
    def __init__(self):
        _adb_server_path = "C:/Users/tim/Desktop/Programming/Python/Programs/Killer_Sudoku_New/scrcpy-win64-v1.24"
        subprocess.check_output("adb start-server", cwd=_adb_server_path, shell=True)
        client = AdbClient(host="127.0.0.1", port=5037)
        self.device = client.device(client.devices()[0].serial)
        self.image = self.create_puzzle_image()

    # get screenshot from phone
    def create_puzzle_image(self):
        self.image = self.device.screencap()
        # crops the image so that only the puzzle is in the screenshot
        return cv2.imread(self.image)[433:1472, 20:1059]

    def fill_puzzle(self):
        cells = self.create_cells()
        cages = self.create_cages(cells)
        self.fill_cages(cells, cages)
        return Puzzle(cells, cages)

    # fills the cells list with dummy cells, only containing their position
    def create_cells(self):
        cells = []
        column = 1
        row = 1
        cell_x = CELL_SIZE
        cell_y = CELL_SIZE
        for i in range(1, 82):
            cells.append(Cell((row, column)))
            cell_x += CELL_DISTANCE
            # if the cell is in the last column, go to the next row
            if i % 9 == 0:
                cell_y += CELL_DISTANCE
                cell_x = 55
                column = 0
                row += 1
            column += 1
        return cells

    # loops through all cells and checks if a cage number is present in the cell, if so, it adds the number to the cage
    def create_cages(self, cells):
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
                cages.append(cage)
        return cages

    # fills the cages with the cells that are contained in the cage
    def fill_cages(self, cells, cages):
        cells_to_check = cells
        for cell in cells_to_check:
            for cage in cages:
                for cage_cell in cage.cells:
                    cell_color = self._cell_color(cell.position)
                    if self._are_adjacent(cell.position, cage_cell.position) and cage.color == cell_color:
                        cell.cage_id = cage.id
                        cage.add_cell(cell)
                        cells_to_check.remove(cell)
                        break
        return cages

    def _cell_color(self, position):
        x = position[0]
        y = position[1]
        return self.image.getpixel((x, y))

    def _are_adjacent(self, position_1, position_2):
        x1, y1 = position_1
        x2, y2 = position_2
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False

    def _read_cage_number(self, position):
        x = position[0]
        y = position[1]
        img = cv2.imread(self.image)[1 + CELL_DISTANCE * x:30 + CELL_DISTANCE * x, 0 + CELL_DISTANCE * y:36 + CELL_DISTANCE * y]
        img[img != 0] = 255
        img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        # OCR
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        d = pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        return d