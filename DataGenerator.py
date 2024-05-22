import random
from Sort.Data import Data

def generate_original_data(DataCount, Dtype = 'random'): #generate original data with Dtype distribution
    data_list = []
    match Dtype:
        case 'random': #data ranging in (1, DataCount) with random order
            data_list = list(range(1,DataCount + 1))
            random.shuffle(data_list)
        case 'almost-sorted': #sorted data except two points
            data_list = list(range(1,DataCount + 1))
            a, b = random.randint(0,DataCount), random.randint(0,DataCount)
            while a == b:
                b = random.randint(0,DataCount)
            data_list[a], data_list[b] = data_list[b], data_list[a]
        case 'reverse': #reverse sorted data
            data_list = list(range(DataCount,-1,-1))
        case 'few-unique': #data with only 4 kind of values
            d = DataCount // 4
            data_list += [d] * d
            data_list += [d*2] * d
            data_list += [d*3] * d
            data_list += [d*4] * (DataCount - d*3)
            random.shuffle(data_list)
        case _: #other options
            print('Unknown Type of Data Distribution')
            exit()
    return data_list

def NewData(DataCount, Dtype = 'random'):
    Data.DataCount = DataCount if 2 < DataCount < int(1e5) else 32
    original_data = generate_original_data(DataCount, Dtype)
    DataSet = list(map(Data, original_data))
    return DataSet