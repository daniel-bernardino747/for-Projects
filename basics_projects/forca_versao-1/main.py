from random import choice
from functions import hangman

with open(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Python\basics_projects\forca_versao-1\Lista-de-Palavras.txt', 'r') as arquivo:
    arq = arquivo.readlines()

word = choice(arq).strip('\n').upper()
hangman(word)