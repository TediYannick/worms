import pygame
import math
import os

class Grenade:
    def __init__(self, x, y, power, angle_deg, screen):
        self.screen = screen
        self.active = True
        self.image = pygame.image.load(os.path.join('assets/Imageworms/', 'grenade.png')).convert_alpha()
        self.x = x
        self.y = y
        self.power = power
        self.angle_rad = math.radians(angle_deg)
        self.vel_x = power * math.cos(self.angle_rad)
        self.vel_y = -power * math.sin(self.angle_rad)
        self.explosion_radius = 100
        self.explosion_center = (0, 0)
        self.gravity = 9.8 
        self.time = 0
        self.time_increment = 0.1
        self.explosion_time = 20 

    def update(self):
        self.x += self.vel_x * self.time_increment
        self.y += self.vel_y * self.time_increment + 0.5 * self.gravity * self.time_increment ** 2
        self.vel_y += self.gravity * self.time_increment  
        self.time += self.time_increment
        
        

        if self.y >= (self.screen.get_height() - 32) // 1.5:
            self.y = (self.screen.get_height() - 32) // 1.5  
            self.vel_y = -self.vel_y * 0.8  
        elif self.time >= self.explosion_time:
            self.explosion_center = (self.x, self.y)
            self.explosion()
            self.destroy()
            

    def draw(self, screen):
        if self.active:
            if self.vel_x < 0:
                screen.blit(self.image, (int(self.x), int(self.y)))
            else:
                flipped_image = pygame.transform.flip(self.image, True, False)  # Retourner horizontalement
                screen.blit(flipped_image, (int(self.x), int(self.y)))

    def explosion(self):
        pygame.draw.circle(self.screen, (255, 128, 0), self.explosion_center, self.explosion_radius)

    def destroy(self):
        self.active = False




class Roquette:
    def __init__(self, x, y, power, angle_deg, screen):
        self.screen = screen
        self.active = True
        self.image = pygame.image.load(os.path.join('assets/Imageworms/', 'roquette.png')).convert_alpha()
        self.x = x
        self.y = y
        self.power = power
        self.angle_rad = math.radians(angle_deg)
        self.vel_x = power * math.cos(self.angle_rad)
        self.vel_y = -power * math.sin(self.angle_rad)
        self.explosion_radius = 100
        self.explosion_center = (0, 0)
        self.gravity = 9.8 
        self.wind = 20.0  
        self.time = 0
        self.time_increment = 0.3

    def update(self):
        self.x += (self.vel_x + self.wind) * self.time_increment  
        self.y += self.vel_y * self.time_increment + 0.5 * self.gravity * self.time_increment ** 2
        self.vel_y += self.gravity * self.time_increment  
        self.time += self.time_increment
        

        if self.y >= self.screen.get_height() // 1.5:
            self.explosion_center = (self.x, self.y)
            self.explosion()
            self.destroy()


    def draw(self, screen):
        if self.active:
            if self.vel_x < 0:
                screen.blit(self.image, (int(self.x), int(self.y)))
            else:
                
                flipped_image = pygame.transform.flip(self.image, True, False)  # Retourner horizontalement
                screen.blit(flipped_image, (int(self.x), int(self.y)))

    def explosion(self):
        pygame.draw.circle(self.screen, (255, 128, 0), self.explosion_center, self.explosion_radius)

    def destroy(self):
        self.active = False

