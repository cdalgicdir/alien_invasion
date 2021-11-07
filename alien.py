import pygame

class Alien(Sprite):
    
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        