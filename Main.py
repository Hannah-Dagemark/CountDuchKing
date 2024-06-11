import pygame
import sys
import random
from threading import Thread

sys.path.append('./Map')
sys.path.append('./Script')
sys.path.append('./Realms')

import ScriptUtils
import MapManager
import RealmManager

# pygame setup
pygame.init()
w,h = 1280, 720
screen = pygame.display.set_mode((w, h))
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
            #print("\n\nT E X T S :")
            #p = []
            #for t in self.texts:
            #    p.append(t[0])
            #print(p)
        
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
        
    def runResourceView(self, info, mode):
        i=0
        if mode == "t": #If running resource view for tile
            info = GameMap.getTileInfo(info)
            
            while (100 + 50*i) < 720: #(Map height)
                self.write("",(840,100+50*i))
                self.write("",(1090,100+50*i))
                i += 1
            i = 0
            self.write("State",(1000,0))
            self.write("Terrain: ", (840,50))
            self.write(info["terrain"].capitalize(),(1090,50))

            for bit in info["gameplay"]:
                #if type(bit) == "<class 'str'" or type(bit) == "<class 'int'":
                if bit[0] == "resources":
                    self.write(f"{bit[0].capitalize()}:", (840,100 + 50*i))
                    i -= 1
                    for subbit in bit[1]:
                        i += 1
                        self.write(f"{subbit[1].capitalize()}, {subbit[0]}",(1090,100+50*i))
                else:
                    self.write(f"{bit[0].capitalize()}:",(840,100 + 50*i))
                    if bit[1] != [] and bit[1] != {}:
                        self.write(bit[1],(1090,100 + 50*i))
                    else:
                        self.write("None",(1090,100 + 50*i))
                i += 1
            tilePrint = self.font.render(info["id"], True, (255, 255, 255))
            tilePrintRect = tilePrint.get_rect()
            tilePrintRect = tilePrintRect.move(1100,0)
            screen.blit(tilePrint, tilePrintRect)
        if mode == "p": #If running resource view for player
            info = GameRealms.getPlayer(info)

            while (100+50*i) < 720: #(Map height)
                self.write("",(840,100+50*i))
                self.write("",(1090,100+50*i))
                i += 1
            i = 0

            self.write(info.name,(1000,0))
            self.write("",(840,50))
            self.write("",(1090,50))

            for key in info.resources.keys():
                self.write(f"{key.capitalize()}:",(840,50 + 50*i))
                self.write(info.resources[key],(1090,50 + 50*i))
                i += 1
            
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

    def addButton(self, name, x, y, width, height, colour_standby=(255,255,255), colour_hover=(200, 200, 200), onAction=None, delOnAction=False):
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
            "delOnAction": delOnAction,
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
            elif button["isHover"] == True:
                button["isHover"] = False

    def drawButtons(self):
        for button in self.buttons:
            buttonRect = pygame.Rect(button["xPos"],button["yPos"],button["width"],button["height"])
            if button["isHover"] == False:
                pygame.draw.rect(screen,(button["colour_standby"]),buttonRect)
            else:
                pygame.draw.rect(screen,(button["colour_hover"]),buttonRect)
                
    def pressed(self, pos):
        for button in self.buttons:
            if button["isHover"] == True:
                if button["button_action"] != None:
                    if button["delOnAction"] == True:
                        self.buttons.remove(button)
                        uTexter.write("",(button["xPos"],button["yPos"]))
                    exec(button["button_action"])
                else:
                    print(f"No action found for button {button["text"]}")
        
