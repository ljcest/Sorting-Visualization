from copy import deepcopy
from .Data import Data

def SelectionSort(Dataset, visual = True):
    #initial the frame
    #FRAME START
    frame = None
    if visual:
        frame = [Dataset]
    #FRAME END
    ds = deepcopy(Dataset)
    for i in range(Data.DataCount):
        tmp = i
        for j in range(i, Data.DataCount):
            #FRAME START
            if visual:
                frame.append(deepcopy(ds))
                frame[-1][i].SetColor('r')
                frame[-1][j].SetColor('k')
            #FRAME END
            if ds[tmp].value > ds[j].value:
                tmp = j
        ds[tmp], ds[i] = ds[i], ds[tmp]
    #FRAME START
    if visual:
        frame.append(deepcopy(ds))
    return frame
    #FRAME END
