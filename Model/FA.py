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


    def printStates(self):
        for node in self.nodes:
            print(node.name)

    def printAlphabet(self):
        print(self.E)

    def printFinalStates(self):
        print(self.endingPoints)

    def printDeterministic(self):
        for node in self.nodes:
            visited = []
            for next in node.nexts:
                if(next[1] in visited):
                    return False
                visited.append(next[1])
        return True



