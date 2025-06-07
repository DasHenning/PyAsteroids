level = 1
levelMultiplier = 1.0
asteroidSize = 3

def increaseLevel():
    global level, levelMultiplier, asteroidSize

    level += 1
    levelMultiplier -= 0.04

    if level%5 == 0 and asteroidSize < 6:
        asteroidSize += 1