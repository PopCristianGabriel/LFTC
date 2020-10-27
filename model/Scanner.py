import LanguageSpecifications as ls
import re

from model.Identifier import Identifier


class Scanner:
    def __init__(self,fileName,pif,symbolTable):
        self.fileName = fileName
        self.operators = ls.operators
        self.separators = ls.separators
        self.reservedWords = ls.reservedWords
        self.pif = pif
        self.symbolTable = symbolTable



    def initializeSeparators(self):
        finalString = ''
        for str in self.separators:
            finalString += str + ' ' + '|'
        #for str in self.operators:
        #    finalString += '(' + str + ')' + ' ' + '|'
        #for str in self.reservedWords:
        #    finalString += '(' + str + ')' + ' ' + '|'
        finalString = finalString[:-1]
        return finalString



    def readProgram(self):
        with open(self.fileName,'r') as program:
            self.program = program.readlines()


    #'{ |} |; |(Program) |(Daca)'
    def tokanize(self):
        finalString = self.initializeSeparators()
        for i in range (len(self.program)):
            line = self.program[i]
            line = re.split('[;,{}() ]',line)
            line = list(filter(None, line))
            self.program[i] = line

        print("dawd")



    def checkLine(self,line):
        for i in range (len(line)):
            if line[i] not in self.operators and line[i] not in self.reservedWords and (line[i] not in self.reservedWords and (line[i - 1]  not in ls.identifier and line[i-1] not in self.reservedWords) and i > 0) and self.symbolTable.exists(line[i]) == False:
                return False

        return True


    def checkValidityOfVariable(self, variable):
       return True

    def interpretTokens(self):
        for line in (self.program):
            line.remove('\n')
            ok = self.checkLine(line)
            if(ok == False):
                print("Error at line ",i)
            else:
                nextIsVariable = False
                for i,word in enumerate(line):
                    if(word in self.reservedWords):
                        self.pif.add(word,-1)
                    elif(word in ls.identifier):
                        self.pif.add(word,-1)
                        nextIsVariable = True
                    elif(nextIsVariable == True):
                        ok = self.checkValidityOfVariable(word)
                        if(ok == False):
                            print("error")
                            return
                        positionInSymbolTable = self.symbolTable.add(Identifier(word,0))
                        self.pif.add(word,positionInSymbolTable)


        print(self.pif.pif)
        self.symbolTable.printSymbolTable()



