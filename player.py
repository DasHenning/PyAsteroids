import pygame
import circleShape as cs
import constants
import projectiles

class Player(cs.CircleShape):
    shotTimer = 0    # timer to control fire rate

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
        # locking player to screen pac-man style
        if self.position.x + 20 < 0:
            self.position.x = constants.SCREEN_WIDTH + 20
        elif self.position.x - 20 > constants.SCREEN_WIDTH:
            self.position.x = -20
        if self.position.y < 0:
            self.position.y = constants.SCREEN_HEIGHT
        elif self.position.y > constants.SCREEN_HEIGHT:
            self.position.y = 0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shotTimer <= 0:
            self.shotTimer = constants.FIRE_RATE
            self.shoot()
        
        self.shotTimer -= dt
    def rotate(self, dt):
        self.rotation += dt*constants.PLAYER_ROTATE_SPEED
        self.rotation %= 360  # Keep the rotation within 0-360 degrees
    
    def move(self, dt):
        self.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * constants.PLAYER_SPEED * dt
        self.position += self.velocity

    def shoot(self):
        projectileVelocitiy = pygame.Vector2(0, -1).rotate(self.rotation) * constants.PROJECTILE_SPEED
        projectile = projectiles.Projectile(self.position.x, self.position.y, constants.PROJECTILE_RADIUS, projectileVelocitiy)
