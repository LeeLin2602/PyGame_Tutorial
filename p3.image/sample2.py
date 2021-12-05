import pygame

pygame.init()

window = pygame.display.set_mode((600,440))
pygame.display.set_caption("PyGame - Image Sample Code")
window.fill((255, 255, 255))

img1 = pygame.image.load('pic1.jpg')
img2 = pygame.image.load('pic2.jpg')
img1 = pygame.transform.scale(img1, (300, 440))
img2 = pygame.transform.scale(img2, (300, 440))
img1 = pygame.transform.rotate(img1, 1)

window.blit(img1,(0, 0))
window.blit(img2,(300, 0))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
