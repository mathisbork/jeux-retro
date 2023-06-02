import pygame


class SonManager:
    def __init__(self):
        self.sounds = {
            'start': pygame.mixer.Sound("Assets1/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("Assets1/sounds/game_over.ogg"),
            'bomb': pygame.mixer.Sound("Assets1/sounds/explosion.ogg"),
            'pan': pygame.mixer.Sound("Assets1/sounds/tir.ogg"),

        }

    def play(self, name):
        self.sounds[name].play()