class uCommunicate:
    
    def __init__(self):
        self.globalGameState = 0 #0 = preround, 1 = active
        self.globalTurn = 0
        self.turnHolder = 0
        self.resourceView = False #False = State resources, True = Player resources
        self.resourceViewActive = True #False = No Button Rendered, True = Button Rendered
    
    def startGame(self):
        GameRealms.load(map)
        self.globalGameState = 1
        self.globalTurn = 1
        uTexter.write("Turn:",(850,580))
        uButtoner.addButton("Player", 850, 0, 120, 50, "darkgray", "gray", "uCommunicator.switchResourceView()", True)
        uButtoner.addButton("Claim", 850, 500,110,40,"darkgray","gray","uCommunicator.claimState()")
        t2 = Thread(target=uCommunicator.gameLoop)
        t2.start()
    
    def tileSelected(self):
        uButtoner.addButton("Build", 0, 600, 100, 50, "darkgray", "gray", "uPopper.buildMenu()")
        uButtoner.addButton("Assemble", 150, 600, 180, 50, "darkgray", "gray", "uPopper.buildMenu()")
        uButtoner.addButton("Order", 380, 600, 120, 50, "darkgray", "gray", "uPopper.buildMenu()")

    def switchResourceView(self):
        if self.resourceView:    
            uButtoner.addButton("Player", 850, 0, 120, 50, "darkgray", "gray", "uCommunicator.switchResourceView()", True)
            self.resourceView = False
        elif not self.resourceView:
            if tile_pressed != None:
                uButtoner.addButton("State", 850, 0, 120, 50, "darkgray", "gray", "uCommunicator.switchResourceView()", True)
                self.resourceViewActive = True
            else:
                self.resourceViewActive = False
            self.resourceView = True

    def gameLoop(self):
        while self.globalGameState == 1:
            for x in range(GameRealms.amount):
                self.turnHolder = x
                GameRealms.applyResourceIncome(x)
                if self.turnHolder != 0:
                    self.turnHolder = GameRealms.players[x].id
                    print(f"Turn being played by: {self.turnHolder}/{GameRealms.players[x].name}")        
                    self.expand_cccs(self.turnHolder)
                else:
                    GameRealms.updateDaywisePlayerResources(self.turnHolder, GameMap)
                    self.globalTurn += 1
                    uTexter.write(str(self.globalTurn), (1090, 580))
                    while self.turnHolder == 0:
                        None
        
    def claimState(self):
        if GameMap.paintedTile and self.turnHolder == 0:
            if not GameMap.tIsClaimed(GameMap.paintedTile.Id):
                ip = GameRealms.getPlayer(f"p1")
                pt = GameMap.paintedTile
                if pt.Id in ip.borderTiles and ip.resources["villagers"] > 0:
                    print(f"Claiming {pt.Id} for {ip.name}")
                    GameMap.claimTileFor(pt.Id,ip)
                    ip.heldTiles.append(pt.Id)
                    for tile in GameMap.findBorderTiles(pt.Id):
                        ip.borderTiles.append(int(tile))
                    ip.resources["villagers"] -= 1
                    self.turnHolder += 1
                elif ip.resources["settlers"] > 0:
                    print(f"Settling {pt.Id} for {ip.name}")
                    GameMap.claimTileFor(pt.Id,ip)
                    ip.heldTiles.append(pt.Id)
                    for tile in GameMap.findBorderTiles(pt.Id):
                        ip.borderTiles.append(int(tile))
                    ip.resources["settlers"] -= 1
                    self.turnHolder += 1
                else:
                    self.turnHolder += 1
    
    def expand_cccs(self, ccc):
        print(f"Using ccc = {ccc}")
        expandTile = None
        curPlayer = GameRealms.getPlayer(f"{ccc}")
        if len(curPlayer.heldTiles) == 0:
            while expandTile == None:
                tryTile = GameMap.findTileAt((random.randint(0,800),random.randint(0,550)))
                if tryTile != None:
                    if not GameMap.tIsClaimed(tryTile):
                        expandTile = tryTile
            GameMap.claimTileFor(expandTile,curPlayer,map)
            curPlayer.heldTiles.append(expandTile)
        else:
            while expandTile == None:
                trytile = int(curPlayer.heldTiles[random.randint(0,len(curPlayer.heldTiles)-1)])
                daPos = GameMap.getTileInfo(trytile)["position"]
                ranX = random.randint(0,3)
                if ranX == 0:
                    if GameMap.getTileInfo(trytile+1)["owner"] == "Unclaimed":
                        expandTile = trytile+1
                elif ranX == 1:
                    if GameMap.getTileInfo(trytile-1)["owner"] == "Unclaimed":
                        expandTile = trytile-1
                elif ranX == 2:
                    daPos = (daPos[0],daPos[1]+1)
                    if GameMap.findTileAtRel(daPos) != None:
                        if GameMap.getTileInfo(GameMap.findTileAtRel(daPos))["owner"] == "Unclaimed":
                            expandTile = GameMap.findTileAtRel(daPos)
                elif ranX == 3:
                    daPos = (daPos[0],daPos[1]-1)
                    if GameMap.findTileAtRel(daPos) != None:
                        if GameMap.getTileInfo(GameMap.findTileAtRel(daPos))["owner"] == "Unclaimed":
                            expandTile = GameMap.findTileAtRel(daPos)
                
            GameMap.claimTileFor(expandTile,GameRealms.getPlayer(f"{ccc}"),map)
            curPlayer.heldTiles.append(expandTile)

class uPop:
        
    def __init__(self):
        self.yes = True
        self.menuColour = (100, 100, 100)
        self.itemColour = (200, 200, 200)
        self.Popup = None
        self.hasPopup = False

    def buildMenu(self):
        self.hasPopup = True
        self.Popup = {
            "x": 200, "y": 200
        }

            
    

uPopper = uPop()
uButtoner = uButtons()
uTexter = uText()
uCommunicator = uCommunicate()

def prerenderGraphics():
    uButtoner.addButton("Start Game", 850, 500, 200, 50, "darkgray", "gray", "uCommunicator.startGame()", True)
prerenderGraphics()


pygame.image.save(map, "./Map/Images/blackstripes.png")

GameRealms = RealmManager.RealmManager()

GameMap = MapManager.MapManager()

GameMap.load(map)

t1 = Thread(target=GameMap.populate, args=(map,))
t1.start()

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
            uCommunicator.globalGameState = 0
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                print(f"MB1 is true")
                pos = pygame.mouse.get_pos()
                uButtoner.pressed(pos)
                if pos[0] < 830 and pos[1] < 580:
                    tile_pressed = GameMap.findTileAt(pos)
                    if tile_pressed != None:
                        GameMap.paintTileBorder(tile_pressed, map)
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if uCommunicator.resourceViewActive == False and uCommunicator.resourceView == True and tile_pressed != None:
        uButtoner.addButton("State", 850, 0, 120, 50, "darkgray", "gray", "uCommunicator.switchResourceView()", True)

    if tile_pressed != None and uCommunicator.resourceView == False:
        uTexter.runResourceView(tile_pressed, "t")
    elif uCommunicator.globalGameState == 1:
        uTexter.runResourceView("p1", "p")
    
    if tile_pressed != None:
        uCommunicator.tileSelected()

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
uCommunicator.globalGameState = 0
pygame.quit()