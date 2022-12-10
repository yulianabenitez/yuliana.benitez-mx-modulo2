import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, START, DEAD, OVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.message import draw_message
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
# cloud
from dino_runner.components.obstacles.cloud import Cloud


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.cloud = Cloud()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.score = 0
        self.game_speed = 20

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((64, 207, 255))
        self.draw_background()
        self.draw_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        # se añaden las nubes en el fondo
        self.cloud.draw(self.screen)
        self.cloud.update(self)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message(
                    f'{self.player.type.capitalize()} enable for {time_to_show} seconds',
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_score(self):
        draw_message(f'your score: {self.score}', self.screen,
                     font_size=20, pos_x_center=1000, pos_y_center=30)

    def reset_score(self):
        self.score = 0
        self.game_speed = 20

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((10, 47, 118))  # color de fondo del screen
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        # Se validan tres oportunidades y en cada una contabilizar las death_count los cuales se iran mostrando en cada una de las partidas
        if self.death_count == 0:
            draw_message('Press any key to start', self.screen,
                         font_size=20, pos_x_center=half_screen_width, pos_y_center=half_screen_height)
            # Dibujar la imagen START en la pantalla que se obtiene de constantes.
            self.screen.blit(START, (half_screen_width -
                                     20, half_screen_height - 140))

        elif self.death_count == 1:
            draw_message('Press any key to start', self.screen,
                         font_size=20, pos_x_center=half_screen_width, pos_y_center=half_screen_height)
            draw_message(
                f'your score: {self.score}', self.screen, pos_y_center=half_screen_height + 50)
            draw_message(f'Death count: {self.death_count}',
                         self.screen, pos_y_center=half_screen_height + 100)
            # Dibujando la imagen DEAD en la pantalla que se obtiene de constante.
            self.screen.blit(DEAD, (half_screen_width -
                                    20, half_screen_height - 140))

        elif self.death_count == 2:
            draw_message('Press any key to start', self.screen,
                         font_size=20, pos_x_center=half_screen_width, pos_y_center=half_screen_height)
            draw_message(
                f'your score: {self.score}', self.screen, pos_y_center=half_screen_height + 50)
            draw_message(f'Death count: {self.death_count}',
                         self.screen, pos_y_center=half_screen_height + 100)
            # Dibujando la imagen DEAD en la pantalla que se obtiene de constante.
            self.screen.blit(DEAD, (half_screen_width -
                                    20, half_screen_height - 140))
        else:
            draw_message('Looooser !!', self.screen, font_size=20,
                         pos_x_center=half_screen_width, pos_y_center=half_screen_height)
            self.screen.blit(OVER, (half_screen_width -
                             180, half_screen_height - 140))
            draw_message(
                f'your score: {self.score}', self.screen, pos_y_center=half_screen_height + 50)
            draw_message(f'Death count: {self.death_count}',
                         self.screen, pos_y_center=half_screen_height + 100)
            # Dibujando la imagen DEAD en la pantalla que se obtiene de constante.
            self.screen.blit(DEAD, (half_screen_width -
                                    20, half_screen_height - 140))
            draw_message('Press any key to restart', self.screen,
                         font_size=20, pos_x_center=half_screen_width, pos_y_center=half_screen_height + 160)

        #  RESET DEL JUEGO
        if self.death_count == 3:
            self.reset_score()
            self.death_count = 0

        pygame.display.update()
        self.handle_events_on_menu()
