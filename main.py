from model.Constant import Constant
from model.Identifier import Identifier
from model.SymbolTable import SymbolTable


def main():
    symbolTable =  SymbolTable()
    i1 = Identifier('a',1)
    i2 = Identifier('b',2)
    i3 = Identifier('c',3)
    c1 = Constant('d',4)
    c2 = Constant('d',5)

    symbolTable.add(i1)
    symbolTable.add(i2)
    symbolTable.add(i3)
    symbolTable.add(c1)
    try:
        symbolTable.add(c2)
    except Exception as e:
        pass

    symbolTable.printSymbolTable()



main()
