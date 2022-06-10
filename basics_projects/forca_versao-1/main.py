from random import choice
from os import system
from functions import hangman, user_condition

with open(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Python\basics_projects\forca_versao-1\Lista-de-Palavras.txt', 'r') as arquivo:
    arq = arquivo.readlines()

while True:
    word = choice(arq).strip('\n').upper()
    # hangman(word)
    exit = 'E'
    while exit not in 'sn':
        exit = user_condition(f'{"=" * 30} \nVamos brincar de novo? [Sim / Não] ', str)
        if exit == 's':
            break
        elif exit == 'n':
            break
        print('Eu não entendi. Responda com "Sim" ou "Não".')
    if exit == 'n':
        break
system('clear')
print('\n== Programa Encerrado ==')