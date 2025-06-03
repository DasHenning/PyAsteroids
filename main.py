import pygame
import constants
import player

def main():
    pygame.init()
    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    print(
        "Starting Asteroids!\n"
        f"Screen width: {constants.SCREEN_WIDTH}\n"
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    
    clock = pygame.time.Clock()
    deltaTime = 0

    while True:
        if pygame.event.get(pygame.QUIT):
            return

        window.fill("black")

        # create and draw the player (check also player.py)
        character = player.Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
        character.draw(window)

        pygame.display.flip()

        deltaTime = clock.tick(100)/1000  # pauses loop for 1/100th of a second (causes 100 FPS) and adds time since last call to deltaTime

if __name__ == "__main__":
    main()