import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Event Sample Code")
window.fill((255, 255, 255))

default_font = pygame.font.SysFont(None, 40)

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        if e.type == pygame.KEYDOWN:
            window.fill((255, 255, 255))
            window.blit(default_font.render('You press down ' + chr(e.key), True, (0, 0, 0)), (10, 10))
            pygame.display.flip()