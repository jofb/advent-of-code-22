from Day import Day

class DaySeven(Day):
    def __init__(self):
        super().__init__()
        
    def partone(self):
        # ignore first command
        self.lines = self.lines[1:]
        # build tree from input
        root_node = Node(None)
        current_node = root_node
        exploring = False
        for line in self.lines:
            # catch cd commands, ignore ls
            if(line[0] == "$"):
                if exploring: 
                    exploring = False
                    current_node.explored = True
                    
                if(line[2:4] == "cd"):
                    dest = line[5:]
                    print("moving to ", dest)
                    if dest == "..": current_node = current_node.get_parent()
                    else: current_node = current_node.get_child(dest)
                else:
                    exploring = True
            elif not current_node.explored:
                ops = line.split(" ")
                if(ops[0].isdigit()):
                    # add value if number
                    print("adding size ", ops[0])
                    current_node.add_size(int(ops[0]))
                else:
                    # create child if dir
                    print("creating child ", ops[1])
                    current_node.add_child(ops[1], Node(current_node))
        
        return root_node.total_sizes(100000)

    
    def parttwo(self):
        # ignore first command
        self.lines = self.lines[1:]
        # build tree from input
        root_node = Node(None)
        current_node = root_node
        exploring = False
        for line in self.lines:
            # catch cd commands, ignore ls
            if(line[0] == "$"):
                if exploring: 
                    exploring = False
                    current_node.explored = True
                    
                if(line[2:4] == "cd"):
                    dest = line[5:]
                    if dest == "..": current_node = current_node.get_parent()
                    else: current_node = current_node.get_child(dest)
                else:
                    exploring = True
            elif not current_node.explored:
                ops = line.split(" ")
                if(ops[0].isdigit()):
                    # add value if number
                    current_node.add_size(int(ops[0]))
                else:
                    # create child if dir
                    current_node.add_child(ops[1], Node(current_node))
        
        # need to find smallest node that is larger than needed space 
        unused_space = 70000000 - root_node.size
        needed_space = 30000000 - unused_space 
        
        return sorted(root_node.find_sizes_larger(needed_space))[0]
    
class Node():
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.size = 0
        self.explored = False
        
    def add_child(self, name, node):
        self.children[name] = node
        
    def get_child(self, name):
        return self.children[name]
    
    def get_parent(self):
        return self.parent
        
    def add_size(self, size):
        self.size += size
        if(self.parent): self.parent.add_size(size)
    
    def total_sizes(self, limit):
        total = 0
        if(self.size <= limit): 
            total = self.size
            
        for child in self.children.values():
            total += child.get_sizes(limit)
                     
        return total
    
    def find_sizes_larger(self, limit):
        nodes = []
        if(self.size >= limit):
            nodes.append(self.size)
        
        for child in self.children.values():
            nodes.extend(child.find_sizes_larger(limit))
            
        return nodes
