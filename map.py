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
    def __init__(self, width: float, height: float, platforms_list: list[pygame.Rect] = [], entrances: list[pygame.Rect] = []):
        self.width = width
        self.height = height
        self.platforms = platforms_list
        self.enterances = entrances

    # TODO define render
    # Renders each object 
    def render(self, screen, pearls: list[pygame.Rect]):
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
            platform.x += x_speed
        for pearl in pearls:
            pearl.x += x_speed
    
    def move_right(self, pearls: list[pygame.Rect], x_speed: float):
        """ Moves the map to the left to illusion right movement."""
        for platform in self.platforms:
            platform.x -= x_speed
        for pearl in pearls:
            pearl.x -= x_speed

    def move_jump(self, y_vel: float, pearls: list[pygame.Rect]) -> float:
        """Lowers the map down to give illusiion of jumping."""
        GRAVITY_ACCEL: float = -0.5
        for platform in self.platforms:
            platform.y += y_vel
        for pearl in pearls:
            pearl.y += y_vel
        y_vel += GRAVITY_ACCEL
        return y_vel


    # TODO define load_room
    # Connects enterances in each room
    def load_room(self):
        ...