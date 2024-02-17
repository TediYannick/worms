import pygame
import math

class Projectile:
    def __init__(self, x, y, power, angle_deg, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.power = power
        self.angle_rad = math.radians(angle_deg)
        self.vel_x = power * math.cos(self.angle_rad)
        self.vel_y = -power * math.sin(self.angle_rad)
        self.gravity = 9.8 
        self.time = 0
        self.time_increment = 0.1

    def update(self):
        # Mettre à jour la position du projectile en utilisant les équations de trajectoire
        self.x += self.vel_x * self.time_increment
        self.y += self.vel_y * self.time_increment + 0.5 * self.gravity * self.time_increment ** 2
        self.vel_y += self.gravity * self.time_increment  
        self.time += self.time_increment

        if self.y >= self.screen.get_height() // 1.5:
            self.y = self.screen.get_height() // 1.5  
            self.vel_y = -self.vel_y * 0.8  # Inverser la vitesse verticale pour simuler le rebond + amortissemnt de 20%
            

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 5)

