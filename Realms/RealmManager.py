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
        temptext = open("./Realms/valid_border_colours.txt", "r")
        self.colournames = temptext.read()
        print (self.colournames)
        self.colournames = self.colournames.split("\n")
        temptext.close()
        for x in range(self.amount):
            if x == 0:
                self.players[0] = Player("p1", self.colournames)
            self.players[x] = Player("c", self.colournames, x, self.compnames)
        for x in self.players:
            p = self.players[x]
            print(f"Player {p.id}/{p.name} with colour {p.borderColour}")
            
    def getPlayer(self, detail):
        if detail == "p1":
            return self.players[0]
        else:
            return self.players[int(detail)]
            
        
class Player:
    
    def __init__(self, controller, colour, id=0, names=None,):
        self.id = id
        self.controller = controller
        self.heldTiles = []
        colour = colour[random.randint(0,len(colour)-1)]
        colour = colour.split(",")
        print (colour)
        self.borderColour = (int(colour[0]),int(colour[1]),int(colour[2]))
        if controller == "c":
            self.name = names[random.randint(0,len(names)-1)]