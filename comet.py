import pygame
import random
from monster import Explosion

#creer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir l'image associé à cette comette
        self.image = pygame.image.load('assets/bomb.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 4)
        self.rect.x = random.randint (20, 1300 )
        self.rect.y = random.randint(-400,-130)
        self.comet_event = comet_event

    def remove(self):

        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('bomb')


        #vérifier le nombre de comète est de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre à 0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y>=500:

            #retirer la boule de feu
            self.remove()

            #si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                #remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #retirer la boule de feu
            self.remove()


            #subir 20 points de dégat
            self.comet_event.game.player.damage(20)