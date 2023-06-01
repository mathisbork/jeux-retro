import pygame
import random
import time

from bonus import Bonus
from bonus2 import BonusBoost, Bonus2
from bonus3 import Bonus3
from sounds import SoundManager
from player import Player
from monster import ennemi1, ennemi2, Boss, ennemi10, ennemi11, guard, ennemi3, ennemi4, ennemi7, ennemi8, \
    bomb, ennemi12
from comet_event import CometFallEvent

#creer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #definir si notre à commencé
        self.bonus_timer = None
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)
        self.all_explosions = pygame.sprite.Group()


        #gerer le bonus
        self.bonus = Bonus()
        self.bonus2 = Bonus2()
        self.bonus3 = Bonus3()



        #group de monstre
        self.all_monsters = pygame.sprite.Group()


        self.pressed = {}
        self.score_0 = False

        self.score_changed = False

        self.score_2 = False

        self.score_3 = False

        self.score_4 = False

        self.score_5 = False

        self.score_6 = False

        self.score_7 = False

        self.score_8 = False

        self.score_9 = False

        self.score_10 = False

        self.score_11 = False

        self.score_12 = False

        self.score_13 = False

        self.score_14 = False


        #gerer le son
        self.sound_manager = SoundManager()

        #mettre le score à 0
        self.score = 0
        self.pressed ={}




    def start(self):
        self.is_playing = True
        self.spawn_monster(ennemi1)



    def add_score(self, points=10):
        self.score += points



    def game_over(self):
        #remettre le jeu à 0, monstre vie etc...
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        #afficher le score sur l'ecran
        score_text = pygame.font.SysFont(None, 40).render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20,20))
        self.all_explosions.update()
        self.all_explosions.draw(screen)

        self.bonus.update()

        if pygame.sprite.collide_rect(self.player, self.bonus):
            self.player.health = self.player.max_health
            self.bonus.reset()

        if self.bonus.visible:
            screen.blit(self.bonus.image, self.bonus.rect)
            #_______________________________________________________

        self.bonus2.update()

        if pygame.sprite.collide_rect(self.player, self.bonus2):
            self.player.attack += 0.02
            self.bonus2.reset()

        if self.bonus2.visible:
            screen.blit(self.bonus2.image, self.bonus2.rect)

         # _______________________________________________________

        self.bonus3.update()

        if pygame.sprite.collide_rect(self.player, self.bonus3):
            self.bonus3.reset()

        if self.bonus3.visible:
            screen.blit(self.bonus3.image, self.bonus3.rect)
        # _______________________________________________________

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)


        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)


        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #recuperer les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()



        # appliquer les images des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon monstre
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comettes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1400:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 5:
            self.player.move_left()

            #______________________________________________________________________

    def affichage_update(self, screen):
        # Afficher les autres éléments
        self.spawn_monster(guard)
        # time.sleep(1)
        self.all_explosions.draw(screen)
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.comet_event.update_bar(screen)
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_event.all_comets.draw(screen)


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

        collisions = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite, Bonus):
                self.player.health = self.player.max_health
                sprite.reset()

        collisions2 = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions2:
            if isinstance(sprite, Bonus3):
                self.player.velocity += 1
                sprite.reset()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
