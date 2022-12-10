import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        """
        La función __init__ es un constructor que toma una imagen y establece el tipo en 0, luego llama
        al constructor de la superclase con la imagen y el tipo, luego establece la posición y del
        pájaro en una selección aleatoria de la lista BIRD_HEIGHTS, y finalmente establece el índice a 0

        :param image: La imagen que se usará para el sprite
        """
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0

    def draw(self, SCREEN):
        """
        Si el índice es mayor o igual a 9, establezca el índice en 0.
        Blit la imagen en el índice dividido por 5 a la pantalla en el rect.
        Incrementa el índice en 1

        :param SCREEN: La pantalla en la que se dibujará la animación
        """
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1
