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
    bY = 5
    bX = 4
    while bX < mapWidth:
        for x in range(bX, mapWidth):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                if y % 5 == 0:
                    map.set_at((x, y), (0,0,0,255))
                    y += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bX += 8
        y = 0

    y = bY

    while bY < mapHeight:
        for x in range(0, mapWidth):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                if y % 5 == 0:
                    map.set_at((x, y), (0,0,0,255))
                    y += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bY += 10
        y = bY

    bX = 4
    y = 0

    while bX < mapWidth:
        for x in range(bX, -1, -1):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                if y % 5 == 0:
                    map.set_at((x, y), (0,0,0,255))
                    y += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bX += 8
        y = 0

    bY = 2
    y = bY

    while bY < mapHeight:
        for x in range(mapWidth, 0, -1):
            if y < mapHeight:    
                map.set_at((x, y), (0,0,0,255))
                y += 1
                if y % 5 == 0:
                    map.set_at((x, y), (0,0,0,255))
                    y += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bY += 10
        y = bY
        
initMapGen()
class uText:

    def __init__(self):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.texts = []

    def write(self, text, position):
        self.texts.append((text,position))
        
    def delete(self, text):
        text2 = []
        for place in self.texts:
            if place[0] != text:
                text2.append(place)
        self.texts = text2
    
    def runText(self):
        for text in self.texts:
            textPrint = self.font.render(str(text[0]), True, (255, 255, 255))
            textPrintRect = textPrint.get_rect()
            textPrintRect = textPrintRect.move(int(text[1][0]),int(text[1][1]))
            screen.blit(textPrint, textPrintRect)
        
    def runTextTile(self, tile_pressed):
        info = GameMap.getTileInfo(tile_pressed)
        tile_pressed = str(tile_pressed)
        tilePrint = self.font.render(tile_pressed, True, (255, 255, 255))
        tilePrintRect = tilePrint.get_rect()
        tilePrintRect = tilePrintRect.move(1000,50)
        screen.blit(tilePrint, tilePrintRect)

uTexter = uText()

uTexter.write("State",(1000,0))

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
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if tile_pressed != None:
        uTexter.runTextTile(tile_pressed)
    
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