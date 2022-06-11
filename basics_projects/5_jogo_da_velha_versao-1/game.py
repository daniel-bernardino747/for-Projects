import math
from re import X
from players import HumanPlayer, ComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for i in range(3):
            for row in self.board[i*3: (i+1)*3]:
                print('| ' + row, end=' ')
            print('|')
            if not i == 2:
                print('-' * 13)
    
    @staticmethod
    def print_board_nums():
        board = [str(num) for num in range(9)]
        for i in range(3):
            for row in board[i*3: (i+1)*3]:
                print('| ' + row, end=' ')
            print('|')
            if not i == 2:
                print('-' * 13)
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_index = math.floor(square / 3)
        row = self.board[row_index*3: (row_index+1)*3]
        if all(s == letter for s in row):
            return True
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False
        
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == ' ']

def play(game, x_player, o_player, print_game=True):

    if print_game:
        print('\nAs posições são:\n')
        game.print_board_nums()
        print()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + f' fez a jogada no espaço {square}.\n')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' ganhou!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print('Deu empate.')


if __name__ == '__main__':
    x_player = ComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)