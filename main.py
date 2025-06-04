import pygame
import constants
import player

def main():
    pygame.init()
    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)

    print(
        "Starting Asteroids!\n"
        f"Screen width: {constants.SCREEN_WIDTH}\n"
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    
    clock = pygame.time.Clock()
    deltaTime = 0

    character = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2) 

    while True:
        if pygame.event.get(pygame.QUIT):
            return

        window.fill("black")

        updatable.update(deltaTime)
        for member in drawable:
            member.draw(window)

        deltaTime = clock.tick(100)/1000  # pauses loop for 1/100th of a second (causes 100 FPS) and adds time since last call to deltaTime
        pygame.display.flip()


if __name__ == "__main__":

    main()