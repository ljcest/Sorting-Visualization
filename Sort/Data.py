class Data(object):

    DataCount = 32 #default numbers of data items

    def __init__(self, value):
        self.value = value
        self.SetColor()
    
    def SetColor(self, rgba = 0):
        if not rgba:
            self.color = (1,
                         1 - self.value/(self.DataCount*2),
                         0.5 + self.value/(self.DataCount*2),
                         1)
        else:
            self.color = rgba
