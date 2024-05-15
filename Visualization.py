import matplotlib.pyplot as plt
from matplotlib import animation
import time

from Sort.Data import Data
from Sort.BubbleSort import BubbleSort
from Sort.InsertationSort import InsertationSort
from Sort.SelectionSort import SelectionSort
from Sort.QuickSort import QuickSort_Normal
from Sort.QuickSort import QuickSort_ThreeRoad
#from Sort.MergeSort import MergeSort



def Visualization(dataset, SortNum, interval, SortDict):
    '''Use pyplot ans animation form matplotlib to complete Visualization on dataset and SortNum'''
    Figs = []
    frames = []
    times = [] #save the time of every sorting algorithm
    fig = plt.figure(1, figsize=(16, 9))
    for i in range(len(SortNum)): #generate figure for every sort algorithm in SortNum
        Figs.append(fig.add_subplot(131 + i))
        Figs[-1].set_xticks([])
        Figs[-1].set_yticks([])
    plt.subplots_adjust(left = 0.01, right = 0.99, bottom = 0.3, top = 0.7, wspace = 0.1, hspace = 0.2) #adjust the size of subplot
    
    for num in SortNum: #insert frames generated from different sort algorithm
        time_s = time.time()
        frames.append(globals()[SortDict[num]](dataset))
        time_t = time.time()
        times.append(time_t - time_s)
    
    def update(count):
        bars = []
        for i in range(len(SortNum)):
            if count < len(frames[i]):
            #if frame count now is not larger than the target frames numbers, update
                Figs[i].cla()
                Figs[i].set_title(SortDict[SortNum[i]])
                Figs[i].set_xticks([])
                Figs[i].set_yticks([])
                #generate bars with data from frames
                bars += Figs[i].bar(x = list(range(1,Data.DataCount+1)),
                                    height = [data.value for data in frames[i][count]],
                                    width = 1,
                                    color = [data.color for data in frames[i][count]]
                                    ).get_children()
        return bars
    
    anim = animation.FuncAnimation(fig, update, frames = max(map(len, frames)), interval = interval)
    plt.show()
    return times