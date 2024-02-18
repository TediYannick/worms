import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, name, start_y):
        super().__init__()
        self.screen = screen
        self.name = name
        self.start_y = start_y
        self.actions_remaining = 7  # Nombre d'actions que le joueur peut effectuer par tour
        self.image = pygame.image.load("assets/BWorm.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = start_y
        self.velocity_y = 0
        self.gravity = 0.5
        self.is_moving_left = False  # Nouvel attribut pour suivre l'état de déplacement à gauche
        self.is_moving_right = False  # Nouvel attribut pour suivre l'état de déplacement à droite
        self.spawn_random()
        self.is_alive = True # Vérifie si le joueur est vivant
    

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Limiter le mouvement vertical dans les limites de l'écran
        if self.rect.bottom >= self.start_y:
            self.rect.bottom = self.start_y
            self.velocity_y = 0
        elif self.rect.top < 0:
            self.rect.top = 0

        # Limiter le mouvement horizontal dans les limites de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()

        # Déplacement horizontal
        if self.is_moving_left:
            self.rect.x -= 5
        if self.is_moving_right:
            self.rect.x += 5

    # Détecte les collisions entre le rectangle joueur et le rectangle projectile
    def check_collision(self, projectile):
        if self.rect.colliderect(projectile.rect):
            self.is_alive = False  # Le joueur est touché et meurt        

    def spawn_random(self):
        min_x = int(self.screen.get_width() * 0.1)
        max_x = int(self.screen.get_width() * 0.9)
        min_y = int(self.start_y * 0.1)  # Ne pas spawner en-dessous de 10% de la hauteur du sol
        max_y = int(self.start_y * 0.9)  # Ne pas spawner au-dessus de 90% de la hauteur du sol
        self.rect.x = random.randint(min_x, max_x)
        self.rect.y = random.randint(min_y, max_y)

    def apply_gravity(self):
        if self.rect.bottom < self.start_y:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
        else:
            self.velocity_y = 0


    def move_left(self):
        self.is_moving_left = True

    def move_right(self):
        self.is_moving_right = True

    def stop_left(self):
        self.is_moving_left = False

    def stop_right(self):
        self.is_moving_right = False

    def jump(self):
        if self.rect.bottom == self.start_y:
            self.velocity_y = -10

    def draw(self):
        self.screen.blit(self.image, self.rect)
