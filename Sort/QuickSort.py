from copy import deepcopy
from .Data import Data
import random

def QuickSort_Normal(Dataset, visual = True):
    '''initial the frame'''
    #FRMAE START
    frame = None
    if visual:
        frame = [Dataset]
    #FRAME END
    ds = deepcopy(Dataset)
    QSort(ds, 0, Data.DataCount - 1, frame)
    #FRAME START
    if visual:
        frame.append(deepcopy(ds))
    return frame
    #FRAME END

def QuickSort_3Way(Dataset, visual = True):
    '''initial the frame'''
    #FRAME START
    frame = None
    if visual:
        frame = [Dataset]
    #FRAME END
    ds = deepcopy(Dataset)
    QSortTR(ds, 0, Data.DataCount - 1, frame) #call the recursion funciton
    #FRAME START
    if visual:
        frame.append(deepcopy(ds))
    return frame
    #FRAME END

def QSort(ds, left, right, frame = None):
    '''normal quicksort function'''
    if right - left < 1:
        return
    #FRAME START
    if frame:
        for i in range(left, right+1):
            ds[i].SetColor('b')
    #FRAME END
    pivot = ds[left].value
    l, r = left, right
    while l < r:
        while l < r and ds[r].value >= pivot:
            #FRAME START
            if frame:
                frame.append(deepcopy(ds))
                frame[-1][l].SetColor('r')
                frame[-1][r].SetColor('k')
            #FRAME END
            r -= 1
        ds[l].value = ds[r].value
        while l < r and ds[l].value < pivot:
            #FRAME START
            if frame:
                frame.append(deepcopy(ds))
                frame[-1][l].SetColor('r')
                frame[-1][r].SetColor('k')
            #FRAME END
            l += 1
        ds[r].value = ds[l].value
    ds[l].value = pivot
    #FRAME START
    if frame:
        for i in range(left, right+1):
            ds[i].SetColor()
    #FRAME END
    QSort(ds, left, l - 1, frame)
    QSort(ds, l + 1, right, frame)

def QSortTR(ds, left, right, frame = None):
    '''threeroad quicksort function'''
    if right - left < 1:
        return
    for i in range(left, right + 1):
        ds[i].SetColor('b')
    pivot = ds[random.randint(left, right)].value
    i = left #the first element index after the last element with value equal to the pivot
    j = left #the last element arg with value less than the pivot
    k = right + 1 #the first element arg with value larger than the pivot
    while i < k:
        #FRAME START
        if frame:
            frame.append(deepcopy(ds))
            frame[-1][i].SetColor('r')
            frame[-1][j].SetColor('k')
            frame[-1][k-1].SetColor('g')
        #FRAME END
        if ds[i].value < pivot:
            ds[i], ds[j] = ds[j], ds[i]
            i += 1
            j += 1
        elif ds[i].value > pivot:
            ds[i], ds[k-1] = ds[k-1], ds[i]
            k -= 1
        else:
            i += 1
    #FRAME START
    if frame:
        for i in range(left, right + 1):
            ds[i].SetColor()
    #FRAME END
    QSortTR(ds, left, j, frame)
    QSortTR(ds, k, right, frame)