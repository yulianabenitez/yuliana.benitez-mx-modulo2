import random
from dino_runner.components.obstacles.obstacle import Obstacle
# from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


# La clase LargeCactus es una subclase de la clase Obstacle. Tiene un atributo de tipo al que se le
# asigna aleatoriamente un valor entre 0 y 2. También tiene un atributo rect que se hereda de la clase
# Obstáculo
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
