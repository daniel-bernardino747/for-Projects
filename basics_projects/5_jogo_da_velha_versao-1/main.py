from os import system
from game import TicTacToe, play, user_condition
from players import ComputerPlayer, HumanPlayer

system('clear')
while True:
    user_choice = user_condition('Quer jogar com X ou O? [X / O] ')
    if user_choice == 'x':
        user_player = HumanPlayer('X')
        computer_player = ComputerPlayer('O')
        break
    elif user_choice == 'o':
        user_player = HumanPlayer('O')
        computer_player = ComputerPlayer('X')
        break
    else:
        print('Eu não entendi. Tente novamente.')

t = TicTacToe()
play(t, user_player, computer_player)
