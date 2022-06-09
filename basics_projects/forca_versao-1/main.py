from random import choice

with open(r'C:\Users\Daniel.DESKTOPDAN\principal_tools\Documents\For_Python\basics_projects\forca_versao-1\Lista-de-Palavras.txt', 'r') as arquivo:
    arq = arquivo.readlines()
print(choice(arq))