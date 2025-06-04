import pygame
import circleshape as cs
import constants

class Player(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)

        self.rotation = 0
    
    # creates a triangle shape representing the player visually
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.3

        #corner points of the triangle
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, surface):
        pygame.draw.polygon(surface, "white", self.triangle())

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)

    def rotate(self, dt):
        self.rotation += dt*constants.PLAYER_ROTATE_SPEED
        self.rotation %= 360  # Keep the rotation within 0-360 degrees
    
    