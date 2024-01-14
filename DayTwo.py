from Day import Day

class DayTwo(Day):
    def __init__(self):
        super().__init__()
        
    def parttwo(self):
        total = 0
        score = {"A": 0, "B": 1, "C": 2}
        rounds = map(lambda s : s.replace(" ", ""), self.lines)
        for round in rounds:
            subtotal = 0
            p1 = round[0]
            option = round[1]
            if option == "X":
                subtotal += ((score[p1] - 1) % 3) + 1
            elif option == "Y":
                subtotal += 3
                subtotal += score[p1] + 1
            elif option == "Z":
                subtotal += 6
                subtotal += ((score[p1] + 1) % 3) + 1

            total += subtotal


        return total
        
    def partone(self):
        total = 0
        shapeMap = {"X": "A", "Y": "B", "Z": "C"}
        score = {"A": 1, "B": 2, "C": 3}
        rounds = map(lambda s : s.replace(" ", ""), self.lines)
        for round in rounds:
            subtotal = 0
            # first determine match outcome
            p1 = round[0]
            p2 = shapeMap[round[1]]
            if p1 == p2:
                subtotal += 3
            elif (p1 == "C" and p2 == "A") or (p1 == "A" and p2 == "B") or (p1 == "B" and p2 == "C"):
                subtotal += 6
                
            # then add on shape score
            subtotal += score[p2]
            total += subtotal
        
        return total
