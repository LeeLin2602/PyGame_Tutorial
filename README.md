---
tags: TA, Course, NCTU
---
# PyGame

## PyGame 介紹

PyGame 是一個跨平台的 Python 模組，提供了圖像、音頻的支援，讓使用者可以利用 PyGame 來快速開發遊戲，且便於移植到其他平台。

### 安裝 PyGame

在使用 PyGame 之前，我們必須要先安裝它，可以利用 pip 來進行 Python 模組的安裝：
```
$ pip install pygame
```

### 遊戲是怎麼產生的？

- 其實電腦是利用快速切換圖片來讓我們誤以為它是連續的影像
	- 切換圖片的速度就被稱為幀率，常用單位是 fps（frame per second），代表一秒會刷新幾次。
- 我們想要動態的遊戲畫面，我們就需要一直去刷新遊戲畫面，所以情理之上，我們可能會寫一個 function 來做畫面的渲染，即輸出那一瞬間的遊戲畫面，之後我們再利用可能定時器的方式，來不斷的呼叫這個畫面渲染的 function
	- 至於畫面要怎麼渲染，我們就會用 PyGame 提供的方式來把圖片堆砌起來
- 遊戲視窗會去捕捉使用者的操作，最常見的就是鍵盤操作和滑鼠操作
	- 使用者的操作會被紀錄起來，並且被稱之為一個事件（event），例如一個 MouseDown Event 然後可能會有參數 (x, y) 意味著使用者在視窗的 (x, y) 的位置按下了滑鼠。

### 一個簡單的範例程式

```python3=
import pygame # 引入 pygame 模組

pygame.init() # 初始化 pygame 模組

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("這是一隻 PyGame 的範例程式")
window.fill((255, 255, 255))

pygame.display.flip() # 顯示 window

while True:
	# 捕捉 pygame 接受到的事件，並且針對關閉視窗的事件做處理
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
```

這是一隻很簡單的程式，他會：
1. 創建一個新的視窗
	- 設置大小為 800x450
	- 設置標題為 「這是一隻 PyGame 的範例程式」
	- 用白色來填充視窗
2. 顯示這個視窗
3. 不斷的捕捉事件
	- 如果是關閉視窗的事件，就結束程式

### 此篇教學文會涵蓋到的部分

我們會介紹 PyGame 提供的以下功能：
- `pygame.font`：可以幫助我們輸出一段文字在視窗上。
- `pygame.event`：可以幫助我們捕捉、處理使用者觸發的事件。
- `pygame.image`：可以幫助我們輸出一張圖片在視窗上。
- `pygame.mixer`：可以幫助我們播放出聲音。

## 正文

### p1.font.sample1 用預設字體輸出文字

```python3=
import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Font Sample Code")
window.fill((255, 255, 255))

########## 重點開始 ##########

default_font = pygame.font.SysFont(None, 40)
text1 = default_font.render('Hello World!', True, (0, 0, 0))
window.blit(text1, (10, 10))

########## ------- ##########

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
```

這份 code 和前一份長的差不多，只是中間多出一段文字渲染的程式碼：
- 用 `pygame.font.SysFont` 來抓系統字體：
	- 我們用 `SysFont(name, size, bold=False, italic=False)` 來引入一個字體，之後才會用這個字體去渲染文字
	- 其中 `name` 表示字體的名稱，`None` 代表預設字體；`size` 表示大小；`bold` 表示是否粗體；`italic` 表示是否斜體。
- 用 `font.render` 來渲染文字：
	- `font.render(text, antialias, color, background=None)` 會使用該字體來去渲染 `text` 這段文字
	- 其中 `antialias `代表是否開啟抗鋸齒；顏色用 RGB 表示；background 代表背景色，預設是透明。
- 之後我們還要把這段文字在視窗渲染出來：
	- `window.blit(text1, (10, 10))` 代表在 window 上面的 (10, 10) 這個位置渲染我們剛剛宣告出的 text1 這段文字。

