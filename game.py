import pygame
import random
import time
from respawn import Respawn1

from Son import SonManager
from player import Player
from monster import ennemi1, ennemi2
from respawn import Respawn1

# variable pour compter les ennemies présent sur l'écran
enemie_count = 4


# creer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        # definir si notre à commencé
        self.bonus_timer = None
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.Respawn1 = Respawn1 (self)
        self.all_explosions = pygame.sprite.Group()

        # group de monstre
        self.all_monsters = pygame.sprite.Group()
        enemie_count = pygame.sprite.Group()

        # gerer le son
        self.Son_manager = SonManager()

        # mettre le score à 0
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        for i in range(1, 5):
            self.spawn_monster(ennemi1)
            self.spawn_monster(ennemi2)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remettre le jeu à 0, monstre vie etc...
        self.all_monsters = pygame.sprite.Group()
        self.Respawn1.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.Respawn1.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.Son_manager.play('game_over')

    def update(self, screen):
        # Vérifier si un monstre est hors de l'écran
        for monster in self.all_monsters:
            if monster.rect.y >= screen.get_height():
                self.all_monsters.remove(monster)
        # Vérifier si la liste des monstres est vide
        if len(self.all_monsters) <= random.randint(1, 5):
            self.spawn_monster(ennemi1)
            self.spawn_monster(ennemi2)

        # afficher le score sur l'ecran
        score_text = pygame.font.SysFont(None, 40).render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        self.all_explosions.update()
        self.all_explosions.draw(screen)

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les enemie de notre jeu
        for monster in self.all_monsters:
            monster.forward()

        # appliquer les images des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon enemie
        self.all_monsters.draw(screen)


        # verifier si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1400:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 5:
            self.player.move_left()

            # ______________________________________________________________________

    def affichage_update(self, screen, enemie_count):

        # Générer des ennemies
        if enemie_count < 5:
            self.spawn_monster(ennemi1)
            self.spawn_monster(ennemi2)

            enemie_count += 1
        self.all_explosions.draw(screen)
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.Respawn1.update_bar(screen)
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

        collisions = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite):
                self.player.health = self.player.max_health
                sprite.reset()

        collisions2 = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions2:
            if isinstance(sprite):
                self.player.velocity += 1
                sprite.reset()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
