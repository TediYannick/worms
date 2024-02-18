import pygame
from player import Player
from map import Map
from projectile import Grenade, Roquette


pygame.init()

# Obtenir la taille de l'écran
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Créer la fenêtre en mode plein écran
screen = pygame.display.set_mode()

# Créer une instance de la classe Map
game_map = Map(screen)
start_y = game_map.start_y

# Créer une instance de la classe Player
player1 = Player(screen, "Worm Alpha", start_y)
player2 = Player(screen, "Worm Beta", start_y)
players = pygame.sprite.Group(player1, player2)

current_player = player1  # Le joueur actuel au début est le joueur 1
font = pygame.font.Font(None, 50)

projectiles = []  # Liste des projectiles

# power = 50  
# grenade = None
# roquette = None 
# angle_deg = 0 
# arme = True

running = True
left_pressed = False
right_pressed = False
space_pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #Ici chaque appui de touche décrémente le nombre d'action restante 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            elif event.key == pygame.K_LEFT and current_player.actions_remaining > 0 and not left_pressed:
                current_player.move_left()
                left_pressed = True
                current_player.actions_remaining -= 1
            
            elif event.key == pygame.K_RIGHT and current_player.actions_remaining > 0 and not right_pressed:
                current_player.move_right()
                right_pressed = True
                current_player.actions_remaining -= 1
            
            elif event.key == pygame.K_SPACE and current_player.actions_remaining > 0 and not space_pressed:
                current_player.jump()
                space_pressed = True
                current_player.actions_remaining -= 1
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                current_player.stop_left()
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                current_player.stop_right()
                right_pressed = False
            elif event.key == pygame.K_SPACE:
                space_pressed = False
        
            # elif event.key == pygame.K_a:  # Touche A pour l'arme
            #     arme = not arme
            #     current_player.actions_remaining -= 1

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 4 and power <= 99: 
        #         power += 1
        #         current_player.actions_remaining -= 1

        #     elif event.button == 5 and power >= 2:  
        #         power -= 1
        #         current_player.actions_remaining -= 1

        #     elif event.button == pygame.BUTTON_LEFT:
                
        #         if arme:
        #             grenade = Grenade(player.rect.x, player.rect.y, power, angle_deg, screen)
        #             roquette = None
        #             current_player.actions_remaining -= 1

        #         else:
        #             roquette = Roquette(player.rect.x, player.rect.y, power, angle_deg, screen)
        #             grenade = None         
        #             current_player.actions_remaining -= 1

            if current_player.actions_remaining == 0:  # Changer de joueur
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1
                current_player.actions_remaining = 7  # Réinitialiser le nombre d'actions pour le nouveau joueur

     # Mise à jour des projectiles
    for projectile in projectiles:
        projectile.update()

    # Vérification des collisions
    for projectile in projectiles:
        for player in players:
            player.check_collision(projectile)           

    # Appliquer la gravité et mettre à jour la position des joueurs
    player1.update()
    player2.update()

    # Afficher la carte
    game_map.draw()

    # Afficher les joueurs
    players.draw(screen)

    # Afficher les compteurs d'actions
    text_player1 = font.render(f"Actions restantes Worm Alpha: {player1.actions_remaining}", True, (15, 5, 107))
    screen.blit(text_player1, (20, 20))

    text_player2 = font.render(f"Actions restantes Worm Beta: {player2.actions_remaining}", True, (15, 5, 107))
    text_rect = text_player2.get_rect()
    text_rect.topright = (screen_width - 20, 20)
    screen.blit(text_player2, text_rect)

    

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
