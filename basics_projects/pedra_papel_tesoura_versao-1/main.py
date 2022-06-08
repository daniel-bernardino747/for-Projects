from decimal import DivisionByZero
from random import choice
import functions
import os
from time import sleep

while True:
    victory = list()
    defeat = list()
    draw = list()
    while True:
        # The computer choosing rock, paper or scissors.

        jokenpo = ['Pedra', 'Papel', 'Tesoura']
        computa_choice = choice(jokenpo)
        
        # Asking what the user will choose.

        user_choice = functions.menu_principal('Pedra','Papel','Tesoura', title='JOKENPO', exit='Ver resultado completo', 
                                                question='Digite sua escolha: ')
        os.system('clear')

        # result record

        if user_choice == 0: # Sair
            break

        elif user_choice == 1: # Pedra
            if computa_choice == 'Pedra':
                functions.game_counter(victory, draw, defeat, 0)
            elif computa_choice == 'Papel':
                functions.game_counter(victory, draw, defeat, -1)
            elif computa_choice == 'Tesoura':
                functions.game_counter(victory, draw, defeat, 1)

        elif user_choice == 2: # Papel
            if computa_choice == 'Pedra':
                functions.game_counter(victory, draw, defeat, 1)
            elif computa_choice == 'Papel':
                functions.game_counter(victory, draw, defeat, 0)
            elif computa_choice == 'Tesoura':
                functions.game_counter(victory, draw, defeat, -1)

        elif user_choice == 3: # Tesoura
            if computa_choice == 'Pedra':
                functions.game_counter(victory, draw, defeat, -1)
            elif computa_choice == 'Papel':
                functions.game_counter(victory, draw, defeat, 1)
            elif computa_choice == 'Tesoura':
                functions.game_counter(victory, draw, defeat, 0)

    # Results
    functions.table_lists(victory, draw, defeat, table_names=('Vitória', 'Empate', 'Derrota'))
    tot_vict = tot_draw = tot_defeat = 0
    for i, v in enumerate(victory):
        tot_vict += v
    for i, v in enumerate(draw):
        tot_draw += v
    for i, v in enumerate(defeat):
        tot_defeat += v
    sleep(1)

    try:
        print(f'Total de Vitórias: {tot_vict} ({(tot_vict / len(victory))*100:.2f}%)')
        print(f'Total de Empates: {tot_draw} ({(tot_draw / len(draw))*100:.2f}%)')
        print(f'Total de Derrotas: {tot_defeat} ({(tot_defeat / len(defeat))*100:.2f}%)')
    except ZeroDivisionError:
        print('Não tivemos nenhum jogo.')
    print('='*50)
    sleep(2)

    if tot_vict > tot_defeat:
        winner = 'Você (Parabéns!!)'
    elif tot_vict < tot_defeat:
        winner = 'Computador (Quem sabe numa próxima vez.)'
    try:
        print(f'O ganhador foi: {winner}')
    except NameError:
        print('Não tivemos nenhum ganhador.')

    while True:
        exit = str(input('\nDeseja continuar o programa? [Sim / Não] ')).strip().lower()[0]
        if exit == 's':
            break
        elif exit == 'n':
            break
        else:
            os.system('clear')
            print('Eu não entendi. Tente de novo.')
    if exit == 'n':
        break

os.system('clear')
print('== Programa encerrado ==')
