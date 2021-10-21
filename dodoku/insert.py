from typing import NoReturn


def _insert(parms):
    print(parms)
    # parse value
    if not "value" in parms.keys():
        result = {'status': 'error: missing value'}# fixed
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
        result = {'status': 'error: missing cell reference'} # fixed
        return result
    if not "integrity" in parms.keys():
        result = {'status': 'error: missing integrity'}# fixed
        return result
    integrity = parms['integrity']
    if not "grid" in parms.keys():
        result = {'status': 'error: missing grid'}# fixed
        return result
    grid = parms['grid']
    
    cell = parms['cell']
    if (cell[0] != "r" and cell[0] != "R"):
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if (cell[2] != "C" and cell[2] != "c") and (cell[3] != "C" and cell[3] != "c"):
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if cell[2] == "C" or cell[2] == "c":
        row = int(cell[1])
        if len(cell)==4:
            column = int(cell[3])
        else:
            column = int(cell[3:4])
        print(row,column)
    else:
        row = int(cell[1:2])
        if len(cell)==5:
            column = int(cell[4])
        else:
            column = int(cell[4:5])
        
        print(row,column)
    
    if row <= 6 and column >= 10:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if row >= 10 and column <= 6:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    # digits out of bounds
    # parse grid
    
    for i in grid:
        if not isinstance(i,int):
            result = {'status': 'error: invalid grid'}# fixed
            return result
        if (int(i) > 9 or int(i) < -9):
            result = {'status': 'error: invalid grid'}# fixed
            return result
    
    
    remade_grid = grid # currently not used
    print(len(grid))
    #first 54 handle as 9 by 6 
    if row <= 6:
        print((row-1)*9 + column-1)
        if grid[(row-1)*9 + column-1] < 0:
            result = {'status': 'error: attempt to change fixed hint'}# fixed
            return result
    #54 - 54 + 45 handle as 15 by 3
    if row > 6 and row <= 10:
        print(53+(row-1)*9 + column-1)
        if grid[53+(row-1)*15 + column-1] < 0:
            result = {'status': 'error: attempt to change fixed hint'}# fixed
            return result
    #54+45 - rest as 9 by 6
    
    if row > 10:
        print(53+45+(row-1)*9 + column-1)
        if grid[53+45+(row-1)*9 + column-1] < 0:
            
            result = {'status': 'error: attempt to change fixed hint'}# fixed
            return result
    # if remade_grid[column,row] < 0:
    #     result = {'status': 'error: cell already used'}
    #     return result


    result = {'status': 'ok','grid':remade_grid,'integrity':integrity}
    return result
