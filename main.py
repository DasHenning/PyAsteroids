import pygame
import constants
import player
import asteroids
import asteroidFields

def main():
    pygame.init()
    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroidsGroup = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroids.Asteroid.containers = (asteroidsGroup, updatable, drawable)
    asteroidFields.AsteroidField.containers = (updatable)

    print(
        "Starting Asteroids!\n"
        f"Screen width: {constants.SCREEN_WIDTH}\n"
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    
    clock = pygame.time.Clock()
    deltaTime = 0

    character = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 
    asteroidField = asteroidFields.AsteroidField()

    while True:
        if pygame.event.get(pygame.QUIT):
            return

        window.fill("black")

        updatable.update(deltaTime)
        for member in drawable:
            member.draw(window)

        deltaTime = clock.tick(100)/1000  # pauses loop for 1/100th of a second (causes 100 FPS) and adds time since last call to deltaTime in seconds (here 0.01)
        pygame.display.flip()


if __name__ == "__main__":

    main()