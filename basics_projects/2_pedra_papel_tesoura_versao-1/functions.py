def menu_principal(*options, title='Title' ,exit='Sair do programa', question='Sua escolha: '):

    print(f'{"=" * 30}\n{title:^30}\n{"=" * 30}')
    for i, v in enumerate(options):
        print(f' [{i+1}] {v}')
    print(f' [0] {exit}\n{"=" * 30}')

    try:
        query = int(input(question))
        return query
    except ValueError:
        print('Digite apenas números. Tente novamente.')
        return ValueError
        
def game_counter(list_victory, list_draw, list_defeat, result):
    if result == -1:
        list_victory.append(0)
        list_draw.append(0)
        list_defeat.append(1)
    elif result == 0:
        list_victory.append(0)
        list_draw.append(1)
        list_defeat.append(0)
    if result == 1:
        list_victory.append(1)
        list_draw.append(0)
        list_defeat.append(0)

def table_lists(*list, title='TABELA DOS JOGOS', table_names):
    print("="*50)
    print(f'{title:^50}')
    print("="*50)
    print(f'{"Jogos":>9} | ', end='')
    for i in range(0, len(list[0])):
        print(i+1, end='    ')
    print(f'\n{"-"*10} {"-----"*len(list[0])}')
    for a, b in enumerate(list):
        print(f'{table_names[a]:>9} | ', end='')
        for i in b:
            print(i, end='    ')
        print()
    print(f'{"-"*10} {"-----"*len(list[0])}')
    print("="*50)

if __name__ == '__main__':
    # a = menu_principal('Pedra', 'Papel', 'Tesoura', title='JOKENPO')
    # print(a)
    vict = list()
    draw = list()
    defeat = list()
    game_counter(vict, draw, defeat, 0)
    print(vict, draw, defeat)