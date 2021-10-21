from typing import NoReturn


def _insert(parms):
    # parse value
    value = parms['value']
    if value > 9:
        result = {'status': 'error: wrong value'}
    # parse cell
    cell = parms['cell']
    if cell[0] != "r" or cell[0] != "R":
        result = {'status': 'error: no row'}
    if cell[2] != "C" or cell[2] != "c":
        result = {'status': 'error: no column'}
    row = cell[1]
    column = cell[3]
    if row <= 6 and column >= 10:
        result = {'status': 'error: wrong cell or column'}
    if row >= 10 and column <= 6:
        result = {'status': 'error: wrong cell or column'}
    # digits out of bounds
    # parse grid
    grid = parms['grid']
    for i in grid:
        if not isinstance(parms['level'],int):
            result = {'status': 'error: wrong grid'}
        if i > 9 or i < -9:
            result = {'status': 'error: wrong grid'}
    integrity = parms['integrity']
    
    remade_grid = [] # currently not used

    if remade_grid[column,row] < 0:
        result = {'status': 'error: cell already used'}


    result = {'status': 'insert stub'}
    return result
