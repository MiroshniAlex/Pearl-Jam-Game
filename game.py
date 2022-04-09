"""Main Game Running Space."""

# Import Libraries
import pygame
from pygame.locals import *
# import random if needed
import sys

# Import custom classes
from map import Map
from player import Player

# Inintialize Pygame
pygame.init()

# Clock to control frame rate 
clock = pygame.time.Clock()
clock.tick(1)

# Define screen height and width
SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600

# Key presses bool
key_press_right: bool = False
key_press_left: bool = False

# Set up the drawing window and size
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set up platforms and pearls
platform1: pygame.Rect = pygame.Rect(-1000, 590, 6000, 10)
platform2: pygame.Rect = pygame.Rect(300, 400, 150, 10)
platform3: pygame.Rect = pygame.Rect(100, 200, 150, 10)
platform4: pygame.Rect = pygame.Rect(400, 10, 150, 10)
platform5: pygame.Rect = pygame.Rect(700, -250, 150, 10)

platforms: list[pygame.Rect] = [platform1, platform2, platform3, platform4, platform5]
pearls: list[pygame.Rect] = [pygame.Rect(125, 190, 10, 10)]

# TODO Instantiate Rooms
room1: Map = Map(600, 600, 0, platforms)

# TODO Instantiate Player
PLAYER_SPEED: float = 1
GRAVITY_ACCEL: float = -.004
PLAYER_HEIGHT: float = 20.0
PLAYER_WIDTH: float = 20.0
player: Player = Player(PLAYER_HEIGHT, PLAYER_WIDTH, 100, 500)

# Defining platform collision check function
def player_platform_collision(room: Map, player: Player) -> bool:
    for platform in room1.platforms:
        if platform.colliderect(player.rect):
            return True
    return False

# Run the game until the user asks to quit or dies and `running` is set to False
running = True

# Game loop
while running:
    
    # Background fill
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():

        # Check for QUIT event (user closes window). If QUIT, then set running to false.
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        # TODO Check if user presses down on a key and if colliding with wall/platform
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_on_plat = False
                for platform in room1.platforms:
                    if platform.y == (player.rect.y + PLAYER_HEIGHT):
                        player_on_plat = True
                if player_on_plat is True:
                    room1.y_vel = 2
                    room1.move_down(pearls)

            elif event.key == pygame.K_d:
                if player_platform_collision(room1, player) is False:
                    key_press_right = True

            elif event.key == pygame.K_a:
                if player_platform_collision(room1, player) is False:
                    key_press_left = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if player_platform_collision(room1, player) is False:
                    key_press_right = False
            
            elif event.key == pygame.K_a:
                if player_platform_collision(room1, player) is False:
                    key_press_left = False

    if key_press_right:
        room1.move_right(pearls, PLAYER_SPEED)

    if key_press_left:
        room1.move_left(pearls, PLAYER_SPEED)

    # Jumping...
    if player_platform_collision(room1, player) is False:
        room1.move_jump(pearls)
        room1.y_vel += GRAVITY_ACCEL
    
    # Moves player to top of platform if collides.
    for platform in room1.platforms:
        collision = False
        if platform.colliderect(player.rect):
            collision = True
        if collision and player.rect.y < platform.y:
            room1.move_down(pearls, player.rect.y - platform.y + PLAYER_HEIGHT)
            room1.y_vel = 0
        elif collision and player.rect.y > platform.y:
            room1.move_down(pearls, -5)

    
    # Updating all models
    room1.render(screen, pearls)
    player.render(screen)

    pygame.display.flip()