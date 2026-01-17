import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mouse Motion Demo")

object_size = 20
object_color = (255, 0, 0)
object_rect = pygame.Rect(0, 0, object_size, object_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            object_rect.center = event.pos

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, object_color, object_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()

# TODO: Learn something basic first then come back to this, like requests with bs4
