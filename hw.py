import pygame
import sys

pygame.init()
class Picture():
    def __init__(self, screen, image_address):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()
        self.ship = Picture(screen, "images/ship.bmp")
        self.moving_right = False
        self.moving_left = False

    def draw(self):
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self..moving_right = True
        #elif event.type == pygame.KEYUP:
            #self._check_keyup_events(event)


    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 255))
    ship = Picture(screen, "images/ship.bmp")
    ship.draw()
    pygame.display.flip()
