from copy import deepcopy
from .Data import Data

def SelectionSort(Dataset):
    #initial the frame
    frame = [Dataset]
    ds = deepcopy(Dataset)
    for i in range(Data.DataCount):
        tmp = i
        for j in range(i, Data.DataCount):
            frame.append(deepcopy(ds))
            frame[-1][i].SetColor('r')
            frame[-1][j].SetColor('k')
            if ds[tmp].value > ds[j].value:
                tmp = j
        ds[tmp], ds[i] = ds[i], ds[tmp]
    frame.append(deepcopy(ds))
    return frame
