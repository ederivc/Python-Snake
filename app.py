import sys
import random
import pygame
import tkinter as tk
from tkinter import messagebox as mBox

WIDTH = 500
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (231, 109, 25)
BLUE = (68, 125, 226)
GRID_SIZE = 20

class Block:
    def __init__(self):
        self.position = (0, 0)
        self.random_position()

    def random_position(self):
        self.position = [(random.randrange(0, 500, 20), random.randrange(0, 500, 20)) for i in range(7)]


    def draw_food(self, window):
        for _, value in enumerate(self.position):
            pygame.draw.rect(window, BLACK, [value[0], value[1], 20, 20])

        pygame.display.update()


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.random_position()

    def random_position(self):
        self.position = (random.randrange(0, 500, 20), random.randrange(0, 500, 20))

    def draw_food(self, window):
        pygame.draw.rect(window, WHITE, [self.position[0], self.position[1] , 20, 20])
        pygame.display.update()
        

class Snake:
    def __init__(self):
        self.velocity = 20
        self.lenght = 1
        self.snake_body = [[220,220]]
        self.actual_movement = random.choice(["right", "left", "up", "down"])
        self.incorrect_movements = {"right": ["left"],
                                    "left": ["right"],
                                    "up": ["down"],
                                    "down": ["up"]}
        self.best_score = 1
        self.temp_score = 1

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

                if event.key == pygame.K_p:
                    pause_game(window)


        self.snake_movements(window)


    def draw_snake(self, window):
        for body in self.snake_body:
            pygame.draw.rect(window, ORANGE, [body[0], body[1], 20, 20])
        
        self.check_error(window)


    def check_error(self, window):
        if list(self.get_snake_head()) in self.snake_body[2:]:
            self.reset()


    def reset(self):
        message(self.lenght) 
        self.snake_body = [[220,220]]
        self.actual_movement = random.choice(["right", "left", "up", "down"])

        if self.lenght > self.temp_score:
            self.temp_score = self.lenght
            self.best_score = self.lenght
        
        self.lenght = 1


    def snake_movements(self, window):
        if self.actual_movement == "right":
            temp = self.snake_body[0][0] + self.velocity
            x = self.check_bounds(temp, "max_limit")
            self.update_snake(x, "X", window)

        if self.actual_movement == "left":
            temp = self.snake_body[0][0] - self.velocity
            x = self.check_bounds(temp, "lower_limit")
            self.update_snake(x, "X", window)

        if self.actual_movement == "up":
            temp = self.snake_body[0][1] - self.velocity
            y = self.check_bounds(temp, "lower_limit")
            self.update_snake(y, "Y", window)   

        if self.actual_movement == "down":
            temp = self.snake_body[0][1] + self.velocity
            y = self.check_bounds(temp, "max_limit")
            self.update_snake(y, "Y", window)
 

    def update_snake(self, value, key, window):
        if key == "X":
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()
            draw(window)
            self.draw_snake(window)

        else:
            self.snake_body.insert(0, [self.snake_body[0][0], value])
            self.snake_body.pop()
            draw(window)
            self.draw_snake(window)


    def grow_snake(self, value, window):
        self.snake_body.insert(0, list(value))
        draw(window)
        self.draw_snake(window)


    def check_bounds(self, checked_value, limit):
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


def message(score):
    root = tk.Tk()
    root.withdraw()
    mBox.showerror("YOU LOST", f"Your score is: {score}")
    try:
        root.destroy()
    except:
        pass


def draw(window):
    window.fill(BLUE)
    x = 0
    y = 0
    for _ in range(WIDTH):
        x += GRID_SIZE
        y += GRID_SIZE

        pygame.draw.line(window, BLACK, (x, 0), (x, WIDTH))
        pygame.draw.line(window, BLACK, (0, y), (HEIGHT, y))


def check_food(snake, food, window):
    if snake.get_snake_head() == food.position:

        snake.grow_snake(food.position, window)

        food.random_position()
        food.draw_food(window)

        snake.lenght += 1

        if snake.lenght > snake.best_score:
            snake.best_score += 1

        print(food.position)


def check_block(snake, block):
    if snake.get_snake_head() in block.position:
        block.random_position()
        snake.reset()
       

def start_menu(start, window):
    window.fill(WHITE)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key:
                #start = False
                return False

    return True


def pause_game(window):

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_r:
                    pass

        window.fill(ORANGE)
        pygame.display.update()
   


"""def main():
    
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(BLUE)
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    block = Block()
    
    myfont = pygame.font.SysFont('Helvetica', 20)
    start = True

    while True:

        clock.tick(11)

        while start:
            start = start_menu(start, window)
                        

        draw(window)
        snake.move_snake(window)


        check_block(snake, block)
        check_food(snake, food, window)
        
        text = myfont.render(f'Score {snake.lenght}', True, BLACK)
        window.blit(text, (5, 0))
        text2 = myfont.render(f'Best score {snake.best_score}', True, BLACK)
        window.blit(text2, (5, 20))

        block.draw_food(window)
        while True:
            if food.random_position in block.position:
                print(f"Here, food {food.position} , block {block.position}")
                food.random_position
                print(f"Final {food.position}")

            break
        food.draw_food(window)

        #pause_game(start)"""


#main()