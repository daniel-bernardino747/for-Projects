# criar o campo minado
class minesweeper():
    def __init__(self):
        self.camp = self.make_camp()
    
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

def play(game, print_game=True):
    if print_game:
        game.print_camp()




# sortear as bombas dentro do campo minado
# inserir o espaço que usuário quer selecionar
# conferir bombas próximas 
# se selecionar uma bomba, mostrar todos as bombas e acabar o game


if __name__ == '__main__':
    game = minesweeper()
    play(game)