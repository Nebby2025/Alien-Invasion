import pygame
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))

while True:
    new_event = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(new_event)
    time.sleep(2)