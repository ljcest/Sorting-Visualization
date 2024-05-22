from copy import deepcopy
from .Data import Data

def InsertationSort(Dataset, visual = True):
    '''insertation sort function'''
    #FRAME START
    frame = None
    if visual:
        frame = [Dataset]
    #FRAME END
    ds = deepcopy(Dataset)

    for i in range(1, Data.DataCount):
        #FRAME START
        if visual:
            frame.append(deepcopy(ds))
            frame[-1][i].SetColor('r')
        #FRAME END
        for j in range(i - 1, -1, -1): #from the tail to the top
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j]
                #FRAME START
                if visual:
                    frame.append(deepcopy(ds))
                    frame[-1][j].SetColor('k')
                #FRAME END
            else:
                break
    #FRAME START
    if visual:
        frame.append(deepcopy(ds))
    #FRAME END
    return frame
