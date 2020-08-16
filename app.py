import sys
import time
import pygame

class Snake:
    def __init__(self):
        self.velocity = 5
        self.x = 200
        self.y = 200
        self.snake_list = [200, 200]
        self.snake_body = [[200, 200]]
        self.direction = "right"

    def draw(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x -= self.velocity
                    #self.increment_velocity()
                    self.direction = "left"
                    self.update_display(window)

                if event.key == pygame.K_RIGHT:
                    self.x += self.velocity
                    #self.increment_velocity()
                    self.direction = "right"
                    self.update_display(window)

                if event.key == pygame.K_DOWN:
                    self.snake_list[1] += self.velocity
                    #self.increment_velocity()
                    self.direction = "down"
                    self.update_display(window)

                if event.key == pygame.K_UP:
                    self.y -= self.velocity
                    #self.increment_velocity()
                    self.direction = "up"
                    self.update_display(window)


        if self.direction == "right":
            x = self.snake_body[0][0] + self.velocity
            self.snake_body.insert(0, [x, self.snake_body[0][1]])
            self.snake_body.pop()
            window.fill(WHITE)
            self.update_display(window)

        if self.direction == "left":
            x = self.snake_body[0][0] - self.velocity
            self.snake_body.insert(0, [x, self.snake_body[0][1]])
            self.snake_body.pop()
            window.fill(WHITE)
            self.update_display(window)

        if self.direction == "down":
            y = self.snake_body[0][1] + self.velocity
            self.snake_body.insert(0, [self.snake_body[0][0], y])
            self.snake_body.pop()
            window.fill(WHITE)
            self.update_display(window)

        if self.direction == "up":
            y = self.snake_body[0][1] - self.velocity
            self.snake_body.insert(0, [self.snake_body[0][0], y])
            self.snake_body.pop()
            window.fill(WHITE)
            self.update_display(window)


    def update_display(self, window):
        var1 = 20
        var2 = 20
        pygame.draw.rect(window, BLACK, [100, 100, 20, 20])
        
        pygame.draw.rect(window, BLACK, [100, 100, 20, 20])
        for body in self.snake_body:


            pygame.draw.rect(window, BLACK, [body[0], body[1], var1, var2])
            pygame.display.update()

        clock.tick(60)


    def increment_velocity(self):
        self.velocity += 0.5


WIDTH = 900
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

grid_size = 20
grid_width = WIDTH/grid_size
grid_height = HEIGHT/grid_size 
clock = pygame.time.Clock()


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(WHITE)
    pygame.display.set_caption("First Game")
    pygame.display.flip()
    
    snake = Snake()

    while True:
        snake.draw(window)
        pygame.display.update()
        #pygame.display.flip()

main()