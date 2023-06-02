# Vérifier si le joueur a atteint 200 points
if self.score >= 60 and not self.score_changed:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(Boss)
    self.spawn_monster(guard)
    self.spawn_monster(guard)
    self.spawn_monster(guard)
    self.spawn_monster(guard)

    # Définir score_changed sur True
    self.score_changed = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _____________________________________________________________________________

if self.score >= 160 and not self.score_2:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi4)
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi3)

    # Définir score_changed sur True
    self.score_2 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)

    # ______________________________________________________________________
if self.score >= 260 and not self.score_3:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi8)
    self.spawn_monster(ennemi8)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi7)

    # Définir score_changed sur True
    self.score_3 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _____________________________________________________________________
if self.score >= 360 and not self.score_4:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(bomb)
    self.spawn_monster(bomb)
    self.spawn_monster(bomb)
    self.spawn_monster(ennemi12)
    self.spawn_monster(ennemi12)

    # Définir score_changed sur True
    self.score_4 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _____________________________________________________________________________________
if self.score >= 460 and not self.score_5:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi11)
    self.spawn_monster(ennemi11)
    self.spawn_monster(ennemi10)
    self.spawn_monster(ennemi10)
    self.spawn_monster(ennemi10)

    # Définir score_changed sur True
    self.score_5 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # ___________________________________________________________________________

if self.score >= 560 and not self.score_6:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(Boss)
    self.spawn_monster(Boss)
    self.spawn_monster(guard)
    self.spawn_monster(guard)
    self.spawn_monster(guard)
    self.spawn_monster(guard)

    # Définir score_changed sur True
    self.score_6 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # ___________________________________________________________________________

if self.score >= 660 and not self.score_7:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi4)
    self.spawn_monster(ennemi4)

    # Définir score_changed sur True
    self.score_7 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _________________________________________________________________________

if self.score >= 3500 and not self.score_8:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi8)
    self.spawn_monster(ennemi8)

    # Définir score_changed sur True
    self.score_8 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # ________________________________________________________________________

if self.score >= 4000 and not self.score_9:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi12)
    self.spawn_monster(ennemi12)
    self.spawn_monster(bomb)
    self.spawn_monster(bomb)
    self.spawn_monster(bomb)
    self.spawn_monster(bomb)

    # Définir score_changed sur True
    self.score_9 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _______________________________________________________________

if self.score >= 4500 and not self.score_10:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi11)
    self.spawn_monster(ennemi11)
    self.spawn_monster(ennemi10)
    self.spawn_monster(ennemi10)
    self.spawn_monster(ennemi10)
    self.spawn_monster(ennemi10)

    # Définir score_changed sur True
    self.score_10 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # _____________________________________________________________________

if self.score >= 5000 and not self.score_11:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi10)
    self.spawn_monster(bomb)
    self.spawn_monster(ennemi1)
    self.spawn_monster(ennemi2)

    # Définir score_changed sur True
    self.score_11 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)
    # ______________________________________________________

if self.score >= 5500 and not self.score_12:
    # Supprimer les monstres existants
    self.all_monsters.empty()

    # Faire apparaître de nouveaux monstres
    self.spawn_monster(ennemi3)
    self.spawn_monster(ennemi7)
    self.spawn_monster(ennemi10)
    self.spawn_monster(bomb)
    self.spawn_monster(ennemi1)
    self.spawn_monster(ennemi2)

    # Définir score_changed sur True
    self.score_12 = True

    for monster in self.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
        # __________________________________________________
    if self.score >= 6000 and not self.score_13:
        # Supprimer les monstres existants
        self.all_monsters.empty()

        # Faire apparaître de nouveaux monstres
        self.spawn_monster(ennemi4)
        self.spawn_monster(ennemi8)
        self.spawn_monster(ennemi11)
        self.spawn_monster(ennemi12)
        self.spawn_monster(Boss)

        # Définir score_changed sur True
        self.score_13 = True

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

    # Afficher les autres éléments
    self.all_explosions.draw(screen)
    screen.blit(self.player.image, self.player.rect)
    self.player.update_health_bar(screen)
    self.comet_event.update_bar(screen)
    self.player.all_projectiles.draw(screen)
    self.all_monsters.draw(screen)
    self.comet_event.all_comets.draw(screen)

    if self.score >= 6500 and not self.score_14:
        # Supprimer les monstres existants
        self.all_monsters.empty()