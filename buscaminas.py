import random 


class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0


class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.cols = cols
        self.rows = rows
        self.num_mines = num_mines
        self.board = []
        self.num_revealed = 0
        self.game_over = False

    def initialize_board(self):
        self.board = [[0]*self.rows for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = Cell()

        for i in range(self.num_mines):
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            while self.board[row][col].is_mine:
                row = random.randint(0, self.rows-1)
                col = random.randint(0, self.cols-1)
            self.board[row][col].is_mine = True
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (row+j in range(self.rows)) and (col+k in range(self.cols)):
                        self.board[row+j][col+k].adjacent_mines += 1

    def reveal_cell(self, row, col):
        if col in range(self.cols) and row in range(self.rows):
            if self.board[row][col].is_revealed:
                return
            self.board[row][col].is_revealed = True
            self.num_revealed += 1
            if self.board[row][col].is_mine:
                self.game_over = True
                return
            if self.board[row][col].adjacent_mines == 0:
                self.reveal_cell(row-1, col)
                self.reveal_cell(row, col-1)
                self.reveal_cell(row+1, col)
                self.reveal_cell(row, col+1)

    def __str__(self):
        board = "  "
        for i in range(rows):
            board += f' {i} '
        board += '\n'
        for index, line in enumerate(self.board):
            board += f'{ index} '
            for element in line:
                if element.is_revealed is False:
                    board += ' - '
                    continue
                if element.is_mine:
                    board += ' X '
                else:
                    board += str(f" {element.adjacent_mines} ")
            board += '\n'
        return board

    def is_win(self):
        if self.num_revealed == self.rows*self.cols - self.num_mines and self.game_over is False:
            return True
        return False


rows = int(input("Ingrese el número de filas: "))
cols = int(input("Ingrese el número de rowumnas: "))
mines = int(input("Ingrese el número de minas: "))


board = Minesweeper(rows, cols, mines)
board.initialize_board()


while (board.game_over is False or board.is_win()):
    row = int(input("Ingrese el número de la fila de la casilla a revelar: "))
    col = int(input("Ingrese el número de la rowumna de la casilla a revelar: "))
    board.reveal_cell(row, col)
    if board.game_over:
        print("¡Lo siento, has perdido!")
        print(board)
        break
    if board.is_win():
        print("¡Haz Ganado, felicidades!")
        print(board)
        break
    print(board)
