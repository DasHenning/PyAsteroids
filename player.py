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