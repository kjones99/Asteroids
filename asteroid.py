import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        angle_offset = random.uniform(20, 50)
        ast1_velocity = self.velocity.rotate(angle_offset)
        ast2_velocity = self.velocity.rotate(-angle_offset)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = ast1_velocity * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = ast2_velocity * 1.2

    
