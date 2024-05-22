from copy import deepcopy
from .Data import Data

def MergeSort(dataset, visual = True):
    '''mergesort port function'''
    #FRMAE START
    frames = None
    if visual:
        frames = [dataset]
    #FRAME END
    ds = deepcopy(dataset)
    Msort(ds, 0, Data.DataCount - 1, frames)
    #FRAME START
    if visual:
        frames.append(deepcopy(ds))
    return frames
    #FRAME END

def Msort(dataset, start, end, frames = None):
    '''the real mergesort function'''
    mid = start + int((end - start) >> 1)
    if end - start > 1:
        Msort(dataset, start, mid, frames)
        Msort(dataset, mid + 1, end, frames)
    #FRAME START
    if frames:
        ds_tmp = deepcopy(dataset)
        for i in range(start, mid + 1):
            ds_tmp[i].SetColor('y')
        for i in range(mid + 1, end + 1):
            ds_tmp[i].SetColor('b')
    #FRAME END
    left, right = start, mid + 1
    n = end - start + 1
    list_tmp = []
    for i in range(n):
        if right > end or (left <= mid and dataset[left].value <= dataset[right].value):
            list_tmp.append(dataset[left])
            id_setcolor = left
            left += 1
        else:
            list_tmp.append(dataset[right])
            id_setcolor = right
            right += 1
        #FRAME BEGIN
        if frames:
            frames.append(deepcopy(ds_tmp))
            frames[-1][id_setcolor].SetColor('r')
        #FRAME END
    for i in range(n):
        dataset[start + i] = list_tmp[i]
    #FRAME BEGIN
    if frames:
        frames.append(deepcopy(dataset))
    #FRAME END