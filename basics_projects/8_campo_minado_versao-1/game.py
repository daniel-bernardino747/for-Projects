import random

# criar o campo minado
class minesweeper():
    def __init__(self):
        self.camp = self.make_camp()
        self.bombs = self.make_bomb()
    
    @staticmethod
    def make_camp():
        return [[' ' for _ in range(8)] for i in range(8)]
    
    def print_camp(self):
        for i in range(8):
            if i == 0:
                print(f'\n      1   2   3   4   5   6   7   8  \n   ', '-'*33)
            print(f' {i}  |', end='')
            for a in self.camp[i]:
                print(f' {a} |', end='')
            print('\n   ','-'*33)

    @staticmethod
    def make_bomb():
        return '+'
    
    def empty_squares(self):
        num_empty = 0 
        for i in range(8):
            num_empty += self.camp[i].count(' ')
        return num_empty

    def set_bombs(self):
        while self.empty_squares(self) > 54:
            self.camp[random.randint(0, 7)][random.randint(0, 7)] = self.bombs
            

def play(game, print_game=True):
    if print_game:
        game.set_bombs()
        game.print_camp()




# sortear as bombas dentro do campo minado
# inserir o espaço que usuário quer selecionar
# conferir bombas próximas 
# se selecionar uma bomba, mostrar todos as bombas e acabar o game


if __name__ == '__main__':
    game = minesweeper()
    play(game)
