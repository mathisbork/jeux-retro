import pygame

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bonus.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 600
        self.timer = 0
        self.visible = False


    def update(self):
        self.timer += 1

        if not self.visible:
            if self.timer >= 15 * 60:
                self.rect.x = 1300
                self.rect.y = 600
                self.visible = True
                self.timer = 0


    def reset(self):
        self.timer = 0
        self.visible = False





