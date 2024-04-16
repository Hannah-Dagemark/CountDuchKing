import random

class TerrainWorker:

    def generateTerrain(self):
        self.terrains = []
        ocean = Terrain("ocean", (0, 102, 255), 2, True, ("plains", "forest", "hills"))
        self.terrains.append(ocean)
        lake = Terrain("lake", (0, 204, 255), 1, True, ("plains", "forest", "hills"))
        self.terrains.append(lake)
        plains = Terrain("plains", (0, 200, 0), 1, False, ("ocean", "lake", "forest", "hills", "desert"))
        self.terrains.append(plains)
        forest = Terrain("forest", (0, 100, 0), 2, False, ("ocean", "lake", "plains", "hills"))
        self.terrains.append(forest)
        hills = Terrain("hills", (102, 102, 153), 2, False, ("ocean", "lake", "plains", "forest"))
        self.terrains.append(hills)
        desert = Terrain("desert", (230, 230, 0), 1, False, ("plains", "dune"))
        self.terrains.append(desert)
        dune = Terrain("dune", (153, 153, 0), 2, False, ("desert",))
        self.terrains.append(dune)
        self.terrainNames = []
        for terrain in self.terrains:
            self.terrainNames.append(str(terrain.name))
        print(f"Added {self.terrainNames}")
        

    def get_terrain(self, action):
        if action == "types":
            return self.terrainNames
        if action == "colours":
            dictionary = {}
            for terrain in self.terrains:
                dictionary[terrain.name] = terrain.colour
            #print(f"{dictionary}")
            return dictionary
    
    def biomebalance(self, biome):
        if biome == "ocean":
            return 2
        if biome == "lake":
            return 3
        if biome == "plains":
            return 5
        if biome == "forest":
            return 4
        if biome == "hills":
            return 3
        if biome == "desert":
            return 2
        if biome == "dune":
            return 1
        
        
    def get_rand_tType(self,dict,pos):
        available_terrains = []
        proximity_terrains = []
        if pos[1] == 0:
            available_terrains = self.terrainNames
        else:
            #print(f"Testing: {dict[pos[0]][pos[1]-1]}")
            if dict[pos[0]][pos[1]-1] != "" and dict[pos[0]][pos[1]-1] != None:
                proximity_terrains.append(dict[pos[0]][pos[1]-1])
                #print(f"Found proxy terrain: {dict[pos[0]][pos[1]-1]}")
            #print(f"Testing: {dict[pos[0]+1][pos[1]-1]}")
            if dict[pos[0]+1][pos[1]-1] != "" and dict[pos[0]+1][pos[1]-1] != None:
                proximity_terrains.append(dict[pos[0]+1][pos[1]-1])
                #print(f"Found proxy terrain: {dict[pos[0]+1][pos[1]-1]}")
            if proximity_terrains == []:
                #print("Fixing null proxy error")
                available_terrains = self.terrainNames
            for terrain in proximity_terrains:
                #print(f"Terrain using:{terrain}")
                for matchterrain in self.terrains:
                    if matchterrain.name == terrain:
                        #print(f"Matched with Terrain successfully")
                        for proxy in matchterrain.proxys:
                            for x in range(0, self.biomebalance(proxy)):
                                available_terrains.append(proxy)
                            #print(f"Found available terrain:{proxy}")
        
        tTypeNum = random.randrange(0, len(available_terrains))
        return available_terrains[tTypeNum]

class Terrain:

    def __init__(self, name, colour, moveC, water, proxys):
        self.name = name
        self.colour = colour
        self.moveCost = moveC
        self.isWater = water
        self.proxys = proxys