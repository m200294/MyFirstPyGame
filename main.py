import pygame
import player
import constants
import logger


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)
    
    ship = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        logger.log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
