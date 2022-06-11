from random import choice
from re import L

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + ', é a sua vez. Escolha a posição (0-8): ')
            try:
                val = int(square)
                pass
            except ValueError:
                print('Posição inválida. Tente novamente.')


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass
