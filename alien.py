import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initializae the aline and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        # self.image = pygame.image.load('images/alien.bmp') # Default alien
        # self.image = pygame.image.load('images/alien2.bmp') # Space color background alien
        self.image = pygame.image.load('images/tie-fighter.bmp') # Tie fighter
        self.rect = self.image.get_rect()

        # Start each new aliean near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)