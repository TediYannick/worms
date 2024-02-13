import pygame
from player import Player
from map import Map

pygame.init()

# Obtenir la taille de l'écran
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Créer la fenêtre en mode plein écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Créer une instance de la classe Map
game_map = Map(screen)

# Créer une instance de la classe Player
player = Player(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Appuyez sur la touche ESC pour quitter
                running = False
            elif event.key == pygame.K_LEFT:  # Appuyez sur la flèche gauche pour déplacer le personnage vers la gauche
                player.move_left()
            elif event.key == pygame.K_RIGHT:  # Appuyez sur la flèche droite pour déplacer le personnage vers la droite
                player.move_right()
            elif event.key == pygame.K_SPACE:  # Appuyez sur la barre d'espace pour faire sauter le personnage
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # Relâchez la touche gauche pour arrêter le déplacement vers la gauche
                player.stop_left()
            elif event.key == pygame.K_RIGHT:  # Relâchez la touche droite pour arrêter le déplacement vers la droite
                player.stop_right()

    # Appliquer la gravité et mettre à jour la position du joueur
    player.update()

    # Afficher la carte
    game_map.draw()

    # Afficher le joueur
    player.draw()

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
