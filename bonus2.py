import pygame
import random

class Bonus2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bonus2.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(900, 1500 - self.rect.width)
        self.rect.y = 600
        self.timer = 0
        self.visible = False


    def update(self):
        self.timer += 1

        if not self.visible:
            if self.timer >= 10 * 60:
                self.rect.x = random.randint(900, 1500 - self.rect.width)
                self.rect.y = 600
                self.visible = True
                self.timer = 0


    def reset(self):
        self.timer = 0
        self.visible = False




class BonusBoost(Bonus2):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bonus2.png")
        self.rect = self.image.get_rect()

    def apply_bonus(self, player):
        player.damage += 0.02