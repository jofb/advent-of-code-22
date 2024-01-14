from Day import Day

class DayThree(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        total = 0
        for rucksack in self.lines:
            length = len(rucksack)
            comp1 = rucksack[:length // 2]
            comp2 = rucksack[length // 2:]
            # find the common char between each
            char = ''.join(set(comp1).intersection(comp2))
            if 'a' <= char <= 'z':
                total += ord(char) - ord('a') + 1
            else:
                total += ord(char) - ord('A') + 27
        return total
    
    def parttwo(self):
        total = 0
        rucksacks = [self.lines[i:i+3] for i in range(0, len(self.lines), 3)]
        for group in rucksacks:
            char = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))
            if 'a' <= char <= 'z':
                total += ord(char) - ord('a') + 1
            else:
                total += ord(char) - ord('A') + 27
        return total