from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_img,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(26,140))
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
win_width = 700
win_height = 500
racket = Player('racket.png',10,400,5)
background = transform.scale(image.load('white_bkg.png'),(win_width,win_height))
win = display.set_mode((win_width,win_height))
display.set_caption('pp2')
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))
    racket.update()
    racket.drop()
    display.update()
