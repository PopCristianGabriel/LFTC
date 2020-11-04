class Node:

    def __init__(self,name,nexts = []):
        self.name = name
        self.nexts = []  #[[Node,value]]

    def addNext(self,next):
        self.nexts.append(next)

    def __eq__(self, other):
        return self.name == other.name


