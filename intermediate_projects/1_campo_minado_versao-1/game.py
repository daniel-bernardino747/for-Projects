import random
import copy

# criar o campo minado
class minesweeper():
    def __init__(self):
        self.real_camp = self.make_camp()
        self.bombs = self.make_bomb()
    
    @staticmethod
    def make_camp():
        return [[0 for _ in range(8)] for i in range(8)]
    
    def print_camp(self, camp):
        for i in range(8):
            if i == 0:
                print(f'\n      1   2   3   4   5   6   7   8  \n   ', '-'*33)
            print(f' {i}  |', end='')
            for a in camp[i]:
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
    
    def danger_zone(self, camp):
        for i in range(8):
            for a, v in enumerate(camp[i]):
                if v == '+':
                    if not a == 0:
                        if camp[i][a-1] != '+':
                            camp[i][a-1] += 1
                    if not a == 7:
                        if camp[i][a+1] != '+':
                            camp[i][a+1] += 1
                    if not i == 0:
                        if camp[i-1][a] != '+':
                            camp[i-1][a] += 1
                        if camp[i-1][a-1] != '+':
                            camp[i-1][a-1] += 1
                        if not a == 7:
                            if camp[i-1][a+1] != '+':
                                camp[i-1][a+1] += 1
                    if not i == 7:
                        if camp[i+1][a] != '+':
                            camp[i+1][a] += 1
                        if camp[i+1][a-1] != '+':
                            camp[i+1][a-1] += 1
                        if not a == 7:
                            if camp[i+1][a+1] != '+':
                                camp[i+1][a+1] += 1
                    
    def player_camp(self, original):
        player_camp = copy.deepcopy(original)
        for i in range(8):
            for a, v in enumerate(original[i]):
                if original[i][a] == 0:
                    player_camp[i][a] = 0
        return player_camp
    
    def show_game(self, camp, row, column):
        camp[row][column] = '*'
        

def play(game, print_game=True):
    if print_game:
        game.set_bombs()
        game.danger_zone(game.real_camp)
        a = input('Digite as coordenadas: [linha, coluna] ')
        row, col = int(a[0]), int(a[-1])
        game.show_game(game.real_camp, row, col)
        fake = game.player_camp(game.real_camp)
        game.print_camp(fake)
        game.print_camp(game.real_camp)



# sortear as bombas dentro do campo minado
# inserir o espaço que usuário quer selecionar
# conferir bombas próximas 
# se selecionar uma bomba, mostrar todos as bombas e acabar o game


if __name__ == '__main__':
    game = minesweeper()
    play(game)
