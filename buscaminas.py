import random 
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.num_mines = 0

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
            print(f"{columna}, {fila}")
            self.tablero[columna][fila].is_mine = True

    def __str__(self):
        todo = ''
        for line in self.tablero:
            for element in line:
                if element.is_mine:
                    todo += '+ '
                else:
                    todo += '* '
            todo += '\n'
        return todo

tablero = Minesweeper(5, 5, 7)
tablero.initialize_board()
print(tablero)
