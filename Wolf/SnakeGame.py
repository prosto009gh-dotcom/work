import pygame
import SoundController
import color
import consts
from Fruit import Fruit
from RenderEngine import RenderEngine
from Snake import Snake

class SnakeGame:

    def __init__(self):
        pygame.init()
        SoundController.main_music.play(-1)
        self.render = RenderEngine()
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 35)
        self.game_over = False
        self.game_close = False
        self.snake2 = Snake(color.blue, 10, 2)
        self.snake = Snake(color.black,10, 1)
        self.fruit = None

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.snake.vector_x > 0:
                        break
                    self.snake.move(-self.snake.speed, 0)
                elif event.key == pygame.K_RIGHT:
                    if self.snake.vector_x < 0:
                        break
                    self.snake.move(self.snake.speed, 0)
                elif event.key == pygame.K_UP:
                    if self.snake.vector_y > 0:
                        break
                    self.snake.move(0, -self.snake.speed)
                elif event.key == pygame.K_DOWN:
                    if self.snake.vector_y < 0:
                        break
                    self.snake.move(0, self.snake.speed)
                elif event.key == pygame.K_a:
                    if self.snake2.vector_x > 0:
                        break
                    self.snake2.move(-self.snake2.speed, 0)
                elif event.key == pygame.K_d:
                    if self.snake2.vector_x < 0:
                        break
                    self.snake2.move(self.snake2.speed, 0)
                elif event.key == pygame.K_w:
                    if self.snake2.vector_y > 0:
                        break
                    self.snake2.move(0, -self.snake2.speed)
                elif event.key == pygame.K_s:
                    if self.snake2.vector_y < 0:
                        break
                    self.snake2.move(0, self.snake2.speed)

    def game_logic(self):
        if self.fruit is None:
            self.fruit = Fruit()
        self.event_handler()
        if self.snake.collide(self.fruit):
            self.snake.eat()
            self.fruit.destroy()
            self.fruit = Fruit()
        if self.snake2.collide(self.fruit):
            self.snake2.eat()
            self.fruit.destroy()
            self.fruit = Fruit()
        if self.snake.collide(self.snake2):
            self.game_over = True
        if self.snake2.collide(self.snake):
            self.game_over = True
        if self.snake.snake_length > 1:
            for i in range(len(self.snake.snake_list)):
                if self.snake2.rect.colliderect(self):
                    self.game_over = True
        if self.snake2.snake_length > 1:
            for i in range(len(self.snake2.snake_list)):
                if self.snake.rect.colliderect(self):
                    self.game_over = True
        self.snake.update()
        self.snake2.update()
        if self.snake.collide_with_screen_border():
            x = self.snake.head.x
            y = self.snake.head.y
            if self.snake.head.x > consts.screen_width:
                self.snake.head.x = 0 + self.snake.block_size
            elif self.snake.head.x < 0:
                self.snake.head.x = consts.screen_width - self.snake.block_size
            elif self.snake.head.y > consts.screen_height:
                self.snake.head.y = 0 + self.snake.block_size
            elif self.snake.head.y < 0:
                self.snake.head.y = consts.screen_height - self.snake.block_size
        if self.snake2.collide_with_screen_border():
            x = self.snake2.head.x
            y = self.snake2.head.y
            if self.snake2.head.x > consts.screen_width:
                self.snake2.head.x = 0 + self.snake2.block_size
            elif self.snake2.head.x < 0:
                self.snake2.head.x = consts.screen_width - self.snake2.block_size
            elif self.snake2.head.y > consts.screen_height:
                self.snake2.head.y = 0 + self.snake2.block_size
            elif self.snake2.head.y < 0:
                self.snake2.head.y = consts.screen_height - self.snake2.block_size
        self.clock.tick(consts.game_FPS)

    def game_loop(self):
        while not self.game_over:
            self.game_logic()
            self.render.add_render_object(self.fruit,self.snake,self.snake2)
            self.render.render()
        pygame.quit()
        quit()


