from random import choice
from os import system
from os.path import dirname, join
from functions import hangman, user_condition

file = join(dirname(__file__), 'Lista-de-Palavras.txt')
with open(file, 'r') as f:
    arq = f.readlines()

exit = 'E'
while exit not in 'n':
    word = choice(arq).strip('\n').upper()
    hangman(word)
    exit = user_condition(f'{"=" * 30} \nVamos brincar de novo? [Sim / Não] ', str)
    if exit == 's':
        pass
    elif exit == 'n':
        break
    else:
        print('Eu não entendi. Responda com "Sim" ou "Não".')
system('clear')
print('\n== Programa Encerrado ==')