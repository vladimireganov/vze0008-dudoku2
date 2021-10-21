from typing import NoReturn


def _insert(parms):
    print(parms)
    # parse value
    if not "value" in parms.keys():
        result = {'status': 'error: missing value'}
        return result
    value = int(parms['value'])
    if value > 9:
        result = {'status': 'error: invalid value'} # fixed
        return result
    if value <= 0:
        result = {'status': 'error: invalid value'} # fixed
        return result
    # parse cell
    if not "cell" in parms.keys():
        result = {'status': 'error: no cell specified'}
        return result
    cell = parms['cell']
    if cell[0] != "r" and cell[0] != "R":
        result = {'status': 'error: missing cell reference'}# fixed
        return result
    if cell[2] != "C" and cell[2] != "c":
        result = {'status': 'error: missing cell reference'}# fixed
        return result
    row = int(cell[1])
    column = int(cell[3])
    if row <= 6 and column >= 10:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if row >= 10 and column <= 6:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    # digits out of bounds
    # parse grid
    if not "grid" in parms.keys():
        result = {'status': 'error: no grid specified'}
        return result
    grid = parms['grid']
    for i in grid:
        if (int(i) > 9 or int(i) < -9):
            result = {'status': 'error: wrong grid'}
            return result
    if not "integrity" in parms.keys():
        result = {'status': 'error: no integrity specified'}
        return result
    integrity = parms['integrity']
    
    remade_grid = [] # currently not used

    # if remade_grid[column,row] < 0:
    #     result = {'status': 'error: cell already used'}
    #     return result


    result = {'status': 'ok','grid':grid,'integrity':integrity}
    return result
