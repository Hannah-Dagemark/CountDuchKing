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
        tileprint = 0
        currentVertical = 0
        currentHorizontal = 0
        currentTile = 0
        for y in range(0, mapObject.get_height()-1):
            if (y-1) % 5 == 0:
                currentVertical += 1
                currentHorizontal = 0
            print(f"Current Vertical:{currentVertical}")
            for x in range(0, mapObject.get_width()-1):
                CurCol = mapObject.get_at((x, y))
                if CurCol == (255,255,255,255):
                    self.tiles[f"{currentTile}"] = Tile(currentTile,(currentHorizontal,currentVertical))
                    goodtiles = self.tileChecker(x, y, mapObject)
                    for pixel in goodtiles: 
                        self.tiles[f"{currentTile}"].add_pixel(pixel)
                    if tileprint < 20:
                        print(f"Added tiles: {goodtiles}")
                        tileprint += 1
                    colour1 = 0
                    colour2 = 255
                    colour3 = 0
                    self.tiles[f"{currentTile}"].paint_pixels(mapObject, int(colour1),int(colour2),int(colour3))
                    currentTile += 1
                    currentHorizontal += 1
        self.amountOfTiles = currentTile
        self.Verticals = 200
        self.Horizontals = 200
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
            print(f"{position}")
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
        print(f"{tilesMapped}")
        mappedColours = self.TileWorker.get_terrain("colours")
        for x in self.tiles.keys():
            tile = self.tiles[f"{x}"]
            if tilesMapped[tile.Position[0]][tile.Position[1]] != "":
                colour = mappedColours[f"{tilesMapped[tile.Position[0]][tile.Position[1]]}"]
                colour1, colour2, colour3 = colour[0], colour[1], colour[2]
                tile.paint_pixels(mapObject, int(colour1),int(colour2),int(colour3))
    
        
class Tile:

    def __init__(self, Id, Pos):
        self.Id = Id
        self.Position = Pos
        self.pixels = []
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def getId(self):
        return self.Id

    def add_pixel(self,pixel):
        self.pixels.append(pixel)

    def paint_pixels(self, map, r,g,b):
        for pixel in self.pixels:
            map.set_at((pixel[0],pixel[1]), (r,g,b,255))

