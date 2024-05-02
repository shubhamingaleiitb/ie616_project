class Game:
    def __init__(self, board_size=8, num_stones=5):
        self.board_size = board_size
        self.num_stones = num_stones
        self.board = [['.' for _ in range(board_size)] for _ in range(board_size)]
        self.players = ['W', 'B']
        self.current_player = 0

        # Place the stones for the players
        for i in range(num_stones):
            self.board[4][i+2] = 'W'
            self.board[3][i+2] = 'B'

    def print_board(self):
        print(' ', ' '.join(chr(ord('A') + i) for i in range(self.board_size)))
        for i, row in enumerate(self.board):
            print(self.board_size - i, ' '.join(row))
        print()

    def get_moves(self):
        moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == self.players[self.current_player]:
                    if i > 0 and self.board[i-1][j] == '.':
                        moves.append((i, j, i-1, j))
                    if i < self.board_size-1 and self.board[i+1][j] == '.':
                        moves.append((i, j, i+1, j))
                    if j > 0 and self.board[i][j-1] == '.':
                        moves.append((i, j, i, j-1))
                    if j < self.board_size-1 and self.board[i][j+1] == '.':
                        moves.append((i, j, i, j+1))
        return moves

    def make_move(self, move):
        i, j, new_i, new_j = move
        self.board[i][j] = 'P'
        self.board[new_i][new_j] = self.players[self.current_player]
        self.current_player = 1 - self.current_player

    def convert_input(self, input_str):
        # Convert a string like "E4" into row and column indices
        col_str, row_str = input_str[0], input_str[1:]
        col = ord(col_str.upper()) - ord('A')
        row = self.board_size - int(row_str)
        return row, col        

    def play(self):
        while True:
            self.print_board()
            moves = self.get_moves()
            if not moves:
                print(f"Player {self.players[1 - self.current_player]} wins!")
                break
            print(f"Player {self.players[self.current_player]}, please enter your move:")
            move = None
            while move not in moves:
                try:
                    input_str = input().split()
                    move = self.convert_input(input_str[0]) + self.convert_input(input_str[1])
                except (ValueError, IndexError):
                    print("Invalid input. Please enter your move as two positions separated by a space (e.g., 'E4 E3').")
            print(f"Player {self.players[self.current_player]} moves from {move[:2]} to {move[2:]}")
            self.make_move(move)

game = Game()
game.play()
