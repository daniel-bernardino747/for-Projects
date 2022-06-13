from os import system
from game import TicTacToe, play, user_condition
from players import ComputerPlayer, HumanPlayer, IAPlayer

x_wins = o_wins = ties = 0
system('clear')
while True:
    IA_or_Not = input('Testar IA com Computador? [Sim / Não] ').upper().strip()[0]
    
    if IA_or_Not == 'N':
        while True:
                user_choice = user_condition('Quer jogar com X ou O? [X / O] ')
                if user_choice == 'x':
                    user_player = HumanPlayer('X')
                    computer_player = IAPlayer('O')
                    break
                elif user_choice == 'o':
                    user_player = HumanPlayer('O')
                    computer_player = IAPlayer('X')
                    break
                else:
                    print('Eu não entendi. Tente novamente.')
    
        t = TicTacToe()
        play(t, user_player, computer_player)

    if IA_or_Not == 'S':
        for i in range(100):
            IA_player = IAPlayer('O')
            computer_player = ComputerPlayer('X')
            t = TicTacToe()
            result = play(t, computer_player, IA_player, print_game=False)
            if result == 'X':
                x_wins += 1
            elif result == 'O':
                o_wins += 1
            else:
                ties += 1
        print(f'Em 100 jogos da velha, o Computador ganhou {x_wins}, a IA ganhou {o_wins} e tivemos {ties} empates.')
        break
