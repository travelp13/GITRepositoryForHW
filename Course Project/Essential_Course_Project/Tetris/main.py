import pygame
from copy import deepcopy
from random import choice, randrange
import os

# Константи гри
WIDTH, HEIGHT = 10, 20                              # розмір ігрового поля в клітинках
TILE_SIZE = 45                                      # розмір кожної клітинки
GAME_RES = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE    # розмір ігрового екрану
RES = 750, 940                                      # розмір вікна гри
FPS = 60                                            # кадри в секунду

class Tetris:
    def __init__(self):
        self.file_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_record = os.path.join(self.file_directory, 'record.txt')
        # Ініціалізація Pygame і налаштування екрану
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode(RES)
        self.game_screen = pygame.Surface(GAME_RES)
        self.clock = pygame.time.Clock()
        

        # Створення сітки для ігрового поля
        self.grid = [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE) for x in range(WIDTH) for y in range(HEIGHT)]

        # Створення форм фігур та позицій блоків
        self.figures_positions = [
            [(-1, 0), (-2, 0), (0, 0), (1, 0)],     # лінія
            [(0, -1), (-1, -1), (-1, 0), (0, 0)],   # квадрат
            [(-1, 0), (-1, 1), (0, 0), (0, -1)],    # Z-подібна
            [(0, 0), (-1, 0), (0, 1), (-1, -1)],    # S-подібна
            [(0, 0), (0, -1), (0, 1), (-1, -1)],    # Т-подібна
            [(0, 0), (0, -1), (0, 1), (1, -1)],     # інша Т-подібна
            [(0, 0), (0, -1), (0, 1), (-1, 0)]      # квадратна
        ]
        self.figures = [[pygame.Rect(x + WIDTH // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in self.figures_positions]
        
        # Ігрові змінні
        self.current_figure, self.next_figure = deepcopy(choice(self.figures)), deepcopy(choice(self.figures))
        self.current_color, self.next_color = self.get_random_color(), self.get_random_color()
        self.field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        
        # Налаштування анімації
        self.animation_count, self.animation_speed, self.animation_limit = 0, 10, 3000
        
        # Фон та шрифти
        self.background = pygame.image.load(os.path.join(self.file_directory, 'img', 'bg.jpg')).convert()
        self.game_background = pygame.image.load(os.path.join(self.file_directory, 'img', 'bg2.jpg')).convert()
        self.main_font = pygame.font.Font(os.path.join(self.file_directory, 'font', 'font.ttf'), 65)
        self.font = pygame.font.Font(os.path.join(self.file_directory,'font', 'font.ttf'), 45)
        
        # Тексти гри
        self.title_tetris = self.main_font.render('TETRIS', True, pygame.Color('orange'))
        self.title_score = self.font.render('Score:', True, pygame.Color('green'))
        self.title_record = self.font.render('Record:', True, pygame.Color('blue'))
        
        # Система рахунків
        self.score = 0
        self.lines = 0
        self.scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

        # Завантаження звуків
        self.move_sound = pygame.mixer.Sound(os.path.join(self.file_directory, 'sounds', 'move.wav'))
        self.rotate_sound = pygame.mixer.Sound(os.path.join(self.file_directory, 'sounds', 'rotate.wav'))
        self.clear_line_sound = pygame.mixer.Sound(os.path.join(self.file_directory, 'sounds', 'clear_line.wav'))
        self.game_over_sound = pygame.mixer.Sound(os.path.join(self.file_directory, 'sounds', 'game_over.wav'))
        
        # Завантаження фонової музики
        pygame.mixer.music.load(os.path.join(self.file_directory, 'sounds', 'background_music.mp3'))
        
        # Налаштування гучності для звуків
        self.move_sound.set_volume(0.1)
        self.rotate_sound.set_volume(0.1)
        self.clear_line_sound.set_volume(0.2)
        self.game_over_sound.set_volume(0.3)
        pygame.mixer.music.set_volume(0.05)
        
        # Програвання фонової музики        
        pygame.mixer.music.play()

    def get_random_color(self):
        # Функція для отримання випадкового кольору
        return (randrange(30, 256), randrange(30, 256), randrange(30, 256))

    def check_borders(self):
        # Перевірка кордонів ігрового поля
        for block in self.current_figure:
            if block.x < 0 or block.x > WIDTH - 1 or block.y > HEIGHT - 1 or self.field[block.y][block.x]:
                return False
        return True

    # Отримання рекорду з файлу
    def get_record(self):
        try:
            with open(self.file_record) as f:
                return f.readline().strip()
        except FileNotFoundError:
            with open(self.file_record, 'w') as f:
                f.write('0')
            return '0'

    # Збереження рекорду у файл    
    def set_record(self):
        try:
            record = self.get_record() 
            record_value = int(record)
        except ValueError:  
            record_value = 0  
        
        with open(self.file_record, 'w') as file:
            file.write(str(max(record_value, self.score)))  # Запись максимального значения

    def run(self):
        # Основний цикл гри
        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.game_screen, (20, 20))
            self.game_screen.blit(self.game_background, (0, 0))
            
            # Обробка подій
            dx, rotate = 0, False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                        self.move_sound.play()
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                        self.move_sound.play()
                    elif event.key == pygame.K_DOWN:
                        self.move_sound.play()
                        self.animation_limit = 100
                    elif event.key == pygame.K_UP:
                        self.rotate_sound.play()
                        rotate = True
            
            # Рух фігур
            old_figure = deepcopy(self.current_figure)
            for block in self.current_figure:
                block.x += dx
            if not self.check_borders():
                self.current_figure = old_figure
            
            # Падіння фігур
            self.animation_count += self.animation_speed
            if self.animation_count > self.animation_limit:
                self.animation_count = 0
                old_figure = deepcopy(self.current_figure)
                for block in self.current_figure:
                    block.y += 1
                if not self.check_borders():
                    for block in old_figure:
                        self.field[block.y][block.x] = self.current_color
                    self.current_figure, self.current_color = self.next_figure, self.next_color
                    self.next_figure, self.next_color = deepcopy(choice(self.figures)), self.get_random_color()
                    self.animation_limit = 3000
            
            # Обертання фігур
            center = self.current_figure[0]
            old_figure = deepcopy(self.current_figure)
            if rotate:
                for block in self.current_figure:
                    x, y = block.y - center.y, block.x - center.x
                    block.x, block.y = center.x - x, center.y + y
                if not self.check_borders():
                    self.current_figure = old_figure
            
            # Видалення повних ліній
            row, lines_cleared = HEIGHT - 1, 0
            for y in range(HEIGHT - 1, -1, -1):
                filled = 0
                for x in range(WIDTH):
                    if self.field[y][x]:
                        filled += 1
                    self.field[row][x] = self.field[y][x]
                if filled < WIDTH:
                    row -= 1
                else:
                    lines_cleared += 1
                    self.animation_speed += 1
                    self.clear_line_sound.play()
            self.score += self.scores[lines_cleared]
            
            # Відображення елементів гри
            [pygame.draw.rect(self.game_screen, (40, 40, 40), rect, 1) for rect in self.grid]
            for block in self.current_figure:
                pygame.draw.rect(self.game_screen, self.current_color, (block.x * TILE_SIZE, block.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            for y, row in enumerate(self.field):
                for x, color in enumerate(row):
                    if color:
                        pygame.draw.rect(self.game_screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            for block in self.next_figure:
                pygame.draw.rect(self.screen, self.next_color, (block.x * TILE_SIZE + 380, block.y * TILE_SIZE + 185, TILE_SIZE, TILE_SIZE))
            self.screen.blit(self.title_tetris, (485, 15))
            self.screen.blit(self.title_score, (535, 780))
            self.screen.blit(self.font.render(str(self.score), True, pygame.Color('white')), (550, 840))
            self.screen.blit(self.title_record, (525, 650))
            self.screen.blit(self.font.render(self.get_record(), True, pygame.Color('red')), (550, 710))
            
            # Перевірка на кінець гри
            if any(self.field[0][x] for x in range(WIDTH)):
                self.set_record()
                self.game_over_sound.play()
                self.field = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
                self.animation_count, self.animation_speed, self.animation_limit = 0, 10, 3000
                self.score = 0
            
            pygame.display.flip()


if __name__ == "__main__":
    game = Tetris()
    game.run()
