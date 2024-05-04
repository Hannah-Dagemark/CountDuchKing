import pygame
import sys
from threading import Thread

sys.path.append('./Map')
sys.path.append('./Script')

import ScriptUtils
import MapManager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CountDuchKing')
clock = pygame.time.Clock()
running = True

map = pygame.image.load( "./Map/Images/sample.jpg")
maprect = map.get_rect()

mapWidth = int(map.get_width())
mapHeight = int(map.get_height())



time1 = pygame.time.get_ticks()
def initMapGen():
    y = 0
    bY = 10
    cY = 0
    bX = 6
    i = 0

    while bX < mapWidth:
        for x in range(bX, mapWidth):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                cY += 1
                if cY % 7 == 0:
                    while i != 4:
                        map.set_at((x, y), (0,0,0,255))
                        y += 1
                        i += 1
                    i = 0
                    cY += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bX += 12
        y = 0
        cY = 0

    bX = 6
    y = 0
    cY = y
    i = 0

    while bX < mapWidth:
        for x in range(bX, -1, -1):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                cY += 1
                if cY % 7 == 0:
                    while i != 4:
                        map.set_at((x, y), (0,0,0,255))
                        y += 1
                        i += 1
                    i = 0
                    cY += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bX += 12
        y = 0
        cY = y

    y = bY
    cY = 0
    
    while bY < mapHeight:
        for x in range(0, mapWidth):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                cY += 1
                if cY % 7 == 0:
                    while i != 4:
                        map.set_at((x, y), (0,0,0,255))
                        y += 1
                        i += 1
                    i = 0
                    cY += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bY += 20
        y = bY
        cY = 0

    bY = 12
    y = bY
    cY = 2

    while bY < mapHeight:
        for x in range(mapWidth, 0, -1):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                cY += 1
                if cY % 7 == 0:
                    while i != 4:
                        map.set_at((x, y), (0,0,0,255))
                        y += 1
                        i += 1
                    i = 0
                    cY += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bY += 20
        y = bY
        cY = 2
        
initMapGen()
class uText:

    def __init__(self):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.texts = []
        self.takenPos = []
        self.texts_to_remove = []

    def write(self, text, position):
        if not (text,position) in self.texts:    
            for textTest in self.texts:
                if textTest[0] != text and textTest[1] == position:
                    self.texts.remove(textTest)
            self.texts.append((text,position))
            print(self.texts)
        
    def delete(self, parameter, info):
        text2 = []
        for place in self.texts:
            if place[0] != info and parameter == "name":
                text2.append(place)
            elif place[1] != info and parameter == "pos":
                text2.append(place)
        self.texts = text2
    
    def runText(self):
        for text in self.texts:
            textPrint = self.font.render(str(text[0]), True, (255, 255, 255))
            textPrintRect = textPrint.get_rect()
            textPrintRect = textPrintRect.move(int(text[1][0]),int(text[1][1]))
            screen.blit(textPrint, textPrintRect)
        
    def runTextTile(self, tile_pressed):
        i=0
        info = GameMap.getTileInfo(tile_pressed)
        self.write(info["terrain"],(1000,50))
        
        for bit in info["gameplay"]:
            if True: #type(bit) == "<class 'str'" or type(bit) == "<class 'int'"
                self.write(bit[0],(840,100 + 50*i))
                self.write(bit[1],(1090,100 + 50*i))
            i += 1
        tile_pressed = str(tile_pressed)
        tilePrint = self.font.render(tile_pressed, True, (255, 255, 255))
        tilePrintRect = tilePrint.get_rect()
        tilePrintRect = tilePrintRect.move(1100,0)
        screen.blit(tilePrint, tilePrintRect)

class uButtons:

    def __init__(self):
        self.buttons = []
        self.colours = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "gray": (200, 200, 200),
            "darkgray": (100, 100, 100),
            "red": (255, 0, 0,),
            "green": (0, 255, 0,),
            "blue": (0, 0, 255,)
        }

    def addButton(self, name, x, y, width, height, colour_standby=(255,255,255), colour_hover=(200, 200, 200), onAction=print("Button pressed")):
        if colour_standby != (255,255,255):
            if self.colours[colour_standby] != None:
                colour_standby = self.colours[colour_standby]
            else:
                colour_standby = (255,255,255)
        if colour_hover != (200, 200, 200):
            if self.colours[colour_hover] != None:
                colour_hover = self.colours[colour_hover]
            else:
                colour_hover = (200, 200, 200)
        button = {
            "text": name,
            "xPos": x,
            "yPos": y,
            "width": int(width),
            "height": int(height),
            "colour_standby": colour_standby,
            "colour_hover": colour_hover,
            "button_action": onAction,
            "isHover": False
        }
        self.buttons.append(button)
        uTexter.write(name,(x,y))

    def updateHover(self):
        pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if pos[0] > button["xPos"] and pos[0] < button["xPos"] + button["width"]:
                if pos[1] > button["yPos"] and pos[1] < button["yPos"] + button["height"]:
                    button["isHover"] = True
            elif button["isHover"] == True:
                button["isHover"] = False

    def drawButtons(self):
        for button in self.buttons:
            buttonRect = pygame.Rect(button["xPos"],button["yPos"],button["width"],button["height"])
            if button["isHover"] == False:
                pygame.draw.rect(screen,(button["colour_standby"]),buttonRect)
            else:
                pygame.draw.rect(screen,(button["colour_hover"]),buttonRect)

uButtoner = uButtons()
uTexter = uText()

def prerenderGraphics():
    uTexter.write("State",(1000,0))
    uButtoner.addButton("Claim",850,600,110,40,"darkgray","gray")
prerenderGraphics()



pygame.image.save(map, "./Map/Images/blackstripes.png")

GameMap = MapManager.MapManager()

GameMap.load(map)

t = Thread(target=GameMap.populate, args=(map,))
t.start()

time2 = pygame.time.get_ticks()

print(str(time2 - time1))   

pygame.image.save(map, "./Map/Images/sampledone.png")

timeX = pygame.time.get_ticks()

print("Entering Running Stage")

tile_pressed = None

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                print(f"MB1 is true")
                pos = pygame.mouse.get_pos()
                tile_pressed = GameMap.findTileAt(pos)
                if tile_pressed != None:
                    GameMap.paintTileBorder(tile_pressed, map)
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if tile_pressed != None:
        uTexter.runTextTile(tile_pressed)
    
    uButtoner.updateHover()
    uButtoner.drawButtons()
    uTexter.runText()

    screen.blit(map, maprect)
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120
    timeY = pygame.time.get_ticks()
    if timeY % 1000 == 0:
        print(f"{timeY-timeX}ms per tick\n{1000/(timeY-timeX)} Ticks per second")
    timeX = pygame.time.get_ticks()
pygame.quit()