from abc import abstractmethod

class Day():
    def __init__(self):
        # read in text file
        file = open("input.txt", "r")
        self.lines = [s.replace("\n", "") for s in file.readlines()]
        file.close()
        
    def run(self, part): 
        if part == 1:
            return self.partone()
        else:
            return self.parttwo()
        
    def partone(self): raise NotImplementedError
    def parttwo(self): raise NotImplementedError