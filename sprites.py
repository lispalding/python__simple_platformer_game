# MADE BY: Lisette Spalding
# FILE NAME: sprites.py
# PROJECT NAME: python__simple_platformer_game
# DATE CREATED: 04/01/2021
# DATE LAST MODIFIED: 04/18/2021
# PYTHON VER. USED: 3.8

##################### IMPORTS #####################
import pygame as pg
import random as r
from os import *

# Custom Imports
from settings import *
#################### FINISHED #####################

################### GLOBAL VAR ####################
vec = pg.math.Vector2
#################### FINISHED #####################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PURPLE)

        # self.image = playerImage # Setting the player image

        self.rect = self.image.get_rect()

        ## Placement
        self.rect.center = (WIDTH/2, HEIGHT/2)
        ## Placement FIN

        ## Movement Variables:
        self.position = vec(WIDTH / 2, HEIGHT / 2)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        ## Movement Variables FIN

        self.keypressed = False

    def togglePressed(self):
        self.keypressed = False

    def update(self):
        """ To use: self.update()
        This is the function that will update the movement of the player character. """
        ##### !! Basic Movement !! #####
        self.acceleration = vec(0, 0.5)

        # Cheking the Keystate
        keystate = pg.key.get_pressed()

        ########## !!!! .. FLOW MOVEMENT .. !!!! ##########
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.acceleration.x += -PLAYER_ACCELERATION

        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.acceleration.x = PLAYER_ACCELERATION

        ## Player Movement Calculations
        self.acceleration.x += self.velocity.x * PLAYER_FRICTION # Applying friction

        # Equations of motion:
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        ########## !!!! .. FLOW FINISHED .. !!!! ##########

        # Setting the screen-wrapping for left and right (Sides of the screen)
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH

        # !! Back to movement !!
        self.rect.midbottom = self.position
        # !! Movement-2 FIN !!

class Platform(pg.sprite.Sprite):
    """ To use: Platform()
    This is the Platform class. This class creates and maintains every platform that appears on the screen. """
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)

        # Setting up the Platform image:
        self.image = pg.Surface((width, height))
        self.image.fill(YELLOW_GREEN)
        # Platform Image FIN

        # Setting up the boundary rectangle:
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Rectangle FIN