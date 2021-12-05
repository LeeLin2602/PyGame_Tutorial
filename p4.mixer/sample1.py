import pygame

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Mixer Sample Code")
window.fill((255, 255, 255))

pygame.mixer.set_num_channels(1)
audio = pygame.mixer.Sound("bgm.mp3")

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mixer.Channel(0).get_busy():
                pygame.mixer.Channel(0).stop()
            pygame.mixer.Channel(0).play(audio, loops = -1)
