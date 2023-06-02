import pygame

#creer une classe pour gérer cette évènement
class Respawn1:

    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 70
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed /100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self,surface):
        self.add_percent()

