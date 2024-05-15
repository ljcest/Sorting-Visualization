import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from DataGenerator import NewData
from Visualization import Visualization

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

class MainWindow():
    def __init__(self, root):
        '''initial the MainWindow'''
        self.root = root
        self.TopFrame = ttk.Frame(root).pack(side = 'top')
        #initial the frame to select datatype
        self.Frame_datatype = ttk.Labelframe(self.TopFrame, text = '排序数据分布类型')
        self.Frame_datatype.pack(side = 'left')
        self.datatype = tk.IntVar()
        for v, s in TypeDict.items():
            self.b = ttk.Radiobutton(self.Frame_datatype, text = s, variable = self.datatype, value = v)
            self.b.pack()
        
        #initial the frame to input nums of data
        self.Frame_datanums = ttk.Labelframe(self.TopFrame, text = '排序数据数量(建议100内)')
        self.Frame_datanums.pack(side = 'left')
        self.datanums_str = tk.StringVar()
        self.b = ttk.Entry(self.Frame_datanums, textvariable = self.datanums_str)
        self.b.pack()

        #initial the frame to select 3 sort algorithms
        self.Frame_sorttype = ttk.Labelframe(self.TopFrame, text = '排序算法(仅支持3个)')
        self.Frame_sorttype.pack(side = 'left')
        self.sort_list = []
        self.button_list = []
        self.Boolvar_list = []
        for v, s in SortDict.items():
            self.Boolvar_list.append(tk.BooleanVar())
            self.b = ttk.Checkbutton(self.Frame_sorttype, text = s, variable = self.Boolvar_list[-1], command = self.Update_Sortlist)
            self.b.pack()
            self.button_list.append(self.b)
        
        #initial the button to start Visualization
        self.ButtonFrame = ttk.Frame(root).pack(side = 'bottom')
        self.ButtonStart = ttk.Button(self.ButtonFrame, text = '开始排序', command = self.Start)
        self.ButtonStart.pack(side = 'left')
        self.ButtonExit = ttk.Button(self.ButtonFrame, text = '退出', command = self.Exit)
        self.ButtonExit.pack(side = 'left')
             
    def Update_Sortlist(self):
        self.sort_list = []
        for i in range(len(self.Boolvar_list)):
            if self.Boolvar_list[i].get():
                self.sort_list.append(i + 1)

    #command function of ButtonStart
    def Start(self):
        try:
            self.datanums = int(self.datanums_str.get())
        except:
            messagebox.showerror(title = '错误', message = '数据数量只能为纯数字')
            return
        if self.datanums < 1:
            messagebox.showerror(title = '错误', message = '数据数量必须大于1')
            return
        if len(self.sort_list) != 3:
            messagebox.showerror(title = '错误', message = '选择的排序算法数只能为3')
            return
        self.dataset = NewData(self.datanums, TypeDict[self.datatype.get()])
        self.times = Visualization(dataset = self.dataset,
                                   SortNum = self.sort_list,
                                   interval = animation_interval,
                                   SortDict = SortDict)

        messagebox.showinfo(title = '算法结束', message = '算法1用时:{}ms\n \
                                                             算法2用时:{}ms\n \
                                                             算法3用时:{}ms\n'.format(*self.times))
    
    def Exit(self):
        self.root.quit

if __name__ == '__main__':
    root = tk.Tk()
    root.title('排序可视化初始设置界面')
    MainWindow(root)
    root.mainloop()
