import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        # remove shot when it leaves the screen
        if (self.position.x < 0 or self.position.x > constants.SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > constants.SCREEN_HEIGHT):
            self.kill()
