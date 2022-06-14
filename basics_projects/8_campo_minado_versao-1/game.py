import random

# criar o campo minado
class minesweeper():
    def __init__(self):
        self.real_camp = self.make_camp()
        self.bombs = self.make_bomb()
    
    @staticmethod
    def make_camp():
        return [[0 for _ in range(8)] for i in range(8)]
    
    def print_camp(self):
        for i in range(8):
            if i == 0:
                print(f'\n      1   2   3   4   5   6   7   8  \n   ', '-'*33)
            print(f' {i}  |', end='')
            for a in self.real_camp[i]:
                print(f' {a} |', end='')
            print('\n   ','-'*33)

    @staticmethod
    def make_bomb():
        return '+'
    
    def empty_squares(self):
        num_empty = 0 
        for i in range(8):
            num_empty += self.real_camp[i].count(0)
        return num_empty

    def set_bombs(self):
        while self.empty_squares() > 54:
            self.real_camp[random.randint(0, 7)][random.randint(0, 7)] = self.bombs
    
    def danger_zone(self):
        for i in range(8):
            for a, v in enumerate(self.real_camp[i]):
                if v == '+':
                    if not a == 0:
                        if self.real_camp[i][a-1] != '+':
                            self.real_camp[i][a-1] += 1
                    if not a == 7:
                        if self.real_camp[i][a+1] != '+':
                            self.real_camp[i][a+1] += 1
                    if not i == 0:
                        if self.real_camp[i-1][a] != '+':
                            self.real_camp[i-1][a] += 1
                        if self.real_camp[i-1][a-1] != '+':
                            self.real_camp[i-1][a-1] += 1
                        if not a == 7:
                            if self.real_camp[i-1][a+1] != '+':
                                self.real_camp[i-1][a+1] += 1
                    if not i == 7:
                        if self.real_camp[i+1][a] != '+':
                            self.real_camp[i+1][a] += 1
                        if self.real_camp[i+1][a-1] != '+':
                            self.real_camp[i+1][a-1] += 1
                        if not a == 7:
                            if self.real_camp[i+1][a+1] != '+':
                                self.real_camp[i+1][a+1] += 1
                    

            

def play(game, print_game=True):
    if print_game:
        game.set_bombs()
        game.danger_zone()
        game.print_camp()




# sortear as bombas dentro do campo minado
# inserir o espaço que usuário quer selecionar
# conferir bombas próximas 
# se selecionar uma bomba, mostrar todos as bombas e acabar o game


if __name__ == '__main__':
    game = minesweeper()
    play(game)
