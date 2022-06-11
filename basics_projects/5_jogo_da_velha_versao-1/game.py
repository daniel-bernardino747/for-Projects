from cmath import e


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
    
    @staticmethod
    def print_board_nums():
        board = [str(_) for _ in range(9)]
        for i in range(3):
            for row in board[i*3: (i+1)*3]:
                print('| ' + row, end=' ')
            print('|')
            print('-' * 24)



if __name__ == '__main__':
    board = [' ' for _ in range(9)]
    for i in range(3):
        for row in board[i*3: (i+1)*3]:
            print('| ' + row, end=' ')
        print('|')
        if not i == 2:
            print('-' * 13)