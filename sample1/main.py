import pygame
from random import randint
from time import time

pygame.init()

window = pygame.display.set_mode((600,440))
pygame.display.set_caption("PyGame - Typing Practice")
window.fill((255, 255, 255))

img0 = pygame.image.load('keyboard.png')
img0 = pygame.transform.scale(img0, (600, 200))

small_font = pygame.font.Font("GenRyuMinTW_Regular.ttf", 30)
big_font = pygame.font.Font("GenRyuMinTW_Regular.ttf", 120)
txt0 = small_font.render('參考鍵盤：', True, (0, 0, 0))
txt1 = small_font.render("請按：", True, (0,0,0))

score = 0

def Loss():
    msg = big_font.render("你輸了", True, (255,0,0))
    window.blit(msg, (200, 10))
    pygame.display.flip()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)

notStart = 1


#### --- 準備進入遊戲 --- ####

msg = small_font.render("任意鍵開始遊戲！", True, (0,0,0))
window.blit(msg, (150, 150))
pygame.display.flip()

while notStart:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        if e.type == pygame.KEYDOWN:
            notStart = 0

#### --- 進入遊戲 --- ####

while True:

    ans = randint(0, 25) + ord('a')

    txt2 = big_font.render(chr(ans).upper(), True, (0, 0, 0))
    txt5 = big_font.render(chr(ans).upper(), True, (0, 0, 0))

    TL = time()

    while True: # 等待使用者回應
        remain = max(0, round(TL + 2 - time(), 2)) 
        txt3 = small_font.render("你還剩下：" + str(remain) + " 秒", True, (0, 0, 0))
        txt4 = small_font.render("你得到了：" + str(score) + " 分", True, (0, 0, 0))
        flg = 0

        window.fill((255, 255, 255))
        window.blit(img0,(0, 240))
        window.blit(txt0, (0, 200))
        window.blit(txt1, (20, 120))
        window.blit(txt2, (100, 60))
        window.blit(txt3, (200, 160))
        window.blit(txt4, (360, 200))
        pygame.display.flip()
        
        if remain == 0:
            Loss()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)
            if e.type == pygame.KEYDOWN:
                if ord('a') <= e.key <= ord('z'):
                    if e.key == ans:
                        score += 1
                        flg = 1
                    else:
                        Loss()

        if flg: 
            break
