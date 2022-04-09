"""Player class."""

import pygame
from pygame.locals import *

class Player:
    """Player movement, updating, rendering, speed, acceleration."""
    rect: pygame.Rect

    def __init__(self, player_height: float, player_width: float, x_pos: float = 30, y_pos: float = 400):
        """Constructor definition for Player class!"""
        self.rect = pygame.Rect(x_pos, y_pos, player_width, player_height)

    def render(self, screen):
        """Draws player."""
        RED: tuple(int) = (255, 0, 0)
        pygame.draw.rect(screen, RED, self.rect)