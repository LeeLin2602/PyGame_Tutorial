import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Event Sample Code")
window.fill((255, 255, 255))

default_font = pygame.font.SysFont(None, 40, False, True)
text1 = default_font.render('<3', True, (0, 0, 0))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            window.blit(text1, (x, y))
            pygame.display.flip()
