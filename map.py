"""Map class."""

import pygame
from pygame.locals import *

class Map:
    """Map class holds all platforms, walls, exits, entrances, and pearls."""
    width: int
    height: int
    platforms: list[pygame.Rect]
    entrances: list[pygame.Rect]
    
    # TODO init (screen_width, screen_height, platform_list, walls, enterances)
    def __init__(self, width: float, height: float, y_vel: float = 0, platforms_list: list[pygame.Rect] = [], entrances: list[pygame.Rect] = []):
        self.width = width
        self.height = height
        self.y_vel = y_vel
        self.platforms = platforms_list
        self.enterances = entrances

    # TODO define render
    # Renders each object 
    def render(self, screen, pearls: list[pygame.Rect] = []):
        """Renders pearls and platforms."""
        PLAT_COLOR: tuple(int) = (105, 88, 51)
        PEARL_COLOR: tuple(int) = (242, 235, 218)
        PEARL_RADIUS: int = 10
        for platform in self.platforms:
            pygame.draw.rect(screen, PLAT_COLOR, platform)
        for pearl in pearls:
            pygame.draw.circle(screen, PEARL_COLOR, (pearl.centerx, pearl.centery), PEARL_RADIUS)

    # Moves map around player
    def move_left(self, pearls: list[pygame.Rect], x_speed: float):
        """Moves the map to the right to illusion left movement."""
        for platform in self.platforms:
            platform.move_ip(x_speed, 0)
        for pearl in pearls:
            pearl.move_ip(x_speed, 0)
    
    def move_right(self, pearls: list[pygame.Rect], x_speed: float):
        """ Moves the map to the left to illusion right movement."""
        for platform in self.platforms:
            platform.move_ip(-x_speed, 0)
        for pearl in pearls:
            pearl.move_ip(-x_speed, 0)

    def move_down(self, pearls: list[pygame.Rect], dist: float = 5):
        """To fix glitch where player gets stuck in platform and cant move."""
        for platform in self.platforms:
            platform.move_ip(0, dist)
        for pearl in pearls:
            pearl.move_ip(0, dist)

    def move_jump(self,  pearls: list[pygame.Rect]):
        """Lowers the map down to give illusiion of jumping."""
        pixel_threshold: float = 0.3
        for platform in self.platforms:
            if self.y_vel < 1 and self.y_vel > pixel_threshold:
                platform.move_ip(0, 1)
            elif self.y_vel > -1 and self.y_vel < -pixel_threshold:
                platform.move_ip(0, -1)
            else: 
                platform.move_ip(0, self.y_vel)
        for pearl in pearls:
            if self.y_vel < 1 and self.y_vel > pixel_threshold:
                pearl.move_ip(0, 1)
            elif self.y_vel > -1 and self.y_vel < -pixel_threshold:
                pearl.move_ip(0, -1)
            else: 
                pearl.move_ip(0, self.y_vel)

    # TODO define load_room
    # Connects enterances in each room
    def load_room(self):
        ...