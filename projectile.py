import pygame

#definir la classe qui va gérer le projectile de notre jeux
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 20
        self.player = player
        self.image = pygame.image.load('Assets1/tir 1.png')
        self.image = pygame.transform.scale(self.image,(20,53))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 75
        self.rect.y = player.rect.y + 0


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity


        #vérifier si notre projectile rentre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des dégat
            monster.damage(self.player.attack)

        #vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.y >700:
            # supprimer le projectile
            self.remove()

