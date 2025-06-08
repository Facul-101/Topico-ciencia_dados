from typing import Literal, TypeAlias, Optional
from pilha import Pilha
import math
import os

# Problem/references:
# https://en.wikipedia.org/wiki/Flood_fill
# https://www.geeksforgeeks.org/flood-fill-algorithm/
# https://www.freecodecamp.org/portuguese/news/algoritmo-de-preenchimento-por-inundacao-explicado/

BIN: TypeAlias = Literal['1', '0', 'X']

def get_std_data(swap_value: BIN) -> tuple[list[list[BIN]], tuple[int, int]]:
    with open(os.path.dirname(__file__)+"/input.txt", 'r') as f:
        raw_matrix = [list(l.strip()) for l in f.readlines()]

    for x, line in enumerate(raw_matrix):
        if 'X' in line:
            y = line.index('X')
            break
    else:
        ValueError("No char 'X' in matrix")

    raw_matrix[x][y] = '1' if swap_value == '0' else '0'

    return raw_matrix, (x, y) # type: ignore

def show_matrix(
        matrix: list[list[BIN]], 
        current_pos: Optional[tuple[int, int]], 
        swap_value: Optional[BIN]
    ):
    assert (current_pos is None and swap_value is None) or \
           (isinstance(current_pos, tuple) and swap_value in BIN.__args__)

    if not current_pos is None:
        matrix[current_pos[0]][current_pos[1]] = 'X'

    for line in matrix:
        print(''.join(line).replace('1', ' ').replace('0', '@'))
    print()

    if not current_pos is None and not swap_value is None:
        matrix[current_pos[0]][current_pos[1]] = swap_value

def flood_fill_recursive(
        matrix: list[list[BIN]], 
        target_pos: tuple[int, int],
        swap_value: BIN,
        show_step: int,
        step_count: list[int]
    ) -> None:
    
    x = target_pos[0] # Linhas
    y = target_pos[1] # Colunas


    if x < 0 or x > len(matrix) or y < 0 or y > len(matrix[0]):
        return

    if matrix[x][y] == swap_value:
        return
    
    matrix[x][y] = swap_value
    step_count[0] += 1

    if show_step and step_count[0]%show_step == 0:
        show_matrix(matrix, target_pos, swap_value)
        input("Press ENTER to proceed")
    
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        flood_fill_recursive(matrix, (x + dx, y + dy), swap_value, show_step, step_count)

def flood_fill_loop(
        matrix: list[list[BIN]], 
        target_pos: tuple[int, int],
        swap_value: BIN,
        show_step: int,
    ) -> None:

    start = matrix[target_pos[0]][target_pos[1]]
    if start == swap_value:
        show_matrix(matrix, target_pos, swap_value)
        return
    
    coord_stack = Pilha('i', len(matrix)*len(matrix)*2)
    coord_stack.empilha(target_pos[0]) # Linha  (x)
    coord_stack.empilha(target_pos[1]) # Coluna (y)
    step_count: int = 0

    while not coord_stack.pilha_esta_vazia():

        # ORDEM DE DESEMPILHAMENTO DEVE SER O INVERSO DA ORDEM DE EMPILHAMENTO
        y: int = coord_stack.desempilha() #type: ignore
        x: int = coord_stack.desempilha() #type: ignore
        # print(x, y) # DEBUG

        if x < 0 or x > len(matrix) or y < 0 or y > len(matrix[0]):
            continue

        if matrix[x][y] == swap_value:
            continue

        matrix[x][y] = swap_value
        step_count += 1

        if show_step and step_count%show_step == 0:
            show_matrix(matrix, (x, y), swap_value)
            # print(step_count) # DEBUG
            input("Press ENTER to proceed")

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            coord_stack.empilha(x + dx)
            coord_stack.empilha(y + dy)

if __name__ == "__main__":
    swap_value = '0'
    matrix, target = get_std_data(swap_value)
    # flood_fill_recursive(matrix, target, swap_value, 1, [0])
    flood_fill_loop(matrix, target, swap_value, 1)
    show_matrix(matrix, None, None)