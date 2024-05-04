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
                if y % set_at((x, y), (0,0,0,255))
                    y5 == 0:
                    map. += 1
        screen.blit(map, maprect)
        pygame.display.flip()
        bY += 10
        y = bY