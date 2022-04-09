"""Main Game Running Space."""

# Import Libraries
import pygame
from pygame.locals import *
# import random if needed
import sys

# Import custom classes

# Inintialize Pygame
pygame.init()

# Clock to control frame rate 
clock = pygame.time.Clock()

# TODO Instantiate Rooms

# TODO Instantiate Player

# Define screen height and width
SCREEN_WIDTH: int = 500
SCREEN_HEIGHT: int = 500

# Set up the drawing window and size
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run the game until the user asks to quit or dies and `running` is set to False
running = True

# Game loop
while running:
    for event in pygame.event.get():
        # Check for QUIT event (user closes window). If QUIT, then set running to false.
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # TODO Check if user presses down on a key
        