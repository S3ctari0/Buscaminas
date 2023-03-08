import random 

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mine = False
class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        for i in range(self.rows):
            for x in range(self.cols):
                print("-",end=" ")
            print()

    def initialize_board(self):
        matriz = [[random.randint(0, 6) for j in range(self.rows)] for i in range(self.cols)]
        minas = random.sample([numero for fila in matriz for numero in fila], 6)
        print(minas)

    def reveal_cell(self, row, col):
        