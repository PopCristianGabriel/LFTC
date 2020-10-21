class Identifier:

    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.variable = True

    def __eq__(self, other):
        return self.name == other.getName()

    def __str__(self):
        return self.name +" "+ str(self.value)

    def getName(self):
        return self.name

    def setName(self,newName):
        self.name = newName

    def getValue(self):
        return self.value

    def setValue(self,newValue):
        self.value = newValue