from Day import Day

class DayOne(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        self.lines.append('')
        # when we run into a gap add everything before it
        subtotal = 0
        max = 0
        for line in self.lines:
            if line == '':
                if subtotal > max:
                    max = subtotal
                subtotal = 0
            else:
                subtotal += int(line)
            
        return max
        
    def parttwo(self):
        self.lines.append('')
        
        subtotal = 0
        subtotals = []
        
        for line in self.lines:
            if line == '':
                subtotals.append(subtotal)
                subtotal = 0
            else:
                subtotal += int(line)
                
        # sort the list
        subtotals.sort(reverse = True)
        
        total = subtotals[0] + subtotals[1] + subtotals[2]
        return total
        
    def run(self, part):
        if part == 1:
            return self.partone()
        else:
            return self.parttwo()
        