from abc import abstractmethod

class Day():
    def __init__(self):
        # read in text file
        file = open("input.txt", "r")
        self.lines = [s.replace("\n", "") for s in file.readlines()]
        file.close()
        
    def run():
        pass
    
    @abstractmethod 
    def show(self): raise NotImplementedError