import sys
import random
import pygame
from tkinter import messagebox as mBox

WIDTH = 500
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (59, 59, 198)
PURPLE = (132, 68, 201)
GRID_SIZE = 20
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.random_position()

    def random_position(self):
        self.position = (random.randrange(0, 500, 20), random.randrange(0, 500, 20))

    def draw_food(self, window):
        pygame.draw.rect(window, WHITE, [self.position[0], self.position[1] , 20, 20])
        #print(self.random_position)
        pygame.display.update()
        

class Snake:
    def __init__(self):
        self.velocity = 20
        self.snake_body = [[220,220], [220,240], [220,260], [220, 280]]
        self.actual_movement = random.choice(["right", "left", "up", "down"])
        self.incorrect_movements = {"right": ["left"],
                                    "left": ["right"],
                                    "up": ["down"],
                                    "down": ["up"]}
        self.get_snake_head()

    def move_snake(self, window):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue

                    self.actual_movement = "left"

                if event.key == pygame.K_RIGHT:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue

                    self.actual_movement = "right"

                if event.key == pygame.K_DOWN:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue

                    self.actual_movement = "down"

                if event.key == pygame.K_UP:
                    if self.check_valid_movement(pygame.key.name(event.key)):
                        continue

                    self.actual_movement = "up"


        self.snake_movements(window)


    def draw_snake(self, window):
        for body in self.snake_body:
            pygame.draw.rect(window, RED, [body[0], body[1], 20, 20])

        self.check_error(window)

        pygame.display.update()


    def check_error(self, window):
        if list(self.get_snake_head()) in self.snake_body[2:]:
            print("You lost")
            window.blit(textsurface,(0,0))
            pygame.time.delay(1000)
            self.reset()


    def reset(self):
        self.snake_body = [[220,220], [220,240], [220,260], [220, 280]]
        self.actual_movement = random.choice(["right", "left", "up", "down"]) 

    def snake_movements(self, window):
        if self.actual_movement == "right":
            x = self.snake_body[0][0] + self.velocity
            x = self.check_border(x, "max_limit")
            self.update_snake(x, "x", window)

        if self.actual_movement == "left":
            x = self.snake_body[0][0] - self.velocity
            x = self.check_border(x, "lower_limit")
            self.update_snake(x, "x", window)

        if self.actual_movement == "up":
            y = self.snake_body[0][1] - self.velocity
            y = self.check_border(y, "lower_limit")
            self.update_snake(y, "y", window)   

        if self.actual_movement == "down":
            y = self.snake_body[0][1] + self.velocity
            y = self.check_border(y, "max_limit")
            self.update_snake(y, "y", window)
 

    def update_snake(self, value, cons, window):
        if cons == "y":
            self.snake_body.insert(0, [self.snake_body[0][0], value])
            self.snake_body.pop()
            redraw_window(window)
            self.draw_snake(window)

        elif cons == "x":
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()
            redraw_window(window)
            self.draw_snake(window)

        else:
            print(list(value))
            self.snake_body.insert(0, list(value))
            redraw_window(window)
            self.draw_snake(window)


    def check_border(self, checked_value, limit):
        if limit == "max_limit":
            if checked_value > 480:
                return 0
            else:
                return checked_value
        else:
            if checked_value < 0:
                return 480
            else:
                return checked_value


    def check_valid_movement(self, next_mov):
        if next_mov in self.incorrect_movements[self.actual_movement]:
            return True

    
    def get_snake_head(self):
        return tuple(self.snake_body[0])


def draw(window):
    x = 0
    y = 0
    for _ in range(WIDTH):
        x += GRID_SIZE
        y += GRID_SIZE

        pygame.draw.line(window, BLACK, (x, 0), (x, WIDTH))
        pygame.draw.line(window, BLACK, (0, y), (HEIGHT, y))

        

def redraw_window(window):
    window.fill(BLUE)
    draw(window)
    pygame.display.update()


def main():
    
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(BLUE)
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    run = True

    while run:
        #pygame.time.delay(5)
        clock.tick(9)

        draw(window)
        snake.move_snake(window)

        if snake.get_snake_head() == food.position:
            snake.update_snake(food.position, "w", window)
            food.random_position()
            food.draw_food(window)


        food.draw_food(window)

main()