import random
import logger
import pygame
import circleshape
import constants

class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = self.velocity.rotate(angle) * 1.2

            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = self.velocity.rotate(-angle) * 1.2
