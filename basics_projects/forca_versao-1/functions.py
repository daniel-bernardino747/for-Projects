from os import system

def user_condition(question, category=str):
    query = category(input(question)).strip().lower()[0]
    return query

def hangman(word):
    system('clear')
    lives = 6
    used_letters = list()
    letters = set(word)
    normal_letters = list(word)
    unnamed = [i.replace(f'{i}', '_') for i in word]
    print('Adivinhe a palavra abaixo:')
    while True:
        if letters == set():
            print(f'O jogo acabou, você descobriu a palavra {word}. Parabéns!')
            break
        print(f'Você tem {lives} vidas.\n')
        for a in unnamed:
            print(a, end=' ')
        if not used_letters == list():
            print(f'\n\nLetras usadas:', end=' ')
            for m in used_letters:
                print(m, end= ' ')
        while True:
            user_letter = str(input('\nDigite uma letra: ')).upper()
            if user_letter in used_letters:
                print(f'Você já adicionou a letra {user_letter}, tente outra.')
            else:
                break
        used_letters.append(user_letter)
        if user_letter in word:
            unnamed = [user_letter if value == user_letter else unnamed[index] for index, value in enumerate(normal_letters)]
            letters.remove(user_letter)
            system('clear')
            if letters == set():
                print('Você achou a última letra.')
            else:
                print('\nVocê achou uma letra da palavra.')
        elif user_letter == '0':
            break
        else:
            lives -= 1
            system('clear')
            print(f'A letra {user_letter} não está na palavra, perdeu uma vida.')
        if lives == 0:
            system('clear')
            print(f'Você perdeu todas as suas vidas. A palavra era: {word}')
            break

if __name__ == '__main__':
    print('== Testes ==')