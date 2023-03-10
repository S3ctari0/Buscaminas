import random 
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.adj_mines = 0

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.tablero = []

    def initialize_board(self):
        self.tablero = [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.cols):
            for j in range(self.rows):
                self.tablero[i][j] = Cell()

        for i in range(self.num_mines):
            columna = random.randint(0, self.cols-1)
            fila = random.randint(0, self.rows-1)
            while self.tablero[columna][fila].is_mine:
                columna = random.randint(0, self.cols-1)
                fila = random.randint(0, self.rows-1)
            self.tablero[columna][fila].is_mine = True
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (columna+j in range(self.cols)) and (fila+k in range(self.rows)): 
                        self.tablero[columna+j][fila+k].adj_mines += 1
    
    def reveal_cell(self,row,col):
        if row in range(self.rows) and col in range(self.cols):
            self.tablero[col][row].is_revealed = True

    def __str__(self):
        tablero = ""
        for line in self.tablero:
            for element in line:
                if element.is_revealed == False:
                    tablero += ' * '
                    continue
                if element.is_mine:
                    tablero += ' + '
                else:
                    tablero += str(f" {element.adj_mines} ")
            tablero += '\n'
        return tablero
    
tablero = Minesweeper(10, 10, 7)
tablero.initialize_board()
print(tablero)
tablero.reveal_cell(3,4)
print(tablero)
