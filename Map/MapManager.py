import random
import TileTypes

class MapManager:

    def tileChecker(self, x, y, map):
        list = []
        CurY = y
        CurX = x
        RelX = 0
        RelY = 0
        floor = False
        contact = False
        while not floor:
            if map.get_at((CurX, CurY)) == (255,255,255,255) and y != 0:
                list.append((CurX,CurY))
                while not contact:
                    if CurX+RelX-1 >= 0:
                        RelX -= 1
                    else:
                        contact = True
                    if map.get_at((CurX+RelX, CurY)) == (0,0,0,255):
                        contact = True
                    if map.get_at((CurX+RelX, CurY)) == (255,255,255,255):
                        list.append((CurX+RelX,CurY))
                contact = False
                RelX = 0
                while not contact:
                    if CurX+RelX+1 < map.get_width():
                        RelX += 1
                    else:
                        contact = True
                    if map.get_at((CurX+RelX, CurY)) == (0,0,0,255):
                        contact = True
                    if map.get_at((CurX+RelX, CurY)) == (255,255,255,255):
                        list.append((CurX+RelX,CurY))
                if CurY+1 < map.get_height():
                    CurY += 1
                else:
                    floor = True
                contact = False
                RelX = 0
            elif map.get_at((CurX, CurY)) == (255,255,255,255) and y == 0:
                list.append((CurX,CurY))
                contact = False
                contactB = False
                RelX = 0
                RelY = 0
                while not contact:
                    if map.get_at((CurX+RelX, CurY)) == (0,0,0,255):
                        contact = True
                    if map.get_at((CurX+RelX, CurY)) == (255,255,255,255):
                        list.append((CurX+RelX,CurY))
                        while not contactB:
                            if CurY+RelY+1 < map.get_height():
                                RelY += 1
                            else:
                                contactB = True
                            if map.get_at((CurX+RelX, CurY+RelY)) == (255,255,255,255):
                                list.append((CurX+RelX,CurY+RelY))      
                            else:
                                contactB = True
                    if CurX+RelX+1 < map.get_width():
                        RelX += 1
                    else:
                        contact = True
                    contactB = False
                    RelY = 0
                contact = False
                floor = True
                RelX = 0
            else:
                floor = True
        return list

    def load(self,mapObject):
        print("Loading map")
        self.tiles = {}
        self.paintedTile = None
        tileprint = 0
        currentVertical = 0
        currentHorizontal = 0
        currentTile = 0
        for y in range(0, mapObject.get_height()-1):
            if (y-1) % 10 == 0:
                currentVertical += 1
                currentHorizontal = 0
            #print(f"Current Vertical:{currentVertical}")
            for x in range(0, mapObject.get_width()-1):
                CurCol = mapObject.get_at((x, y))
                if CurCol == (255,255,255,255):
                    self.tiles[f"{currentTile}"] = Tile(currentTile,(currentHorizontal,currentVertical))
                    goodtiles = self.tileChecker(x, y, mapObject)
                    for pixel in goodtiles: 
                        self.tiles[f"{currentTile}"].add_pixel(pixel)
                    if tileprint < 20:
                        #print(f"Added tiles: {goodtiles}")
                        tileprint += 1
                    colour1 = 0
                    colour2 = 255
                    colour3 = 0
                    self.tiles[f"{currentTile}"].paint_pixels(mapObject, int(colour1),int(colour2),int(colour3))
                    currentTile += 1
                    currentHorizontal += 1
        self.amountOfTiles = currentTile
        self.Verticals = 120
        self.Horizontals = 80
        print(f"{self.tiles.keys()}")

    def populate(self, mapObject):
        print("Populating map")
        print("Loading terrains...")
        self.TileWorker = TileTypes.TerrainWorker()
        self.TileWorker.generateTerrain()
        tilesMapped = [["" for i in range(self.Verticals)] for j in range(self.Horizontals)]
        types = self.TileWorker.get_terrain("types")
        for tile in self.tiles.keys():
            position = self.tiles[f"{tile}"].Position
            #print(f"{position}")
            if position[1] == 0:
                choice = random.randrange(1,7)
                if choice != 6 and position[0] != 0:
                    tilesMapped[position[0]][position[1]] = tilesMapped[position[0]-1][position[1]]
                else:
                    tilesMapped[position[0]][position[1]] = self.TileWorker.get_rand_tType(tilesMapped, position)
            elif position [0] == 0:
                choice = random.randrange(1,7)
                if choice != 6 and position[1] != 0:
                    tilesMapped[position[0]][position[1]] = tilesMapped[position[0]][position[1]-1]
                else:
                    tilesMapped[position[0]][position[1]] = self.TileWorker.get_rand_tType(tilesMapped, position)
            else:
                choice = random.randrange(1,21)
                if choice <= 6:
                    tilesMapped[position[0]][position[1]] = tilesMapped[position[0]][position[1]-1]
                elif choice >= 7 and choice <= 14:
                    tilesMapped[position[0]][position[1]] = tilesMapped[position[0]-1][position[1]]
                elif choice != 20:
                    choice2 = random.randrange(1,3)
                    if choice2 == 1:
                        tilesMapped[position[0]][position[1]] = tilesMapped[position[0]][position[1]-1]
                    else:
                        if position[0] != int(mapObject.get_width()):
                            tilesMapped[position[0]][position[1]] = tilesMapped[position[0]+1][position[1]-1]
                        else:
                            tilesMapped[position[0]][position[1]] = tilesMapped[position[0]-1][position[1]-1]
                elif choice == 20:
                    tilesMapped[position[0]][position[1]] = self.TileWorker.get_rand_tType(tilesMapped, position)
        #print(f"{tilesMapped}")
        mappedColours = self.TileWorker.get_terrain("colours")
        for x in self.tiles.keys():
            tile = self.tiles[f"{x}"]
            if tilesMapped[tile.Position[0]][tile.Position[1]] != "":
                colour = mappedColours[f"{tilesMapped[tile.Position[0]][tile.Position[1]]}"]
                colour1, colour2, colour3 = colour[0], colour[1], colour[2]
                tile.add_terrain(f"{tilesMapped[tile.Position[0]][tile.Position[1]]}")
                tile.paint_pixels(mapObject, int(colour1),int(colour2),int(colour3))
                tile.findBorder(mapObject)
    
    def findTileAt(self, pos):
        for x in self.tiles.keys():
            tile = self.tiles[f"{x}"]
            if any(x == pos for x in tile.getPixels()):
                if int(x) == int(tile.getId()):
                    return x
                else:
                    print(f"Mismatching ID for found tile: {x} / {tile.getId()}")
                    return (x,tile.getId())
                
        print(f"Could not find tile at position: {pos[0]},{pos[1]}")
        return None
    
    def getTileInfo(self, id):
        info = {}
        thistile = self.tiles[f"{id}"]
        info["id"] = id
        info["pixels"] = thistile.getPixels()
        info["terrain"] = thistile.getTerrain()
        info["border"] = thistile.getBorderPixels()
        info["gameplay"] = thistile.getGameplayInfo()
        return info
    
    def paintTileBorder(self, id, mapObject):
        if self.paintedTile != None:
            self.clearPaintedTile(mapObject)
            print("Clearing previous tile")
        tile = self.tiles[f"{id}"]
        tile.paint_border_pixels(mapObject)
        self.paintedTile = tile
    
    def clearPaintedTile(self, mapObject):
        self.paintedTile.paint_border_pixels(mapObject)
        self.paintedTile = None
        print("Cleared previous tile")
    
        
