import pygame
import math
from player import Player
from map import Map
from tools import *
from projectile import Grenade, Roquette

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))

game_map = Map(screen)

player1 = Player(screen, "joueur1")
player2 = Player(screen, "joueur2")
current_player = player1

font = pygame.font.Font(None, 36)

power = 50  
grenade = None
roquette = None 
angle_deg = 0 
arme = True
win = False

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Appuyez sur la touche ESC pour quitter
                running = False
            #gestion personnage
            elif event.key == pygame.K_LEFT and current_player.actions_remaining > 0:
                current_player.actions_remaining -= 1
                current_player.move_left()
            elif event.key == pygame.K_RIGHT and current_player.actions_remaining > 0:
                current_player.actions_remaining -= 1
                current_player.move_right()
            elif event.key == pygame.K_SPACE and current_player.actions_remaining > 0:  
                current_player.jump()
                current_player.actions_remaining -= 1
            elif event.key == pygame.K_a:  # Touche A pour l'arme
                arme = not arme
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :  
                current_player.stop_left()
            elif event.key == pygame.K_RIGHT : 
                current_player.stop_right()

            if current_player.actions_remaining == 0:  # Changer de joueur
                current_player = switch_player(current_player, player1, player2)
                current_player.actions_remaining = 7  # Réinitialiser le nombre d'actions pour le nouveau joueur

            #gestion projectile
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and power <= 99: 
                power += 1
            elif event.button == 5 and power >= 2:  
                power -= 1
            elif event.button == pygame.BUTTON_LEFT and grenade is None and roquette is None:
                if arme:
                    grenade = Grenade(current_player.rect.x, current_player.rect.y, power, angle_deg, screen)
                    roquette = None
                else:
                    roquette = Roquette(current_player.rect.x, current_player.rect.y, power, angle_deg, screen)
                    grenade = None 

        
    if not win:
        player1.update()
        player2.update()

        game_map.draw()
        player1.draw()
        player2.draw()
        

        if grenade:
            grenade.update()
            grenade.draw(screen)

            if current_player == player1:
                if player_hit(player2, grenade):
                    win = True
            else:
                if player_hit(player1, grenade):
                    win = True

            if not grenade.active: 
                grenade = None
                current_player = switch_player(current_player, player1, player2) 
                current_player.actions_remaining = 7

        elif roquette:
            roquette.update()
            roquette.draw(screen)

            if current_player == player1:
                if player_hit(player2, roquette):
                    win = True
            else:
                if player_hit(player1, roquette):
                    win = True

            if not roquette.active:
                roquette = None
                current_player = switch_player(current_player, player1, player2)
                current_player.actions_remaining = 7
            

        angle_deg = angle(current_player.rect.x, current_player.rect.y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        trajectoire_points = trajectoire(current_player.rect.x, current_player.rect.y, power, angle_deg, 100)
        for point in trajectoire_points:
            pygame.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 2)


        #text_surface1 = font.render(f"Position: ({current_player.rect.x}, {current_player.rect.y})", True, (255, 0, 0))
        #text_surface2 = font.render(f"Position souris: ({pygame.mouse.get_pos()[0]}, { pygame.mouse.get_pos()[1]})", True, (255, 0, 0))
        #text_surface3 = font.render(f"angle°: ({round(angle_deg)}°)", True, (255, 0, 0))
        text_surface4 = font.render(f"action restante du {current_player}: ({current_player.actions_remaining})", True, (255, 0, 0))
        text_surface5 = font.render(f"arme: {'grenade' if arme else 'roquette'}", True, (255, 0, 0))
        text_surface6 = font.render(f"power: ({power} % )", True, (255, 0, 0))
        
        


        #screen.blit(text_surface1, (10, 10))
        #screen.blit(text_surface2, (10, 46))
        #screen.blit(text_surface3, (10, 76))
        screen.blit(text_surface4, (10, 10))
        screen.blit(text_surface5, (10, 46))
        screen.blit(text_surface6, (10, 82))
       

        


        pygame.display.flip()
    else:
        font = pygame.font.Font(None, 100)
        if current_player == player1:
            text_surface7 = font.render(f"player 2 WIN!", True, (255, 189, 0))
            screen.blit(text_surface7, (screen_width // 2 - 100, screen_height // 2))
        else:
            text_surface7 = font.render(f"player 1 WIN!", True, (255, 189, 0))
            screen.blit(text_surface7, (screen_width // 2, screen_height // 2))
    pygame.display.flip()

pygame.quit()
