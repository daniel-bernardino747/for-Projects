import functions

# Create a function that draws a value between 0 and 9

# If the user wants, he can change these values
ans = functions.user_condition('Deseja escolher entre quais números quer adivinhar? [Sim / Não] ')
if ans == 's':
    value = functions.value_random(input('Primeiro valor: '), input('Último valor: '))
elif ans == 'n':
    value = functions.value_random()
else:
    print('Não consegui entender. Por favor, responda com "Sim" ou "Não".')
print(value)
# Ask what value the user thinks it is
# Ask if you want to play again