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
        self.dereferences = ls.dereferences



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
            line = re.split('(;,{}() )',line)
            #    line = re.split('[;,{}() ]',line)
            line = list(filter(None, line))
            self.program[i] = line



    def checkDereference(self,variable):
        if('[' not in variable or ']' not in variable):
            return False
        return True

    def checkLine(self,line):
        for i in range (len(line)):
            if not self.checkDereference(line[i]) and line[i] not in self.operators and line[i] not in self.reservedWords and (line[i] not in self.reservedWords and (line[i - 1]  not in ls.identifier and line[i-1] not in self.reservedWords) and i > 0) and self.symbolTable.exists(line[i]) == False:
                return False

        return True


    def checkValidityOfVariable(self, variable):
       if(variable[0] in "0123456789"):
           return False


    def interpretTokens(self):
        for lineNumber,line in enumerate(self.program):
            ok = False
            for separator in self.separators:
                if(separator in line[0]):
                    ok = True
                    break
            if(ok == False):
                print("Error at line ", lineNumber + 1)
                return

            line = line = re.split('[;,{}() ]',line[0])
            try:
                line.remove('\n')
            except ValueError as e:
                pass

            try:
                line.remove(';')
            except ValueError as e:
                pass
            try:
                line.remove('')
            except ValueError as e:
                pass

            ok = self.checkLine(line)
            if(ok == False):
                print("Error at line ",lineNumber + 1)
                return
            else:
                nextIsVariable = False
                for i,word in enumerate(line):
                    if(word in self.reservedWords or word in self.operators):
                        self.pif.add(word,-1)


                    elif(word in ls.identifier):
                        self.pif.add(word,-1)
                        nextIsVariable = True
                    elif(nextIsVariable == True):
                        ok = self.checkValidityOfVariable(word)
                        if(ok == False):
                            print("error at line",lineNumber + 1)
                            return
                        positionInSymbolTable = self.symbolTable.add(Identifier(word,0))
                        self.pif.add(word,positionInSymbolTable)


        print(self.pif.pif)
        self.symbolTable.printSymbolTable()



