import pygame
import sys
from threading import Thread

sys.path.append('./Map')

import MapManager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

map = pygame.image.load( "./Map/Images/sample.jpg")
maprect = map.get_rect()

mapWidth = int(map.get_width())
mapHeight = int(map.get_height())

y = 0
bY = 5
bX = 4

time1 = pygame.time.get_ticks()

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

pygame.image.save(map, "./Map/Images/blackstripes.png")

GameMap = MapManager.MapManager()

GameMap.load(map)

t = Thread(target=GameMap.populate, args=(map,))
t.start()

time2 = pygame.time.get_ticks()

print(str(time2 - time1))   

pygame.image.save(map, "./Map/Images/sampledone.png")

timeX = pygame.time.get_ticks()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

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