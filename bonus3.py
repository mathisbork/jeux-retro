import pygame
import random

class Bonus3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bonus4.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(800, 1500 - self.rect.width)
        self.rect.y = 40
        self.timer = 0
        self.visible = False


    def update(self):
        self.timer += 1

        if not self.visible:
            if self.timer >= 17 * 60:
                self.rect.x = random.randint(800, 1500 - self.rect.width)
                self.rect.y = 530
                self.visible = True
                self.timer = 0


    def reset(self):
        self.timer = 0
        self.visible = False




class BonusBoost3(Bonus3):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bonus4.png")
        self.rect = self.image.get_rect()

    def apply_bonus2(self, player):
        player.velocity += 5