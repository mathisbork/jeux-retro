import pygame
from projectile import Projectile

#creer une première classe qui va représenter notre joueur
class Player(pygame.sprite.Sprite):
    import pygame

    # ...

    import pygame

    # ...

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 10
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('Assets1/vaisseau 5.png')
        self.image = pygame.transform.scale(self.image, (70,70))  # Redimensionner l'image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300

    # ...

    # ...

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # desiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 12, self.rect.y + 9, self.max_health, 8])
        pygame.draw.rect(surface, (48, 236, 15), [self.rect.x + 12, self.rect.y + 9, self.health, 8])

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        #jouer le son
        self.game.sound_manager.play('pan')

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre et que il ne soit pas plus à droite que 670 pixel
        if not self.game.check_collision(self, self.game.all_monsters) :
            if self.rect.x + self.velocity <= 670:
                self.rect.x += self.velocity
            else:
                self.rect.x = 670

    def move_left(self):
        self.rect.x -= self.velocity