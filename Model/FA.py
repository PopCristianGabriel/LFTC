class FA:

    def __init__(self,startingPoint,endingPoints,E,nodes):
        self.startingPoint = startingPoint
        self.endingPoints = endingPoints
        self.E = E
        self.nodes = nodes


    def refactor(self):

        for node in self.nodes:
            newNexts = []
            for i in range (len(node.nexts)):
                if( i % 2 == 0):
                    newNexts.append(node.nexts[i])
            node.nexts = newNexts

    def printFA(self):
        for node in self.nodes:
            for next in node.nexts:
                print(node.name + ' goes to ' + next[0].name + ' with ' + next[1])






