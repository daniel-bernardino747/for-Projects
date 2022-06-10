from os import system

def hangman(word):
    system('clear')
    lives = 6
    used_letters = list()
    letters = set(word)
    normal_letters = list(word)
    unnamed = [i.replace(f'{i}', '_') for i in word]
    print('Adivinhe a palavra abaixo:')
    while True:
        print(f'Você tem {lives} vidas.\n')
        for a in unnamed:
            print(a, end=' ')
        if not used_letters == list():
            print(f'\n\nLetras usadas:', end=' ')
            for m in used_letters:
                print(m, end= ' ')
        user_letter = str(input('\nDigite uma letra: ')).upper()
        used_letters.append(user_letter)
        if user_letter in word:
            unnamed = [user_letter if value == user_letter else unnamed[index] for index, value in enumerate(normal_letters)]
            letters.remove(user_letter)
            system('clear')
            print('\nVocê achou uma letra.')
        elif user_letter == '0':
            break
        else:
            lives -= 1
            system('clear')
            print('Errou')
        if lives == 0:
            system('clear')
            print(f'Você perdeu todas as suas vidas. A palavra era: {word}')
            break

if __name__ == '__main__':
    print('== Testes ==')