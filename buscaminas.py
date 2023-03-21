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
        self.board = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
        mines = random.sample(range(self.rows*self.cols), self.num_mines)
        for index in mines:
            row, col = divmod(index, self.cols)
            while self.board[row][col].is_mine:
                index = random.randint(0, self.rows*self.cols-1)
                row, col = divmod(index, self.cols)
            self.board[row][col].is_mine = True
            for i in range(max(0, row-1), min(self.rows, row+2)):
                for j in range(max(0, col-1), min(self.cols, col+2)):
                    self.board[i][j].adjacent_mines += 1

    def reveal_cell(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if self.board[r][c].is_revealed:
                continue
            self.board[r][c].is_revealed = True
            self.num_revealed += 1
            if self.board[r][c].is_mine:
                self.game_over = True
                return
            if self.board[r][c].adjacent_mines == 0:
                if r > 0:
                    stack.append((r-1, c))
                if c > 0:
                    stack.append((r, c-1))
                if r < self.rows-1:
                    stack.append((r+1, c))
                if c < self.cols-1:
                    stack.append((r, c+1))

    def __str__(self):
        # generate header
        header = "\t"
        for i in range(self.cols):
            header += str(i) + "\t"
        # generate board
        board = []
        for row_index, row in enumerate(self.board):
            row_str = f"{row_index} \t"
            for cell in row:
                if not cell.is_revealed:
                    row_str += "-\t"
                elif cell.is_mine:
                    row_str += "X\t"
                else:
                    row_str += str(cell.adjacent_mines) + "\t"
            board.append(row_str)
        return header + "\n" + "\n".join(board)
    
    def is_win(self):
        return self.num_revealed == self.rows*self.cols - self.num_mines and not self.game_over


rows = int(input("Ingrese el número de filas: "))
cols = int(input("Ingrese el número de columnas: "))
mines = int(input("Ingrese el número de minas: "))


board = Minesweeper(rows, cols, mines)
board.initialize_board()


while (board.game_over is False or board.is_win()):
    row = int(input("Ingrese el número de la fila de la casilla a revelar: "))
    col = int(input("Ingrese el número de la columna de la casilla a revelar: "))
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
