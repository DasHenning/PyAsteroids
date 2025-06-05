import constants
import pygame
import circleShape as cs

class Projectile(cs.CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 3)

    def update(self, dt):
        self.position += self.velocity * dt
        
        # Remove the projectile if it goes off-screen
        if (self.position.x < -self.radius or self.position.x > constants.SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or self.position.y > constants.SCREEN_HEIGHT + self.radius):
            self.kill()