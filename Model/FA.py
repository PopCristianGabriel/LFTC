import copy
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


    def getStartingPoint(self,name):
        for node in self.nodes:
            if(node.name == name):
                return node

    def accepts(self,sequence):
        node = self.getStartingPoint(self.startingPoint)
        toVisit = copy.copy(node.nexts)


        while(len(sequence) > 0 and len(toVisit) > 0):
            j = 0
            toVisit2 = copy.copy(toVisit)
            for i,nodeNext in enumerate(toVisit2):
                if(nodeNext[1] != sequence[0]):
                    del toVisit[j]

                else:
                    j+= 1
            del sequence[0]
            toVisit2 = []
            currently = copy.copy(toVisit)
            for next in toVisit:
                toVisit2.append(copy.copy(self.getStartingPoint(next[0].name).nexts))
            try:
                toVisit = toVisit2[0]
            except Exception:
                pass

        if(len(sequence) != 0):
            return False
        for node in currently:
            if(node[0].name in self.endingPoints):
                return True
        return False





