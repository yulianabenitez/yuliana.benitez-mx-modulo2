import random
from dino_runner.components.obstacles.obstacle import Obstacle
# from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


# La clase SmallCactus es una subclase de la clase Obstacle. Tiene un atributo de tipo al que se le
# asigna aleatoriamente un valor entre 0 y 2. También tiene un atributo rect que se hereda de la clase
# Obstáculo. El atributo rect es un objeto rectangular que se utiliza para detectar colisiones. El
# atributo rect tiene un atributo y que se establece en 325
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
