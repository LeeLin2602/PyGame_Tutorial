import pygame

pygame.init()

window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("PyGame - Image Sample Code")
window.fill((255, 255, 255))

img1 = pygame.image.load('pic1.jpg')
img2 = pygame.image.load('pic2.jpg')

window.blit(img1,(0, 0))
window.blit(img2,(600, 0))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
