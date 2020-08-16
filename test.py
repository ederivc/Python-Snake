import random
import pygame

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRID_SIZE = 20


class Snake:
    def __init__(self):
        self.velocity = 20
        self.snake_body = [[0,0], [0,1], [0,2], [0, 3]]
        self.random_movement()
        self.actual_movement = "right"
        self.turn = " "

    def move_snake(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actual_movement = "left"

                if event.key == pygame.K_RIGHT:
                    self.actual_movement = "right"

                if event.key == pygame.K_DOWN:
                    self.actual_movement = "down"

                if event.key == pygame.K_UP:
                    self.actual_movement = "up"


        self.snake_movements(window)


    def draw_snake(self, window):
        for body in self.snake_body:
            pygame.draw.rect(window, RED, [body[0], body[1], 20, 20])
        pygame.display.update()



    def check_movement(self, window, movement):
        for i, value in enumerate(self.snake_body):
            self.snake_body[i][1] += self.velocity

        print(self.snake_body)
        self.draw_snake(window)


    def random_movement(self):
        pass


    def snake_movements(self, window):
        if self.actual_movement == "right":
            x = self.snake_body[0][0] + self.velocity
            self.update_snake(x, "x", window)

        if self.actual_movement == "left":
            x = self.snake_body[0][0] - self.velocity
            self.update_snake(x, "x", window)

        if self.actual_movement == "up":
            y = self.snake_body[0][1] - self.velocity
            self.update_snake(y, "y", window)   

        if self.actual_movement == "down":
            y = self.snake_body[0][1] + self.velocity
            self.update_snake(y, "y", window)
 

    def update_snake(self, value, cons, window):
        if cons == "y":
            self.snake_body.insert(0, [self.snake_body[0][0], value])
            self.snake_body.pop()
            redraw_window(window)
            self.draw_snake(window)

        else:
            self.snake_body.insert(0, [value, self.snake_body[0][1]])
            self.snake_body.pop()
            redraw_window(window)
            self.draw_snake(window)





def draw(window):
    x = 0
    y = 0
    for _ in range(WIDTH):
        x += GRID_SIZE
        y += GRID_SIZE

        pygame.draw.line(window, BLACK, (x, 0), (x, WIDTH))
        pygame.draw.line(window, BLACK, (0, y), (HEIGHT, y))


def redraw_window(window):
    window.fill(WHITE)
    draw(window)
    pygame.display.update()


def main():
    
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(WHITE)
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    snake = Snake()

    run = True

    while run:
        #pygame.time.delay(50)
        clock.tick(10)

        draw(window)

        snake.move_snake(window)


main()