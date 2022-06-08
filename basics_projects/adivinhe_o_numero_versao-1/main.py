import functions
import os
from time import sleep

# Create a function that draws a value between 0 and 9

while True:
    # If the user wants, he can change these values

    while True:
        try:
            condition = functions.user_condition('\nDeseja escolher entre quais números quer adivinhar? [Sim / Não] ')
            if condition == 's':
                value = functions.value_random(input('Primeiro valor: '), input('Último valor: '))
                if value == ValueError:
                    print('Responda com um número. Letras e/ou outros algarismos não são aceitos. Tente novamente.')
                else:
                    break 
            elif condition == 'n':
                value = functions.value_random()
                os.system('clear')
                break
            else:
                print('Não consegui entender. Por favor, responda com "Sim" ou "Não".')
        except IndexError:
            print('Você não digitou nada. Tente novamente.')
    if condition == 'n':
        print('\n[Por padrão, o computador sorteou um valor entre 0 e 9.]')
    else:
        pass

    while True:
        # Ask what value the user thinks it is

        answer = functions.user_answer('Qual valor você acha que o computador sorteou? ', int)
        if answer == value:
            os.system('clear')
            print(f'Você acertou, o computador pensou no número {value}')
            sleep(4)
            os.system('clear')
            break
        elif answer != ValueError:
            print(f'\nNão foi dessa vez, seu número foi {answer} e o número do computador foi {value}.')
            sleep(4)
            os.system('clear')
            break
        elif answer == ValueError:
            print('Você não digitou um número. Tente novamente.')

    while True:
        # Ask if the user want to play again

        try:
            game_again = functions.user_condition('Quer jogar de novo? [Sim / Não] ')
            if game_again == 's':
                break
            elif game_again == 'n':
                break
            else:
                print('Não consegui entender. Por favor, responda com "Sim" ou "Não".')
        except IndexError:
            print('Você não digitou nada. Tente de novo.')
            os.system('clear')
        os.system('clear')
    if game_again == 'n':
        break

print('\n== Programa Encerrado. ==\n')