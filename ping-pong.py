from pygame import *
import random
class GameSprite(sprite.Sprite):
    size = (26, 140)
    def __init__(self,player_img,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),self.size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def drop(self):
        win.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    size = (28, 28)
    speed_x = 1
    speed_y = 1
    def update(self):
        self.rect.y += self.speed_y * self.speed
        self.rect.x += self.speed_x * self.speed

        if self.rect.x > win_width-28:
            self.speed_x = -1

        if self.rect.y >= win_height-28:
            self.speed_y = -1
    
        if self.rect.y <= 0:
            self.speed_y = 1

        if self.rect.x <= 0:
            self.speed_x = 1




win_width = 700
win_height = 500
racket = Player('racket.png',10,400,5)
racket2 = Player2("racket.png", win_width-36,400,5)
ball = Enemy("bal.png",350, 100, 2)
background = transform.scale(image.load('white_bkg.png'),(win_width,win_height))
win = display.set_mode((win_width,win_height))
display.set_caption('pp2')
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(ball, racket2) or sprite.collide_rect(ball, racket):
        ball.speed_x = ball.speed_x * -1
    win.blit(background, (0, 0))
    ball.update()
    ball.drop()
    racket.update()
    racket.drop()
    racket2.update()
    racket2.drop()
    display.update()
