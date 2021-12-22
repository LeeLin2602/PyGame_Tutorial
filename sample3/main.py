import pygame
from random import randint, shuffle
from time import time

pygame.init()

window = pygame.display.set_mode((1600,900))
pygame.display.set_caption("PyGame - 接龍")

font = pygame.font.SysFont(None, 25)
suits = [pygame.transform.scale(pygame.image.load('flower.png'), (18, 20))]
ranks = [font.render(j, True, (0, 0, 0)) for j in [str(i) for i in range(11)] + ['J', 'Q', 'K']]

class Card:
    # 這是一張撲克牌
    def __init__(self, suit, rank):
        self.s = suit
        self.r = rank

    def blit(self, focus = 0):
        # blit 會回傳一個可以被繪製的物件
        # 可以用 window.blit(x.blit(), (x, y))
        obj = pygame.Surface((100, 140))
        obj.fill((255, 255, 255))

        if focus == 0:
            pygame.draw.rect(obj, (0, 0, 0), [0, 0, 100, 140], 3)
        else:
            pygame.draw.rect(obj, (255, 0, 0), [0, 0, 100, 140], 9)

        obj.blit(suits[self.s], (5, 5))
        obj.blit(ranks[self.r], (9, 30))
        obj.blit(ranks[self.r], (27, 7))
        return obj

class Pool:
    # 代表卡池，也就是維護剩下的卡片
    def __init__(self):
        self.cards = []

        # 初始化加入三副花色相同的牌
        for i in range(3):
            for j in range(1, 14):
                self.cards.append(Card(0, j))

        shuffle(self.cards) # 洗牌

    def remaining(self):
        return len(self.cards)

    def pop(self):
        
        # 把牌組中最上面的一張牌拿出去，可能是發牌，或是補牌

        if len(self.cards):
            return self.cards.pop()
        else:
            return None

class Pane:
    # 手牌
    def __init__(self, pool):
        # 初始化的時候抽 6 張牌加入手牌
        self.pool = pool
        self.hand = []
        for i in range(6):
            self.hand.append(self.pool.pop())
        self.focus = -1

    def setFocus(self, focus):
        # Focus 代表那張手牌正在被點選
        self.focus = focus
        self.focus = max(self.focus, -1)
        self.focus = min(self.focus, len(self.hand) - 1)

    def width(self):
        # 會回傳手牌物件的寬度，來判斷有沒有點擊到手牌
        return 100 + max(len(self.hand) - 1, 0) * 28

    def blit(self):
        obj = pygame.Surface((500, 140))
        obj.fill((13, 139, 58))

        pygame.draw.rect(obj, (0, 0, 0), [0, 0, 100, 140], 3)
        txt = font.render("X" + str(self.pool.remaining()), True, (0, 0, 0))

        obj.blit(txt, (65, 120))

        for i in range(len(self.hand)):
            obj.blit(self.hand[i].blit(self.focus == i), (150 + 28 * i, 0))

        return obj

class Slot():
    # 一個上面的區塊，可以讓你調整牌面
    def __init__(self, pool = None):
        # 初始化的時候抽 5 張牌
        self.cards = []
        if pool:
            for i in range(5):
                self.cards.append(pool.pop())
        self.focus = -1

    def height(self):
        # 會回傳 slot 物件的高度，來判斷有沒有點擊到 slot
        if len(self.cards) <= 1:
            return 140
        else:
            return 140 + max(0, len(self.cards) - 1) * 26

    def blit(self):
        obj = pygame.Surface((100, 600))
        obj.fill((13, 139, 58))
        pygame.draw.rect(obj, (0, 0, 0), [0, 0, 100, 140], 1)

        for i in range(len(self.cards)):
            obj.blit(self.cards[i].blit(), (0, 26 * i))

        if self.focus != -1:
            pygame.draw.rect(obj, (255, 0, 0), [0, self.focus * 26, 100, self.height() - self.focus * 26], 6)

        return obj

    def setFocus(self, focus):
        # Focus 代表那一個 slot 的某部分牌正在被選取
        self.focus = focus
        self.focus = min(self.focus, len(self.cards) - 1)
        self.focus = max(self.focus, -1)
        for i in range(self.focus + 1, len(self.cards)):
            if self.cards[i].r != self.cards[i - 1].r + 1:
                self.focus = -1
                return

    def merge(self, segment):
        # 要有牌從手牌或是其他 slot 被移動過來
        if len(self.cards) == 0:
            self.cards = segment
            self.focus = -1
            return 1
        elif segment[0].r == self.cards[-1].r + 1:
            self.cards += segment
            self.focus = -1
            return 1
        return 0

class Game():
    # 一局遊戲
    def __init__(self):
        self.pool = Pool()
        self.slots = []
        # 一局遊戲會有 8 個 slot
        for i in range(4):
            self.slots.append(Slot(self.pool))
        for i in range(4):
            self.slots.append(Slot())

        shuffle(self.slots) # 隨機調換 slot 的位置，讓他看起來更隨機

        self.pane = Pane(self.pool)
        self.focus = None

    def setFocus(self, area, card):
        pa = pc = na = None
        if self.focus:
            # 把舊的資料記錄起來並且清除掉
            pa, pc = self.focus
            if pa == "pane":
                self.pane.focus = -1

            for i in range(8):
                if pa == "slot" + str(i):
                    self.slots[i].setFocus(-1)
                    pa = i

        self.focus = [area, card]
        
        if area == None:
            self.focus = None
            return

        # 如果是摸手牌
        if area == "pane":
            self.pane.setFocus(card)
            self.focus[1] = self.pane.focus
            na = area
            nc = self.focus[1]

        # 如果是摸某個 slot
        for i in range(8):
            if area == "slot" + str(i):
                self.slots[i].setFocus(card)
                self.focus[1] = self.slots[i].focus
                na = i
                nc = self.focus[1]

        if pa == None:
            return
        elif type(pa) == int and type(na) == int and pa != na and pc != -1:
            # 從某個 slot 轉移到另一個 slot
            segment = self.slots[pa].cards[pc:]
            if self.slots[na].merge(segment):
                self.slots[pa].cards = self.slots[pa].cards[:pc]
        elif pa == "pane" and type(na) == int and pc != -1:
            # 從手牌轉移到某個 slot
            segment = [self.pane.hand[pc]]
            if self.slots[na].merge(segment):
                self.pane.hand[pc] = self.pool.pop()
                if self.pane.hand[pc] == None:
                    del self.pane.hand[pc]

    def blit(self):
        obj = pygame.Surface((1600,900))
        obj.fill((13, 139, 58))
        obj.blit(self.pane.blit(), (100, 700))

        for i in range(len(self.slots)):
            obj.blit(self.slots[i].blit(), (300 + i * 150, 80))

        return obj

#### --- 進入遊戲 --- ####


game = Game()

while True:

    window.blit(game.blit(), (0, 0))
    pygame.display.flip()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            exit(0)

        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            flg = 1
            # 你摸到手牌，然後要點擊手牌
            if 250 <= x <= 250 + game.pane.width() and 700 <= y <= 840:
                # pane
                x = (x - 250) // 28
                game.setFocus("pane", x)
                flg = 0
            # 摸某個 slot
            for i in range(8):
                if 300 + i * 150 <= x <= 300 + i * 150 + 100 and 80 <= y <= 80 + game.slots[i].height():
                    game.setFocus("slot" + str(i), (y - 80) // 26)
                    flg = 0
            # 如果是無效點擊，就把舊的紀錄清除掉
            if flg:
                game.setFocus(None, None)