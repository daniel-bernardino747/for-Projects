from pprint import pprint

def find_first_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):

    # step 1.2.1.1: cria variáveis com as linhas e colunas
    row_valid = puzzle[row]
    if guess in row_valid:
        # step 1.2.1.2: Se o chute estiver lá, retorna que n é válido
        return False

    col_valid = [puzzle[i][col] for i in range(9)]
    if guess in col_valid:
        return False
    
    # step 1.2.1.3: cria os quadrados e testa eles
    square_in_row = (row // 3) * 3
    square_in_col = (col // 3) * 3

    for r in range(square_in_row, square_in_row + 3):
        for c in range(square_in_col, square_in_col + 3):
            if puzzle[r][c] == guess:
                return False
    
    # step 1.2.1.4: se passar tudo isso, é válid
    return True



# step 1: function resolvedor_sudoku(desafio):
def solver_sudoku(puzzle):

    # step 1.1: encontra o primeiro espaço vazio // sair para caso esteja resolvido
    row, col = find_first_empty(puzzle)

    if row is None:
        return True
    
    # step 1.2: faz o chute
    for guess in range(1, 10):

        # step 1.2.1: confere se esse chute é válido
        if is_valid(puzzle, guess, row, col):
            # step 1.2.2: se for: muda a posição para seu chute
            puzzle[row][col] = guess

            # step  1.2.2.1: retorna True
            if solver_sudoku(puzzle):
                return True
        
        # step 1.2.3: se não for: deixa -1
        puzzle[row][col] = -1
    
    # step 1.3: Se não deu returna False
    return False

# step 2: Testa com __name__ = __main__
if __name__ == '__main__':
    initial_test = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solver_sudoku(initial_test))
    pprint(initial_test)

    test_2 = [
        [-1, 9, -1,   -1, -1, -1,   3, -1, -1],
        [-1, -1, -1,   8, 2, -1,   5, -1, 9],
        [5, 7, 2,   6, 9, -1,   -1, -1, -1],

        [7, 6, 3,   2, 5, 9,   4, 1, -1],
        [-1, 4, -1,   -1, -1, 6,   -1, 3, -1],
        [-1, -1, 9,   -1, 3, -1,   2, -1, -1],

        [-1, -1, -1,   -1, 4, -1,   -1, 5, -1],
        [9, 3, -1,   5, 6, 7,   -1, -1, -1],
        [6, 8, -1,   -1, -1, -1,   -1, 9, 4]
    ]
    print(solver_sudoku(test_2))
    pprint(test_2)
