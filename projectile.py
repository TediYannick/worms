import pygame
import math

class Projectile:
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power
        self.vel_x = 0  # Vitesse horizontale initiale
        self.vel_y = 0  # Vitesse verticale initiale
        self.gravity = 0.5  # Valeur de la gravité

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += self.gravity
