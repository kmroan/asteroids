from circleshape import CircleShape
from logger import log_event
import pygame, constants, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        ast1 = velocity.rotate(self.velocity)
        ast2 = velocity.rotate(self.velocity * -1)

