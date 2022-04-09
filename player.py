"""Player class."""

import pygame
from pygame.locals import *

class Player:
    """Player movement, updating, rendering, speed, acceleration."""
    y_pos: float #arbitary values assigned to the position of the player
    x_pos: float
    rect: pygame.Rect




    def __init__(self, x_pos: float = 30, y_pos: float = 400 rect: pygame.Rect):
        """Constructor definition for Player class!"""
        self.rect = rect
        self.y_pos = y_pos
        self.x_pos = x_pos




