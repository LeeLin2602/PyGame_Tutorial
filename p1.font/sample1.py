import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Font Sample Code")
window.fill((255, 255, 255))

default_font = pygame.font.SysFont(None, 40)

text1 = default_font.render('Hello World!', True, (0, 0, 0))

window.blit(text1, (10, 10))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
