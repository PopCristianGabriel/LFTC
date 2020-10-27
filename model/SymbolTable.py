from model.Identifier import Identifier


class SymbolTable:

    def __init__(self):
        self.table = {}
        self.checkingTable = {}
        self.index = 0

    def add(self,newValue):
        position = self.checkingTable.get(newValue.getName())
        if(position == None):
            self.checkingTable[newValue.getName()] = self.index
            self.table[self.index] = newValue
            self.index += 1
            return self.index - 1
        value = self.table[position]
        if(value.variable == True):
            self.table[position] = newValue
            return position


    def exists(self,identifier):
        return self.checkingTable.get(identifier) != None


    def get(self,id):
       return self.table[id]

    def printSymbolTable(self):
        for index,value in self.table.items():
            print("id: " , index , "value:" ,value)



