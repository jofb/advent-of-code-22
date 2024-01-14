from Day import Day

class DayFour(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        total = 0
        for line in self.lines:
            pair = line.split(",")
            # map to lists of numbers, then check bounds
            elf1 = list(map(lambda x : int(x), pair[0].split("-")))
            elf2 = list(map(lambda x : int(x), pair[1].split("-")))

            if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
                total += 1
 
        return total
    
    def parttwo(self):
        total = 0
        for line in self.lines:
            pair = line.split(",")
            # map to lists of numbers, then check bounds
            elf1 = list(map(lambda x : int(x), pair[0].split("-")))
            elf2 = list(map(lambda x : int(x), pair[1].split("-")))

            if ((elf1[0] <= elf2[1] and elf1[1] >= elf2[1]) or (elf1[1] >= elf2[0] and elf1[0] <= elf2[0]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1])):
                total += 1
 
        return total
    
    