from random import randint

def user_answer(question, category=str):
    try:
        query = category(input(question))
        return query
    except ValueError:
        return ValueError

def user_condition(question):
    query = str(input(question)).strip().lower()[0]
    return query

def value_random(first=0, last=9):
    try:
        num1 = int(first)
        num2 = int(last)
    except ValueError:
        return ValueError
    if num1 < num2:
        value = randint(num1, num2)
    else:
        value = randint(num2, num1)
    return value

if __name__ == '__main__':
    a = value_random(input('Primeiro valor: '), input('Segundo valor: '))
    if a == ValueError:
        print('eerouuuu')