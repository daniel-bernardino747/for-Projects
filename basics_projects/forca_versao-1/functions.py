from os import system

def hangman(word):
    system('clear')
    lives = 6
    letters = set(word)
    normal_letters = list(word)
    unnamed = [i.replace(f'{i}', '_') for i in word]
    print('Adivinhe a palavra abaixo:')
    while True:
        print(f'Você tem {lives} vidas.\n')
        for a in unnamed:
            print(a, end=' ')
        user_letter = str(input('\nDigite uma letra: ')).upper()
        if user_letter in word:
            """for index, value in enumerate(normal_letters):
                if user_letter == value:
                    unnamed[index] = user_letter
                else:
                    unnamed[index] = unnamed[index]"""
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