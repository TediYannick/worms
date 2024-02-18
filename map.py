import pygame


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.load_assets()
        self.num_tiles_x = self.screen.get_width() // 32
        self.num_tiles_y = self.screen.get_height() // 32
        self.start_y = self.screen.get_height() / 1.5
        

       
    def load_assets(self):
        # Charger l'image de fond
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        # Charger l'image des tiles du sol
        self.terreH = pygame.image.load("assets/Imageworms/terreH.png")
        self.terreH = pygame.transform.scale(self.terreH, (32, 32))

        self.terreS = pygame.image.load("assets/Imageworms/terreS.png")
        self.terreS = pygame.transform.scale(self.terreS, (32, 32))

    def draw(self):
        # Afficher l'arrière-plan
        self.screen.blit(self.background, (0, 0))

        # Boucle pour afficher les tiles du sol
        for y in range(self.num_tiles_y):
            for x in range(self.num_tiles_x):
                if y < 1:
                    self.screen.blit(self.terreH, (x * 32, self.start_y + y * 32))
                else:
                    self.screen.blit(self.terreS, (x * 32, self.start_y + y * 32))

