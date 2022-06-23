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
            # step 1.2.1.1: cria variáveis com as linhas e colunas
            # step 1.2.1.2: Se o chute estiver lá, retorna que n é válido
            # step 1.2.1.3: cria os quadros e testa eles
            # step 1.2.1.4: se passar tudo isso, é válido
        # step 1.2.2: se for: muda a posição para seu chute
            # step  1.2.2.1: retorna True
        # step 1.2.3: se não for: deixa -1
    # step 1.3: Se não deu returna False
# step 2: Testa com __name__ = __main__
