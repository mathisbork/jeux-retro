import pygame
import math
from game import Game

pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre de notre jeu
pygame.display.set_caption("Shooter retro")
screen = pygame.display.set_mode((740,500))

# Charger l'arrière plan de notre jeu
background = pygame.image.load('Assets1/fond.png')

#charger notre bouton pour creer la partie
play_button = pygame.image.load('Assets1/play_btn.png')
play_button = pygame.transform.scale(play_button, (374,62))
play_button_rect = play_button.get_rect()
play_button_rect.x = 200
play_button_rect.y = 220
#charger notre jeu
game = Game()


running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0,-235))

    #verifier si notre jeux a commencé
    if game.is_playing:
        #déclencher les instructions de la parties
        game.update(screen)
    #vérifier si notre n'as pas commencé
    else:
        #ajouter écran de bien venue
#         screen.blit(banner, (banner_rect))
        screen.blit(play_button, (play_button_rect))

    #mettre à jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           #detecter si la touche espace est enclanchée pour lancé le projectile
           if event.key == pygame.K_SPACE:
               if game.is_playing:
                game.player.launch_projectile()
               else:
                   # mettre le jeu en mode lancé
                   game.start()
                   # jouer le son
                   game.Son_manager.play('start')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris clique sur le bouton pour lancer le jeu
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()


    #fixer le nomvre de FPS
    clock.tick(FPS)
