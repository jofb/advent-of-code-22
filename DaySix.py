from Day import Day

class DaySix(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        total = 0
        window_size = 4
        
        line = self.lines[0]
        # move a window through the string and check for distinctness in first 4 chars
        for i in range(len(line) - window_size + 1):
            window = line[i:i + window_size]
            # check distinctness of window
            if(len(set(window)) == window_size):
                total += i    
                print(i + window_size)
                break
    
    def parttwo(self):
        total = 0
        window_size = 14
        
        line = self.lines[0]
        # move a window through the string and check for distinctness in first 4 chars
        for i in range(len(line) - window_size + 1):
            window = line[i:i + window_size]
            # check distinctness of window
            if(len(set(window)) == window_size):
                total += i    
                print(i + window_size)
                break
    