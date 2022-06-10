from os import system

def user_condition(question, category=str):
    while True:
        try:
            query = category(input(question)).strip().lower()[0]
        except IndexError:
            print('Você não digitou nada.')
        else:
            break
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
            while True:
                try:
                    user_letter = str(input('\nDigite uma letra: ')).upper().strip()[0]
                except IndexError:
                    print('É preciso digitar uma letra. Tente de novo.')
                    continue
                else:
                    break
            if user_letter in used_letters:
                print(f'Você já adicionou a letra {user_letter}, tente outra.')
            elif user_letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-':
                print('Você não digitou uma letra válida. Tente de novo.')
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
                print('Você achou uma letra da palavra.')
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