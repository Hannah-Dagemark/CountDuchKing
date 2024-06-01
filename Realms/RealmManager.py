import random

class RealmManager:
    
    def load(self, mapObject, amount=6):
        print("Loading Players...")
        self.players = {}
        self.amount = amount
        temptext = open("./Realms/computer_names.txt", "r")
        self.compnames = temptext.read()
        self.compnames = self.compnames.split("\n")
        temptext.close()
        temptext = open("./Realms/valid_border_colours.txt", "r")
        self.colournames = temptext.read()
        self.colournames = self.colournames.split("\n")
        temptext.close()
        for x in range(self.amount):
            if x == 0:
                c = self.colournames[random.randint(0,len(self.colournames)-1)]
                self.players[0] = Player("p1", c)
                self.colournames.remove(c)
            c1 = self.colournames[random.randint(0,len(self.colournames)-1)]
            c2 = self.compnames[random.randint(0,len(self.compnames)-1)]
            self.players[x] = Player("c", c1, x, c2)
            self.colournames.remove(c1)
            self.compnames.remove(c2)
        for x in self.players:
            p = self.players[x]
            print(f"Player {p.id}/{p.name} with colour {p.borderColour}")
            
    def getPlayer(self, detail):
        if detail == "p1":
            return self.players[0]
        else:
            return self.players[int(detail)]
        
    def updateDaywisePlayerResources(self, id, MapMan):
        print(f"\n\n\nUpdating DaywiseResourceGain for {id}\n\n")
        p = self.players[id]
        print(f"\nPrevious gains: {p.daywiseResourceGain}")
        p.resetDailyGains()
        print(f"HeldTiles Check: {p.heldTiles}")
        for t in p.heldTiles:
            tInfo = MapMan.tiles[str(t)]
            for resource in tInfo.resources:
                p.daywiseResourceGain[str(resource[1])] += resource[0]
        print(f"\nNew gains: {p.daywiseResourceGain}")
        
    def applyResourceIncome(self, id):
        print(f"Applying resource income for {id}")
        p = self.players[id]
        for r in p.daywiseResourceGain.keys():
            p.resources[str(r)] += p.daywiseResourceGain[str(r)]
        if p.passiveResourceGain.keys():
            for r in p.passiveResourceGain.keys():
                p.resources[str(r)] += p.passiveResourceGain[str(r)]

    

            
        
class Player:
    
    def __init__(self, controller, colour, id=0, name=None,):
        self.resources = {
            "settlers": 1,
            "villagers": 4,
            "wood": 0.0,
            "stone": 0.0,
            "food": 0.0,
            "weapons": 0.0,
            "tools": 0.0,
        }
        self.daywiseResourceGain = {
            "wood": 0.0,
            "stone": 0.0,
            "food": 0.0,
            "weapons": 0.0,
            "tools": 0.0
        }
        self.passiveResourceGain = {}
        self.id = id
        self.controller = controller
        self.heldTiles = []
        self.borderTiles = []
        colour = colour.split(",")
        print (colour)
        self.borderColour = (int(colour[0]),int(colour[1]),int(colour[2]))
        self.name = name
    
    def resetDailyGains(self):
        self.daywiseResourceGain = {
            "wood": 0.0,
            "stone": 0.0,
            "food": 0.0,
            "weapons": 0.0,
            "tools": 0.0
        }