import pygame
from random import randint
from time import time

pygame.init()

window = pygame.display.set_mode((390,390))
pygame.display.set_caption("PyGame - OOXX")

imgo = pygame.transform.scale(pygame.image.load('o.png'), (128, 128))
imgx = pygame.transform.scale(pygame.image.load('x.png'), (128, 128))

class Block:
    def __init__(self, r, c):
        # 0 -> empty
        # 1 -> O
        # 2 -> X
        self.type = 0
        self.r = r
        self.c = c
    
    def turn(self, round_):
        if self.type:
            return False
        if round_ == 0:
            self.type = 1
        else:
            self.type = 2
        return True

    def blit(self, window):
        if self.type == 1:
            window.blit(imgo, (self.r * 130, self.c * 130))
        elif self.type == 2:
            window.blit(imgx, (self.r * 130, self.c * 130))


class Game:
    def __init__(self):
        self.blocks = [[], [], []]
        self.round_ = 0
        for i in range(3):
            for j in range(3):
                self.blocks[i].append(Block(i, j))

    def click(self, x, y):
        if self.round_ == -1:
            return

        x //= 129
        y //= 129
        if self.blocks[x][y].turn(self.round_):
            self.round_ = not self.round_

    def blit(self, window):
        pygame.draw.rect(window, (0, 0, 0), (128,0,2,390)) 
        pygame.draw.rect(window, (0, 0, 0), (258,0,2,390))
        pygame.draw.rect(window, (0, 0, 0), (0,128,390,2))
        pygame.draw.rect(window, (0, 0, 0), (0,258,390,2))

        for r, row in enumerate(self.blocks):
            for c, blk in enumerate(row):
                blk.blit(window)

        if self.isSet():
            self.round_ = -1

        pygame.display.flip()

    def isSet(self):
        for i in range(3):
            if self.blocks[i][0].type != 0 and self.blocks[i][0].type == self.blocks[i][1].type and self.blocks[i][1].type == self.blocks[i][2].type:
                pygame.draw.rect(window, (255, 0, 0), (128 * i + 64,10,10,370))
                return True
            if self.blocks[0][i].type != 0 and self.blocks[0][i].type == self.blocks[1][i].type and self.blocks[1][i].type == self.blocks[2][i].type:
                pygame.draw.rect(window, (255, 0, 0), (10,128 * i + 64,370,10))
                return True

        for i in range(3):
            for j in range(3):
                if self.blocks[i][j].type == 0:
                    return False

        return True

#### --- 進入遊戲 --- ####

while True:

    window.fill((255, 255, 255))
    game = Game()

    while not game.isSet():

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                game.click(x, y)

        game.blit(window)

    del game

    # 點一下繼續遊戲
    flg = 1
    while flg:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                flg = 0