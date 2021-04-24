# MADE BY: Lisette Spalding
# FILE NAME: main.py
# PROJECT NAME: python__simple_platformer_game
# DATE CREATED: 04/01/2021
# DATE LAST MODIFIED: 04/24/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import *

# Custom Imports
from settings import *
from sprites import *
################### FINISHED ###################

################ MAIN GAME LOOP ################
####### Game class #######
class Game(object):
    """ To use: Game()
    This class runs the main game. """
    def __init__(self):
        self.running = True

        pg.init()  # Initializing Pygame Library
        pg.mixer.init()  # Sounds

        # Initializing display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)

        # Initializing clock
        self.clock = pg.time.Clock()

    def new(self):
        """ To use: self.new()
        This method creates a new game. """
        # Creating the sprite groups
        self.allSprites = pg.sprite.Group() # All sprites group
        self.playerGroup = pg.sprite.Group() # Player group
        self.platformsGroup = pg.sprite.Group() # Platform group

        ## Creating the game objects
        self.player = Player()
        # Adding player to sprite groups
        self.allSprites.add(self.player)
        self.playerGroup.add(self.player)

        # Spawning base platform
        basePlatform = Platform(0, HEIGHT - 40, WIDTH, 40)
        # Adding platform to group
        self.allSprites.add(basePlatform)
        self.platformsGroup.add(basePlatform)

        # Other Platforms adding
        plat1 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.allSprites.add(plat1)
        self.platformsGroup.add(plat1)

        # Start running game loop...
        self.run()

    def run(self):
        """ To use: self.run()
        This method runs the game. """
        ## Game loop
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)

            # Processing input events
            self.events()

            # Processing updated variables
            self.update()

            # Creating the images on the screen
            self.draw()

    def events(self):
        """ To use: self.events()
        This method keeps track of the events that happen throughout running the game. """
        for event in pg.event.get():
            # Check for closing windows:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

    def update(self):
        """ To use: self.update()
        This method updates what is shown on the HUD. """
        self.allSprites.update()

        # Collision check between player and platforms
        hits = pg.sprite.spritecollide(self.player, self.platformsGroup, False)
        if hits:
            self.player.position.y = hits[0].rect.top
            self.player.velocity.y = 0

    def draw(self):
        """ To use: self.draw()
        This method draws the content on the screen. """
        self.screen.fill(BLACK)

        self.allSprites.draw(self.screen)

        ## This is the very last thing to happen during the draw:
        pg.display.flip()

    def showStartingScreen(self):
        """ To use: self.showStartingScreen()
        This method shows the starting screen. """
        pass

    def showGameOverScreen(self):
        """ To use: self.showGameOverScreen()
        This method shows the game over screen. """
        pass

####### Finished #######

g = Game() # Defining the game start

g.showStartingScreen() # Showing the starting screen for the new game

while g.running:
    g.new() # This kicks off the actual game loop
    g.showGameOverScreen()

# If the loop ever breaks this happens:
pg.quit()
################### FINISHED ###################