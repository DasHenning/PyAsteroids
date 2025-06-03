import pygame
import constants

def main():
    pygame.init()
    window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    print(
        "Starting Asteroids!\n"
        f"Screen width: {constants.SCREEN_WIDTH}\n"
        f"Screen height: {constants.SCREEN_HEIGHT}"
    )
    
    while True:
        if pygame.event.get(pygame.QUIT):
            return
        window.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()