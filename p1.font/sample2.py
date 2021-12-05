import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Font Sample Code")
window.fill((255, 255, 255))

default_font = pygame.font.SysFont(None, 40, False, True)
text1 = default_font.render('Hello World!', True, (0, 0, 0))
window.blit(text1, (10, 10))

another_font = pygame.font.Font("GenRyuMinTW_Regular.ttf", 40)
text2 = another_font.render('你好世界！', True, (0, 0, 0))
window.blit(text2, (10, 80))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
