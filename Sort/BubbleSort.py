from copy import deepcopy
from .Data import Data

def BubbleSort(Dataset, visual = True):
    '''bubblesort function'''
    #FRAME START
    frame = None
    if visual:
        frame = [Dataset]
    #FRAME END
    ds = deepcopy(Dataset)
    for i in range(Data.DataCount):
        flag = False
        for j in range(Data.DataCount - i - 1):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j]
                flag = True
            #FRAME START
            if visual:
                frame.append(deepcopy(ds)) #save the data list now after every comparation
                frame[-1][j+1].SetColor('r')
            #FRAME END
        if not flag:
            break
    if visual:
        frame.append(ds) #save the final sorted data list
    return frame
            