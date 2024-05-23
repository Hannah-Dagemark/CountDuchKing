import random

class RealmManager:
    
    def load(self, mapObject, amount=6):
        print("Loading Players...")
        self.players = {}
        self.amount = amount
        temptext = open("./Realms/computer_names.txt", "r")
        self.compnames = temptext.read()
        print (self.compnames)
        self.compnames = self.compnames.split("\n")
        temptext.close()
        for x in range(self.amount):
            if x == 0:
                self.players[0] = Player("p1")
            self.players[x] = Player("c", x, self.compnames)
        for x in self.players:
            p = self.players[x]
            print(f"Player {p.id}/{p.name} with colour {p.borderColour}")
            
    def getPlayer(self, detail):
        if detail == "p1":
            return self.players[0]
        else:
            print("oopsie")
            
        
class Player:
    
    def __init__(self, controller, id=0, names=None):
        self.id = id
        self.controller = controller
        self.borderColour = (random.randint(10,240),random.randint(10,240),random.randint(10,240))
        if controller == "c":
            self.name = names[random.randint(0,len(names)-1)]