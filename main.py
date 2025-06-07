import time

import pygame
import constants
import levelSystem
import player
import asteroids
import asteroidField
import projectiles

def main():
    pygame.init()

    started = time.time()

    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroidsGroup = pygame.sprite.Group()
    projectilesGroup = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroids.Asteroid.containers = (asteroidsGroup, updatable, drawable)
    asteroidField.AsteroidField.containers = (updatable)
    projectiles.Projectile.containers = (projectilesGroup, updatable, drawable)

    print(
        "Starting Asteroids!\n"
        f"Screen width: {constants.SCREEN_WIDTH}\n"
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    
    clock = pygame.time.Clock()
    deltaTime = 0
    secondCheck = 0.0

    character = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    asteroidSpace = asteroidField.AsteroidField()

    while True:
        if pygame.event.get(pygame.QUIT):
            return

        window.fill("black")

        updatable.update(deltaTime)
        
        # check for collisions between asteroids and player
        for asteroid in asteroidsGroup:
            if character.collision(asteroid):
                character.draw(window)
                pygame.display.flip()

                passed = time.time() - started
                print(f"Game Over! You died at Level {levelSystem.level} and survived {int(passed)} seconds.")
                return
            
        # check for collisions between projectiles and asteroids
        for projectile in projectilesGroup:
            for asteroid in asteroidsGroup:
                if projectile.collision(asteroid):
                    projectile.kill()
                    asteroid.split()
                    break  # prevent multiple collisions with the same projectile
        
        for member in drawable:
            member.draw(window)

        # increment the level every 20 seconds
        passedTime = int(time.time() - started)
        if  secondCheck >= 1 and passedTime%20 == 0 and levelSystem.level < 15:
            secondCheck = 0
            levelSystem.increaseLevel()
        
        deltaTime = clock.tick(100)/1000  # pauses loop for 1/100th of a second (causes 100 FPS) and adds time since last call to deltaTime in seconds (here 0.01)
        secondCheck += deltaTime
        pygame.display.flip()


if __name__ == "__main__":
    main()