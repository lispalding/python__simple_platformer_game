# MADE BY: Lisette Spalding
# FILE NAME: sprites.py
# PROJECT NAME: python__simple_platformer_game
# DATE CREATED: 04/01/2021
# DATE LAST MODIFIED: 04/14/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import *
from settings import *
################### FINISHED ###################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(PURPLE)

        # self.image = playerImage
        #
        # self.rect = self.image.get_rect()

        ## Placement
        self.rect.center = (WIDTH/2, HEIGHT/2)
        ## Placement FIN

        self.speedx = 0
        self.speedy = 0

        self.keypressed = False

    def togglePressed(self):
        self.keypressed = False

    def update(self):
        """ To use: self.update()
        This is the function that will update the movement of the player character. """
        ##### !! Basic Movement !! #####
        # self.speedx = 0
        # self.speedy = 0

        # Cheking the Keystate
        keystate = pg.key.get_pressed()

        ########## !!!! .. FLOW MOVEMENT .. !!!! ##########
        # if keystate[pg.K_LEFT] or keystate[pg.K_a]:
        #     self.speedx += -5
        # if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
        #     self.speedx = 5
        # if keystate[pg.K_UP] or keystate[pg.K_w]:
        #      self.speedy = -5
        # if keystate[pg.K_DOWN] or keystate[pg.K_s]:
        #      self.speedy = 5
        #
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        ########## !!!! .. FLOW FINISHED .. !!!! ##########

        ####### !!!! .. BASIC GRID MOVEMENT .. !!!! #######
        # if (keystate[pg.K_LEFT] or keystate[pg.K_a]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += -50
        #
        # if (keystate[pg.K_RIGHT] or keystate[pg.K_d]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += 50
        #
        # if (keystate[pg.K_UP] or keystate[pg.K_w]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += -50
        #
        # if (keystate[pg.K_DOWN] or keystate[pg.K_s]) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centery += 50
        ####### !!!! .. BASIC GRID FINISHED .. !!!! #######

        ######### !!!! .. MOUSE MOVEMENT .. !!!! ##########
        # self.rect.center = (mousex, mousey) # Move Everywhere
        # self.rect.centerx = mousex  # Move Side to Side
        # self.rect.centery = mousey # Move Up and Down

        ########## .!. MOUSE CLICK AND DRAG
        if mouseBttnHeld:
            self.rect.center = (mousex, mousey)
        ########## .!. MOUSE CLICK AND DRAG FIN

        ######### !!!! .. MOUSE FINISHED .. !!!! ##########

        ##### !!!! .. SCREEN BINDING .. !!!! #####
        # We are binding the player to the screen area
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        ##### !!!! .. BINDING FINISH .. !!!! #####