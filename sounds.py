import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'start': pygame.mixer.Sound("assets/sounds/start.mp3"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'bomb': pygame.mixer.Sound("assets/sounds/bomb.ogg"),
            'pan': pygame.mixer.Sound("assets/sounds/pan.mp3"),
            'mort': pygame.mixer.Sound("assets/sounds/mort.mp3"),
            'bonus': pygame.mixer.Sound("assets/sounds/bonus.mp3")

        }

    def play(self, name):
        self.sounds[name].play()
