import pygame
import random
from asteroids import Asteroid
from constants import *
import levelSystem

class AsteroidField(pygame.sprite.Sprite):
    # edges of the screen where asteroids can spawn
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-(ASTEROID_MIN_RADIUS*levelSystem.asteroidSize), y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MIN_RADIUS*levelSystem.asteroidSize, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -(ASTEROID_MIN_RADIUS*levelSystem.asteroidSize)),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MIN_RADIUS*levelSystem.asteroidSize),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE*levelSystem.levelMultiplier:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, levelSystem.asteroidSize)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)