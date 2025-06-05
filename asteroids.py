import pygame
import constants
import circleShape as cs
import random

class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (163, 163, 163), self.position, self.radius, 5)

    def update(self, dt):
        self.position += self.velocity * dt