效果大概長這樣：
![](https://i.imgur.com/Ctttwrl.png)

### p1.font.sample2 用其他字體輸出文字

實際上除了預設字體外，我們完全可以上網找自己喜歡的字體，並且在自己的遊戲當中使用該字體，而 PyGame 也支援我們使用非系統字體來進行文字渲染：

```
import pygame

pygame.init()

window = pygame.display.set_mode((800,450))
pygame.display.set_caption("PyGame - Font Sample Code")
window.fill((255, 255, 255))

default_font = pygame.font.SysFont(None, 40, False, True)
text1 = default_font.render('Hello World!', True, (0, 0, 0))
window.blit(text1, (10, 10))

########## 重點開始 ##########

another_font = pygame.font.Font("GenRyuMinTW_Regular.ttf", 40)
text2 = another_font.render('你好世界！', True, (0, 0, 0))
window.blit(text2, (10, 80))

########## ------- ##########

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)

```

這份 code 也和前一份長的差不多，只是中間又多出一段文字渲染的程式碼：
- 我們用 `pygame.font.Font` 來引入不同的字體，這邊我引入了 `GenRyuMinTW_Regular.ttf` 這個文件，他是一個中文字體的字體檔。
- 我們用類似的方式把他渲染出來。

效果圖如下：
![](https://i.imgur.com/keynTVe.png)

### p2.event.sample1 捕捉滑鼠按下事件

```python3=
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
```

這份 code 也和最前一份長的差不多，只是下面多出一段捕捉事件的程式碼：
- 和捕捉 `pygame.QUIT`（按下關閉視窗的事件）類似，我們用 `pygame.MOUSEBUTTONDOWN` 來表示滑鼠被按下的事件；
- 我們用 `pygame.mouse.get_pos()` 來取得現在滑鼠所在的位置，並且在該位置輸出一個愛心 <3。

效果圖如下：
![](https://i.imgur.com/kLIOYKW.png)

### p2.event.sample2 捕捉鍵盤按下事件

```python3=
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
```

這份 code 和前一份長的很像，只是改成了偵測鍵盤事件，值得一提的事情是：
- `e.key` 回傳的是 ASCII 碼，所以如果是一般的字母、數字，可以用 `chr()` 這個函數將他們轉換成我們認識的樣子；但如果是一些特殊的字元，比如你按下 CapsLock，那程式就會報錯，**不是因為 PyGame 不支援特殊字元，而是因為我這邊想要用 `chr()` 把他輸出出來**。

效果圖如下：
![](https://i.imgur.com/wlKEBkj.png)

還有許多不同的 events，甚至哪怕是鍵盤滑鼠，也有分按下（Down）和彈起（Up）等不同的 event，族繁不及備載，這邊就不贅述了，有興趣的同學可以去讀 [Docs](https://www.pygame.org/docs/ref/event.html)。

### p3.image.sample1 渲染圖片

```python3=
import pygame

pygame.init()

window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("PyGame - Image Sample Code")
window.fill((255, 255, 255))

img1 = pygame.image.load('pic1.jpg')
img2 = pygame.image.load('pic2.jpg')

window.blit(img1,(0, 0))
window.blit(img2,(800, 0))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
```

這份 code 和前面的字體渲染長的很像，只是改成了圖片渲染。

效果圖如下：
![](https://i.imgur.com/beyLvVT.jpg)

不過兩張卡片的大小不一似乎挺令人困擾的，如果同一份素材可以在不同的地方隨我心意縮放，似乎會更方便？

### p3.image.sample2 圖片縮放

```python3=
import pygame

pygame.init()

window = pygame.display.set_mode((1200,450))
pygame.display.set_caption("PyGame - Image Sample Code")
window.fill((255, 255, 255))

img1 = pygame.image.load('pic1.jpg')
img2 = pygame.image.load('pic2.jpg')
img1 = pygame.transform.scale(img1, (600, 450))
img2 = pygame.transform.scale(img2, (600, 450))
img1 = pygame.transform.rotate(img1, 1)

window.blit(img1,(0, 0))
window.blit(img2,(600, 0))

pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
```

我們利用 `pygame.transform` 這個模組來幫助我們針對某個待渲染的東西做一些變換，例如這邊利用 `pygame.transform.scale` 來縮放一張圖片，把他改成 300x440 的大小；有利用 `pygame.transform.rotate` 來旋轉一張圖片，旋轉 1度。

效果圖如下：
![](https://i.imgur.com/sZXZSSi.jpg)

### p4.mixer.sample1 點擊播放 bgm

```
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

```

我們會利用 `pygame.mixer` 來幫助我們管理音訊：
- 首先我們利用 `pygame.mixer.init()` 來幫助我們初始化這個模組；
- 接著利用 `pygame.mixer.set_num_channels()` 來指定說我們需要多少個 channel
	- 有多少個 channel 意味著你可以同時在多少個音軌上做操作
- 接著我們用 `pygame.mixer.Sound()` 來載入一個音訊檔
- 最後當我們要播放的時候：
	- 我們先用 `pygame.mixer.Channel(0).get_busy()` 來取得 0 號 channel 是否在播放東西，如果在播放東西，我們就把他停止掉；
	- 否則我們就在 0 號 channel 上面播放那則音訊，其中 `loops = -1` 意味著不要循環播放。

至此，我們就學會了開發一個遊戲最基礎的一些元件，接下來就可以利用這些元件來拼湊出一款遊戲！

## 範例 - 打字練習

小時候電腦課會讓孩子進行打字練習，不如自己寫一個打字練習的程式吧！

```python3=

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
```

效果圖如下：
![](https://i.imgur.com/CGMMgrJ.png)

## 範例 - 魔塔遊戲

這是助教以前吃飽沒事幹用 PyGame 寫的遊戲，只使用了前面介紹的 4 個工具做出來的 RPG 遊戲，效果圖如下：
![](https://i.imgur.com/btEQi9N.png)

如果有興趣的話可以去看看[REPO](https://github.com/LeeLin2602/Mota-Magic-Tower)，可以給助教點星星喔～