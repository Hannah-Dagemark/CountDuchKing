import random

class TerrainWorker:

    def generateTerrain(self):
        self.terrains = []
        ocean = Terrain("ocean", (0, 102, 255), 2, True)
        self.terrains.append(ocean)
        lake = Terrain("lake", (0, 204, 255), 1, True)
        self.terrains.append(lake)
        plains = Terrain("plains", (0, 200, 0), 1, False)
        self.terrains.append(plains)
        forest = Terrain("forest", (0, 100, 0), 2, False)
        self.terrains.append(forest)
        hills = Terrain("hills", (102, 102, 153), 2, False)
        self.terrains.append(hills)
        desert = Terrain("desert", (230, 230, 0), 1, False)
        self.terrains.append(desert)
        dune = Terrain("dune", (153, 153, 0), 2, False)
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
            return dictionary
        
    def get_rand_tType(self):
        tTypeNum = random.randrange(0, len(self.terrains))
        return self.terrainNames[tTypeNum]

class Terrain:

    def __init__(self, name, colour, moveC, water):
        self.name = name
        self.colour = colour
        self.moveCost = moveC
        self.isWater = water