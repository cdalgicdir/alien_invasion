import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bomb_color

        self.rect = pygame.Rect(0, 0,
                                self.settings.bomb_width,
                                self.settings.bomb_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self) -> None:
        self.y -= self.settings.bomb_speed
        self.rect.y = self.y
    
    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.color, self.rect)