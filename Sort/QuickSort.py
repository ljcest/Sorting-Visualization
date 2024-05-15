from copy import deepcopy
from .Data import Data
import random

def QuickSort_Normal(Dataset):
    #initial the frame
    frame = [Dataset]
    ds = deepcopy(Dataset)
    QSort(ds, 0, Data.DataCount - 1, frame)
    frame.append(deepcopy(ds))
    return frame

def QuickSort_ThreeRoad(Dataset):
    #initial the frame
    frame = [Dataset]
    ds = deepcopy(Dataset)
    QSortTR(ds, 0, Data.DataCount - 1, frame) #call the recursion funciton
    frame.append(deepcopy(ds))
    return frame

def QSort(ds, left, right, frame):
    if right - left < 1:
        return
    for i in range(left, right+1):
        ds[i].SetColor('b')
    pivot = ds[left].value
    l, r = left, right
    while l < r:
        while l < r and ds[r].value >= pivot:
            frame.append(deepcopy(ds))
            frame[-1][l].SetColor('r')
            frame[-1][r].SetColor('k')
            r -= 1
        ds[l].value = ds[r].value
        while l < r and ds[l].value < pivot:
            frame.append(deepcopy(ds))
            frame[-1][l].SetColor('r')
            frame[-1][r].SetColor('k')
            l += 1
        ds[r].value = ds[l].value
    ds[l].value = pivot
    for i in range(left, right+1):
        ds[i].SetColor()
    QSort(ds, left, l - 1, frame)
    QSort(ds, l + 1, right, frame)

def QSortTR(ds, left, right, frame):
    if right - left < 1:
        return
    for i in range(left, right + 1):
        ds[i].SetColor('b')
    pivot = ds[random.randint(left, right)].value
    i = left #the first element index after the last element with value equal to the pivot
    j = left #the last element arg with value less than the pivot
    k = right + 1 #the first element arg with value larger than the pivot
    while i < k:
        frame.append(deepcopy(ds))
        frame[-1][i].SetColor('r')
        frame[-1][j].SetColor('k')
        frame[-1][k-1].SetColor('g')
        if ds[i].value < pivot:
            ds[i], ds[j] = ds[j], ds[i]
            i += 1
            j += 1
        elif ds[i].value > pivot:
            ds[i], ds[k-1] = ds[k-1], ds[i]
            k -= 1
        else:
            i += 1
    for i in range(left, right + 1):
        ds[i].SetColor()
    QSortTR(ds, left, j, frame)
    QSortTR(ds, k, right, frame)