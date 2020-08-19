from app import *

if __name__ == "__main__":
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

        #pause_game(start)