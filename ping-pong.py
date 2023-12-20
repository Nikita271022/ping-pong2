from pygame import *
win_width = 700
win_height = 500

win = display.set_mode((win_width,win_height))
display.set_caption('pp2')
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False