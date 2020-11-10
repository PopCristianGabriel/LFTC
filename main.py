from Model.Reader import Reader
from UI.UI import UI

if __name__ == '__main__':
   reader = Reader('FA.in.txt')
   finitaAutomata = reader.getFA()
   ui = UI(finitaAutomata)
   ui.run()
