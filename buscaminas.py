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
        self.tablero = []

    def initialize_board(self):
        self.tablero = [[Cell()]*self.cols for _ in range(self.rows)]

    def __str__(self):
        todo = ''
        for line in self.tablero:
            for element in line:
                if element.is_mine:
                    todo += '+'
                else:
                    todo += '*'
            todo += '\n'
        return todo


tablero = Minesweeper(5, 5, 7)
tablero.initialize_board()
print(tablero)
