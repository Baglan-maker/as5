import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Mouse Interaction")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            print(f"Mouse moved to ({x}, {y})")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"Mouse clicked at ({x}, {y})")

    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()
