import random

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
        tiles = {}
        tileprint = 0
        currentTile = 0
        for y in range(0, mapObject.get_height()-1):
            for x in range(0, mapObject.get_width()-1):
                CurCol = mapObject.get_at((x, y))
                if CurCol == (255,255,255,255):
                    tiles[f"{currentTile}"] = Tile(currentTile)
                    goodtiles = self.tileChecker(x, y, mapObject)
                    for pixel in goodtiles: 
                        tiles[f"{currentTile}"].add_pixel(pixel)
                    if tileprint < 20:
                        print(f"Added tiles: {goodtiles}")
                        tileprint += 1
                    localId = tiles[f"{currentTile}"].getId() % (255*3)
                    if localId < 255:
                        colour1 = localId
                        colour2 = 0
                        colour3 = 0
                    elif localId >= 255 and localId <= 510:
                        colour1 = 255
                        colour2 = localId - 255
                        colour3 = 0
                    else:
                        colour1 = 255
                        colour2 = 255
                        colour3 = localId - 510
                    tiles[f"{currentTile}"].paint_pixels(mapObject, int(colour1),int(colour2),int(colour3))
                    currentTile += 1
        self.amountOfTiles = currentTile
        print(f"{tiles.keys()}")

class Tile:

    def __init__(self, Id):
        self.Id = Id
        self.pixels = []
        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def getId(self):
        return self.Id

    def add_pixel(self,pixel):
        self.pixels.append(pixel)

    def paint_pixels(self, map, r,g,b):
        print(f"{r},{g},{b}")
        for pixel in self.pixels:
            map.set_at((pixel[0],pixel[1]), (r,g,b,255))

