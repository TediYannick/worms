import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.bottom = screen.get_height() // 2
        self.velocity_y = 0
        self.gravity = 0.5
        self.is_moving_left = False  # Nouvel attribut pour suivre l'état de déplacement à gauche
        self.is_moving_right = False  # Nouvel attribut pour suivre l'état de déplacement à droite

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom >= self.screen.get_height() // 1.5:
            self.rect.bottom = self.screen.get_height() // 1.5
            self.velocity_y = 0

        if self.is_moving_left:  # Vérifie si la touche de déplacement à gauche est enfoncée
            self.rect.x -= 5
        if self.is_moving_right:  # Vérifie si la touche de déplacement à droite est enfoncée
            self.rect.x += 5

    def move_left(self):
        self.is_moving_left = True  # Met à True lorsque la touche est enfoncée

    def move_right(self):
        self.is_moving_right = True  # Met à True lorsque la touche est enfoncée

    def stop_left(self):
        self.is_moving_left = False  # Met à False lorsque la touche est relâchée

    def stop_right(self):
        self.is_moving_right = False  # Met à False lorsque la touche est relâchée

    def jump(self):
        if self.rect.bottom == self.screen.get_height() // 1.5:
            self.velocity_y = -10

    def draw(self):
        self.screen.blit(self.image, self.rect)