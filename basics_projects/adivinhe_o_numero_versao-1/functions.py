from random import randint

def user_answer(answer):
    question = str(input(answer)).strip().lower()[0]
    return question

def value_random(first=0, last=9):
    try:
        num1 = int(first)
        num2 = int(last)
        if num1 < num2:
            value = randint(num1, num2)
        else:
            value = randint(num2, num1)
    except ValueError:
        return 'Responda com um número, letras e outros algarismos não são aceitos. Tente novamente.'
    return value


if __name__ == '__main__':
    print(value_random(input('Primeiro valor: '), input('Segundo valor: ')))