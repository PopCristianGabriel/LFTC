class UI:

    def __init__(self,fa):
        self.fa = fa

    def printOptions(self):
        print("1 - print all the states")
        print("2 - print the alphabet")
        print("3 - print the transitions")
        print("4 - print the final states")
        print("5 - check if the given FA is deterministic")
        print("6 - check if a sequence is accepted by fa")
        print("0 - quit")

    def run(self):
        option = 23
        while(option != 0):
            self.printOptions()
            option = int(input())
            if(option == 1):
                self.fa.printStates()
            elif(option == 2):
                self.fa.printAlphabet()
            elif(option == 3):
                self.fa.printFA()
            elif(option == 4):
                self.fa.printFinalStates()
            elif(option == 5):
                if(self.fa.printDeterministic()):
                    print("the Finita automata is deterministic")
                else:
                    print("the Finita automata is not deterministic")
            elif(option == 6):
                sequence = input()
                sequence = sequence.split(" ")
                print(self.fa.accepts(sequence))