class Tile:

    def __init__(self, Id, Pos):
        self.Id = Id
        self.Position = Pos
        self.pixels = []
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.terrain = ""
        self.resources = {}
        self.buildings = []
        self.units = {}
        self.owner = "Unclaimed"
        self.pop = 0
        self.borderPixels = []
        self.borderPainted = False
    
    def getId(self):
        return self.Id
    
    def getPixels(self):
        return self.pixels
    
    def getTerrain(self):
        return self.terrain
    
    def getBorderPixels(self):
        return self.borderPixels
    
    def getGameplayInfo(self):
        infoToSend = (("resources", self.resources), ("buildings", self.buildings), ("units", self.units), ("owner", self.owner), ("population", self.pop))
        return infoToSend

    def add_pixel(self,pixel):
        self.pixels.append(pixel)

    def add_terrain(self, terrain):
        self.terrain = terrain
        #print(f"Added terrain for tile {self.Id}, it is now a {self.terrain} / {terrain} biome")

    def paint_pixels(self, map, r,g,b):
        for pixel in self.pixels:
            map.set_at((pixel[0],pixel[1]), (r,g,b,255))
    
    def paint_border_pixels(self, map):
        if self.borderPainted == False:
            print(f"Painting border for tile {self.Id}")
            for pixel in self.borderPixels:
                map.set_at((pixel[0],pixel[1]), (255,255,255,255))
            self.borderPainted = True
        else:
            print(f"Clearing border for tile {self.Id}")
            for pixel in self.borderPixels:
                map.set_at((pixel[0],pixel[1]), (0,0,0,255))

    def findBorder(self, map):
        for pixel in self.pixels:
            #check above
            if pixel[1] != 0:
                if map.get_at((pixel[0],pixel[1]-1)) == ((0,0,0,255)):
                    self.borderPixels.append((pixel[0],pixel[1]-1))
            #check right
            if pixel[0] < map.get_width()-1:
                if map.get_at((pixel[0]+1,pixel[1])) == ((0,0,0,255)):
                    self.borderPixels.append((pixel[0]+1,pixel[1]))
            #check below
            if pixel[1] < map.get_height()-1:
                if map.get_at((pixel[0],pixel[1]+1)) == ((0,0,0,255)):
                    self.borderPixels.append((pixel[0],pixel[1]+1))
            #check left
            if pixel[0] != 0:
                if map.get_at((pixel[0]-1,pixel[1])) == ((0,0,0,255)):
                    self.borderPixels.append((pixel[0]-1,pixel[1]))


