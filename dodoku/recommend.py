from typing import NoReturn
from matplotlib.pyplot import grid

def _recommend(parms):
    # result = {'status': 'recommend stub'}
    # cell , grid , integrity
    if not "cell" in parms.keys():
        result = {'status': 'error: missing cell'}# fixed
        return result
    if not "grid" in parms.keys():
        result = {'status': 'error: missing grid'}# fixed
        return result
    if not "integrity" in parms.keys():
        result = {'status': 'error: missing integrity'}# fixed
        return result
    # cell = 
    row = 0
    column = 0
    if not isinstance(parms['cell'],str):
        return {'status': 'error: cell input is not string'}
        
    cell = parms['cell']
    grid = parms['grid']
    
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
        if len(cell) == 4:
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
        
    suggest = []
    
    if row <= 6:
        #print((row-1)*9 + column-1)
        if grid[(row-1)*9 + column-1] != 0:
            suggest = []
            result = {'status': 'ok','recommendation':suggest}
            return result
            
    #54 - 54 + 45 handle as 15 by 3
    if row > 6 and row <= 10:
        #print(54+(row-1-6)*9 + column-1)
        if grid[54+(row-1-6)*15 + column-1] != 0:
            suggest = []
            result = {'status': 'ok','recommendation':suggest}
        
            return result
    #54+45 - rest as 9 by 6
    
    if row > 10:
        #print(54+45+(row-1-9)*9 + column-1-6)
        if grid[54+45+(row-1-9)*9 + column-1-6] != 0:
            suggest = []
            result = {'status': 'ok','recommendation':suggest}
        
            return result
    # x = (column -1 ) // 3
    # y = (row -1) // 3
    used = []
    # if grid[x + y ]
    
    

    result = {'status': 'ok','recommendation':suggest}
    return result
