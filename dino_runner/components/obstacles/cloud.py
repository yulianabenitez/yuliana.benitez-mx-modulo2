import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    # Creando una nueva instancia de la clase Cloud.
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    # Actualización de la posición de la nube.
    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
