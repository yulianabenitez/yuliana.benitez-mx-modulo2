import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
FONT_COLOR = (255, 255, 255)


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
        self.running = False
        self.score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1

    def reset_score(self):
        self.score = 0
        self.game_speed = 20

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
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

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_events_on_menu(self):
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_SPACE:
                    self.run()

    def show_menu(self):
        self.handle_events_on_menu()
        self.screen.fill((10, 47, 118))  # color de fondo del screen
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render('Press any key to start', True, FONT_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)

            textd = font.render(
                f'Death count: {self.death_count}', True, FONT_COLOR)
            textd_rect = textd.get_rect()
            textd_rect.center = (half_screen_width, half_screen_height + 50)
            self.screen.blit(textd, textd_rect)

            self.screen.blit(ICON, (half_screen_width -
                                    20, half_screen_height - 140))
        else:
            font = pygame.font.Font(FONT_STYLE, 30)
            textco = font.render('Game Over', 30, FONT_COLOR)
            textco_rect = textco.get_rect()
            textco_rect.center = (half_screen_width, half_screen_height - 150)
            self.screen.blit(textco, textco_rect)

            textd = font.render(
                f'Death count: {self.death_count}', 30, FONT_COLOR)
            textd_rect = textd.get_rect()
            textd_rect.center = (half_screen_width, half_screen_height + 50)
            self.screen.blit(textd, textd_rect)

            texts = font.render(f'Last score: {self.score}', 30, FONT_COLOR)
            texts_rect = texts.get_rect()
            texts_rect.center = (half_screen_width, half_screen_height + 100)
            self.screen.blit(texts, texts_rect)
            self.screen.blit(ICON, (half_screen_width -
                                    20, half_screen_height - 140))
            fontes = pygame.font.Font(FONT_STYLE, 15)
            textes = fontes.render('Press ESC to exit', True, FONT_COLOR)
            textes_rect = textes.get_rect()
            textes_rect.center = (half_screen_width, half_screen_height + 180)
            self.screen.blit(textes, textes_rect)

        pygame.display.update()
        self.handle_events_on_menu()
