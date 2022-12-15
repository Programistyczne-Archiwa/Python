import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw a rectangle
    pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
    pygame.display.update()
    