from Model.FA import FA
from Model.Node import Node
import copy

class Reader:
    def __init__(self,fileName):
        self.fileName = fileName


    def existsNode(self,nodes,name):
        if(len(nodes) == 0):
            return False
        for node in nodes:
            if(node.name == name):
                return True
        return False


    def getNode(self,nodes,name):
        for node in nodes:
            if(node.name == name):
                return node




    def getFA(self):
        with open(self.fileName,'r') as file:
            file.seek(0,0)
            fl = file.readlines()
            nodes = fl[0]
            nodes = nodes.rstrip()
            nodes = nodes.split(' ')
            startingPoint =  nodes[0]
            endingNodes = fl[1]
            endingNodes = endingNodes.rstrip()
            endingNodes = endingNodes.split(' ')
            E = fl[2]
            E = E.strip()
            nodes = []
            transitions = []
            for i in range(3,len(fl)):
                line = fl[i]
                line = line.rstrip()
                if(len(line) > 0):
                    line = line.split(' ')
                    if(not self.existsNode(nodes,line[0])):
                        node = Node(line[0])
                        if(not self.existsNode(nodes,line[1])):
                            nextNode = Node(line[1])

                            node.addNext([nextNode,line[2]])
                            nodes.append(nextNode)
                        else:
                            nextNode = self.getNode(nodes,line[1])
                            node.addNext([nextNode,line[2]])
                        nodes.append(node)

                    else:
                        node = self.getNode(nodes,line[0])
                        if (not self.existsNode(nodes, line[1])):
                            nextNode = Node(line[1])
                            node.addNext([nextNode, line[2]])
                            nodes.append(nextNode)
                        else:
                            nextNode = self.getNode(nodes, line[1])
                            node.addNext([nextNode, line[2]])





            finitaAutomata = FA(startingPoint,endingNodes,E,nodes)
            finitaAutomata.refactor()
            return finitaAutomata

