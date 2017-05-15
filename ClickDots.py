import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click to Draw") 
keep_going = True
YELLOW = (255,0,0)
radius = 15

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            pygame.draw.circle(screen, YELLOW, spot, radius)
    pygame.display.update()

pygame.quit()
