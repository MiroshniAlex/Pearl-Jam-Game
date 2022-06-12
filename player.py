"""Player class."""

import pygame
from pygame.locals import RLEACCEL

class Player(pygame.sprite.Sprite):
    """Player movement, updating, rendering, speed, acceleration."""
    rect: pygame.Rect
    image: pygame.surface.Surface

    def __init__(self, player_height: float, player_width: float, x_pos: float = 30, y_pos: float = 400):
        """Constructor takes x, y, width, and height and makes rect out of it. And makes sprite."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pearl-Jam-Game/assets/player2.png").convert()
        self.rect = pygame.Rect(x_pos, y_pos, player_width, player_height)
        DEFAULT_IMAGE_SIZE = (20, 20)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        # self.image.set_colorkey(RLEACCEL)
        

    def render(self, screen):
        """Draws player."""
        # RED: tuple(int) = (255, 0, 0)
        # pygame.draw.rect(screen, RED, self.rect)
        screen.blit(self.image, self.rect)