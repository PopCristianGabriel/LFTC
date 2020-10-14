from model.Identifier import Identifier


class Constant(Identifier):

    def __init__(self, name, value):
        Identifier.__init__(self,name,value)
        self.variable = False
