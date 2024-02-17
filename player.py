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
        self.is_moving_left = False  
        self.is_moving_right = False  

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom >= self.screen.get_height() // 1.5:
            self.rect.bottom = self.screen.get_height() // 1.5
            self.velocity_y = 0

        if self.is_moving_left and self.rect.x >= 0:  
            self.rect.x -= 5
        if self.is_moving_right and self.rect.x <= self.screen.get_width() - 32: 
            self.rect.x += 5

    def move_left(self):
        self.is_moving_left = True  

    def move_right(self):
        self.is_moving_right = True  
    def stop_left(self):
        self.is_moving_left = False  

    def stop_right(self):
        self.is_moving_right = False  

    def jump(self):
        if self.rect.bottom == self.screen.get_height() // 1.5:
            self.velocity_y = -10

    def draw(self):
        self.screen.blit(self.image, self.rect)