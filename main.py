import pygame
import player
import constants
import logger
from asteroids import Asteroid
import asteroidfield
import sys
from shot import Shot 

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    #groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #instances auto-contain in groups
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    #class instances
    ship = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    ast_field = asteroidfield.AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        logger.log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        #automaticaly updates all objects in updatable group via the update method
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                logger.log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    logger.log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        #iterate over all objects in drawable group to draw them on screen
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
