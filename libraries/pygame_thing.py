import pygame, sys

pygame.init()

screen_size = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Hi")

print(pygame.display.get_active())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
