import Visualization
from DataGenerator import NewData

animation_interval = 10
SortDict = {1:'BubbleSort',
            2:'InsertationSort',
            3:'SelectionSort',
            4:'QuickSort_Normal',
            5:'QuickSort_ThreeRoad',
            6:'MergeSort'}

TypeDict = {1:'random',
            2:'almost-sorted',
            3:'reverse',
            4:'few-unique'}

def StartVis(DataCount, Dtype, interval, SortNum):
    '''try:
        DataCount = int(input('Please enter the numbers of data items(default 30):'))
    except:
        DataCount = 30
    dataset = NewData(DataCount, Dtype) 
    SortNum = [1, 2, 3] #set the target 3 kinds of sort algorithm
    print('---------------------------')
    print('Available Sorting Algorithm')
    for item in SortDict.items():
        print(item)
    print('---------------------------')
    try:
        SortNum[0] = int(input('Please enter the number of Sort Algorithm 1:'))
        SortNum[1] = int(input('Please enter the number of Sort Algorithm 2:'))
        SortNum[2] = int(input('Please enter the number of Sort Algorithm 3:'))
    except: #if an input is not right, set the SortNum to default values
        SortNum = [1, 2, 3]
    '''
    dataset = NewData(DataCount, Dtype)
    Visualization.Visualization(dataset = dataset,
                                SortNum = SortNum,
                                interval = animation_interval,
                                SortDict = SortDict) 