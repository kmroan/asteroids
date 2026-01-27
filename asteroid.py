from circleshape import CircleShape
import pygame, constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius,constants.LINE_WIDTH)

    def update(self, dt):
        self.move
