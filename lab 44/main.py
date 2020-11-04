from Model.Reader import Reader

if __name__ == '__main__':
   reader = Reader('input2.txt')
   finitaAutomata = reader.getFA()
   finitaAutomata.printFA()