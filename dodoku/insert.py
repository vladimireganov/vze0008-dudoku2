from typing import NoReturn


def _insert(parms):
    #print(parms)
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
    if len(cell) > 6:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    
    if (cell[0] != "r" and cell[0] != "R"):
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if (cell[2] != "C" and cell[2] != "c") and (cell[3] != "C" and cell[3] != "c"):
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if cell[2] == "C" or cell[2] == "c":
        if cell[3]<"0" or cell[3] > "9":
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        if cell[1]<"0" or cell[1] > "9":
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        row = int(cell[1])
        if len(cell)==4:
            column = int(cell[3])
        else:
            if cell[4]<"0" or cell[4] > "9":
                result = {'status': 'error: invalid cell reference'}# fixed
                return result
            column = int(cell[3:])
        
    else:
        if cell[1]<"0" or cell[1] > "9":
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        if cell[2]<"0" or cell[2] > "9":
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        if cell[4]<"0" or cell[4] > "9":
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        
            
        row = int(cell[1])*10 + int(cell[2])
        if len(cell) == 5:
            column = int(cell[4])
        elif len(cell) == 6:
            if cell[5]<"0" or cell[5] > "9":
                result = {'status': 'error: invalid cell reference'}# fixed
                return result
            column = int(cell[4:])
        else:
            result = {'status': 'error: invalid cell reference'}# fixed
            return result
        
    
    if row <= 6 and column >= 10:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if row >= 10 and column <= 6:
        result = {'status': 'error: invalid cell reference'}# fixed
        return result
    if row <= 0 or row >15 or column > 15 or column <= 0:
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
    
    #first 54 handle as 9 by 6 
    
    if row <= 6:
        #print((row-1)*9 + column-1)
        if grid[(row-1)*9 + column-1] < 0:
            result = {'status': 'error: attempt to change fixed hint'}
            return result
        else:
            remade_grid[53+(row-1-6)*15 + column-1] = value
    #54 - 54 + 45 handle as 15 by 3
    if row > 6 and row <= 10:
        #print(54+(row-1-6)*9 + column-1)
        if grid[54+(row-1-6)*15 + column-1] < 0:
            result = {'status': 'error: attempt to change fixed hint'}
            return result
        else:
            remade_grid[53+(row-1-6)*15 + column-1] = value
    #54+45 - rest as 9 by 6
    
    if row > 10:
        #print(54+45+(row-1-9)*9 + column-1-6)
        if grid[54+45+(row-1-9)*9 + column-1-6] < 0:
            
            result = {'status': 'error: attempt to change fixed hint'}
            return result
        else:
            remade_grid[53+(row-1-9)*15 + column-1-6] = value
    # if remade_grid[column,row] < 0:
    #     result = {'status': 'error: cell already used'}
    #     return result
    

    result = {'status': 'ok','grid':remade_grid,'integrity':integrity}
    return result
