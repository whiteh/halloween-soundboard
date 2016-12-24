## Halloween Soundboard
## Mark Greenwood for WythyDojo (@wythydojo)
## To be used with makey-makey and pumpkins

## Python 2.7 and Pygame - http://www.pygame.org/download.shtml

import pygame

pygame.init()
screen = pygame.display.set_mode((1,1))
pygame.mixer.init(frequency=22050,channels=4)

## Sounds from http://soundbible.com/
files = [
        './wav/evil_laugh.wav',
        './wav/witches_laugh.wav',
        './wav/bat.wav'
    ]

def play(index):
    sound = pygame.mixer.Sound(files[index])
    chan = pygame.mixer.Channel(index)
    chan.queue(sound)

def play1(index):
    pygame.mixer.music.load(files[index])
    pygame.mixer.music.play(0)
    

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play(0)
                print "Up key"
            if event.key == pygame.K_DOWN:
                play(1)
                print "Down key"
            if event.key == pygame.K_LEFT:
                play(2)
                print "Left key"
