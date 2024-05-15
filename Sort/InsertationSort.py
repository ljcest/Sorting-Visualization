from copy import deepcopy
from .Data import Data

def InsertationSort(Dataset):
    # initial the frame
    frame = [Dataset]
    ds = deepcopy(Dataset)

    for i in range(1, Data.DataCount):
        frame.append(deepcopy(ds))
        frame[-1][i].SetColor('r')
        for j in range(i - 1, -1, -1): #from the tail to the top
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j]
                frame.append(deepcopy(ds))
                frame[-1][j].SetColor('k')
            else:
                break
    frame.append(deepcopy(ds))
    return frame
