import pygame
import constants
import circleShape as cs
import random

class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (115, 115, 115), self.position, self.radius, 6)

    def update(self, dt):
        self.position += self.velocity * dt

        # Remove the asteroid if it goes off-screen
        if (self.position.x < -self.radius*3 or self.position.x > constants.SCREEN_WIDTH + self.radius*3 or
            self.position.y < -self.radius*3 or self.position.y > constants.SCREEN_HEIGHT + self.radius*3):
            self.kill()

    def split(self):
        if self.radius > constants.ASTEROID_MIN_RADIUS:
            newAngle = random.uniform(20, 50)

            newVector1 = self.velocity.rotate(newAngle)
            newVector2 = self.velocity.rotate(-newAngle)

            newRadius = self.radius-constants.ASTEROID_MIN_RADIUS

            child1 = Asteroid(self.position.x + self.velocity.rotate(90).normalize().x*newRadius,
                                self.position.y + self.velocity.rotate(90).normalize().y*newRadius,
                                newRadius)
            child1.velocity = newVector1*1.4

            child2 = Asteroid(self.position.x - self.velocity.rotate(90).normalize().x*newRadius,
                                self.position.y - self.velocity.rotate(90).normalize().y*newRadius,
                                newRadius)
            child2.velocity = newVector2*1.4

        self.kill()