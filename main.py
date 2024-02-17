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
player = Player(screen)
font = pygame.font.Font(None, 36)

power = 50  
grenade = None
roquette = None 
angle_deg = 0 
arme = True

running = True
while running:
    for event in pygame.event.get():
        angle_deg = angle(player.rect.x, player.rect.y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Appuyez sur la touche ESC pour quitter
                running = False
            #gestion personnage
            elif event.key == pygame.K_LEFT: 
                player.move_left()
            elif event.key == pygame.K_RIGHT:  
                player.move_right()
            elif event.key == pygame.K_SPACE:  
                player.jump()
            elif event.key == pygame.K_a:  # Touche A pour l'arme
                arme = not arme
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  
                player.stop_left()
            elif event.key == pygame.K_RIGHT: 
                player.stop_right()
            #gestion projectile
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and power <= 99: 
                power += 1
            elif event.button == 5 and power >= 2:  
                power -= 1
            elif event.button == pygame.BUTTON_LEFT:
                if arme:
                    grenade = Grenade(player.rect.x, player.rect.y, power, angle_deg, screen)
                    roquette = None
                else:
                    roquette = Roquette(player.rect.x, player.rect.y, power, angle_deg, screen)
                    grenade = None 

        

    player.update()
    game_map.draw()
    player.draw()
    
    
    if grenade:
        grenade.update()
        grenade.draw(screen)
    elif roquette:
        roquette.update()
        roquette.draw(screen)


    trajectoire_points = trajectoire(player.rect.x, player.rect.y, power, angle_deg, 100)
    for point in trajectoire_points:
        pygame.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 2)


    text_surface1 = font.render(f"Position: ({player.rect.x}, {player.rect.y})", True, (255, 0, 0))
    text_surface2 = font.render(f"Position souris: ({pygame.mouse.get_pos()[0]}, { pygame.mouse.get_pos()[1]})", True, (255, 0, 0))
    text_surface3 = font.render(f"angle°: ({round(angle_deg)}°)", True, (255, 0, 0))
    text_surface4 = font.render(f"power: ({power} % )", True, (255, 0, 0))
    text_surface5 = font.render(f"arme: {'grenade' if arme else 'roquette'}", True, (255, 0, 0))


    screen.blit(text_surface1, (10, 10))
    screen.blit(text_surface2, (10, 46))
    screen.blit(text_surface3, (10, 76))
    screen.blit(text_surface4, (10, 106))
    screen.blit(text_surface5, (10, 142))

    pygame.display.flip()

pygame.quit()
