"""Pearl Class."""
from player import Player
import pygame
from pygame.locals import *

class Pearl:
    """Pearl/ jump boost."""
    pearls: list[pygame.Rect]

    # TODO init (pearl_list)
    def __init__(self, x_pos: float, y_pos: float):
        self.x_pos = x_pos
        self.y_pos = y_pos

    # TODO define collect
    # Pearl is collected by player and disappears
    def collect(self):
        """When player collides into pearl. The pearl should disappear."""
        destroy pearls


    # TODO define respawn
    # Either timer or tracks player jumps. 