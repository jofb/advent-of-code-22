import re

from Day import Day

class DayFive(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        index = self.lines.index('')

        all_crates = []
        for x in range(len(self.lines[index - 1].replace(" ", ""))):
            c_index = 1 + (x * 4)
            # from each crate we're grabbing the c_indexth char
            mapped_crates = map(lambda z : z[c_index], self.lines[:index - 1])
            filtered_crates = filter(lambda y : y != ' ', mapped_crates)
            crates = list(filtered_crates)
            all_crates.append(crates)

        # parse instructions
        for instruction in self.lines[index + 1:]:
            params = [int(n) for n in re.findall(r'\d+', instruction)]
            num = params[0]
            source = params[1]
            dest = params[2]
            
            # check crates to move from source
            moved_crates = all_crates[source - 1][:num]
            # remove from source
            all_crates[source - 1] = all_crates[source - 1][num:]
            # place in dest
            all_crates[dest - 1] = list(reversed(moved_crates)) + all_crates[dest - 1]

        s = ''.join(map(lambda c : c[0], all_crates))
        return s
    
    def parttwo(self):
        index = self.lines.index('')

        all_crates = []
        for x in range(len(self.lines[index - 1].replace(" ", ""))):
            c_index = 1 + (x * 4)
            # from each crate we're grabbing the c_indexth char
            mapped_crates = map(lambda z : z[c_index], self.lines[:index - 1])
            filtered_crates = filter(lambda y : y != ' ', mapped_crates)
            crates = list(filtered_crates)
            all_crates.append(crates)

        # parse instructions
        for instruction in self.lines[index + 1:]:
            params = [int(n) for n in re.findall(r'\d+', instruction)]
            num = params[0]
            source = params[1]
            dest = params[2]
            
            # check crates to move from source
            moved_crates = all_crates[source - 1][:num]
            # remove from source
            all_crates[source - 1] = all_crates[source - 1][num:]
            # place in dest
            all_crates[dest - 1] = moved_crates + all_crates[dest - 1]

        s = ''.join(map(lambda c : c[0], all_crates))
        return s
    