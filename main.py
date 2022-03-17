# Joshua Martinez
import random

import pygame
import time

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple_.png")
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, Game.display_x)
        self.y = random.randint(0, Game.display_y)


class Snake:

    def __init__(self, parent_screen, length):
        self.length = length
        self.direction = None
        self.parent_screen = parent_screen
        self.snake_head = pygame.image.load("resources/snake_head.png")
        self.snake_body = pygame.image.load("resources/snake_.png")
        self.snake_player_x = [SIZE] * length
        self.snake_player_y = [SIZE] * length

    def draw(self):
        self.parent_screen.blit(self.snake_head, (self.snake_player_x[0], self.snake_player_y[0]))

        for i in range(1, self.length):
            self.parent_screen.blit(self.snake_body,
                                    (self.snake_player_x[i], self.snake_player_y[i]))

    def grow(self):
        self.length += 1
        self.snake_player_x.append(-1)
        self.snake_player_y.append(-1)

    def boundary_check(self):

        if self.snake_player_x[0] <= 0:
            self.snake_player_x[0] = 0
        if self.snake_player_x[0] >= 750:
            self.snake_player_x = 750
        if self.snake_player_y[0] <= 0:
            self.snake_player_y[0] = 0
        if self.snake_player_y[0] >= 550:
            self.snake_player_y[0] = 550

        # if 0 >= self.snake_player_x:
        #     self.snake_player_x = 0
        # elif self.snake_player_x >= 750:
        #     self.snake_player_x = 750
        # if 0 >= self.snake_player_y:
        #     self.snake_player_y = 0
        # elif self.snake_player_y >= 550:
        #     self.snake_player_y = 550

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        # self.boundary_check()

        for i in range(self.length - 1, 0, -1):
            self.snake_player_x[i] = self.snake_player_x[i - 1]
            self.snake_player_y[i] = self.snake_player_y[i - 1]

        if self.direction == "up":
            self.snake_player_y[0] -= SIZE
        if self.direction == "down":
            self.snake_player_y[0] += SIZE
        if self.direction == "left":
            self.snake_player_x[0] -= SIZE
        if self.direction == "right":
            self.snake_player_x[0] += SIZE

        self.draw()


class Game:
    display_x = 960
    display_y = 640

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Game.display_x, Game.display_y))
        pygame.display.set_caption("Snake Game")
        icon = pygame.image.load("resources/snake.png")
        pygame.display.set_icon(icon)
        self.snake = Snake(self.screen, 5)
        self.apple = Apple(self.screen)
        self.apple.draw()

    def show_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score, (600, 10))

    def play(self):
        self.show_score()
        self.apple.draw()
        self.snake.walk()
        time.sleep(0.15)

        if self.is_collision(self.snake.snake_player_x[0], self.snake.snake_player_y[0], self.apple.x, self.apple.y):
            print("Collision occurred")
            self.apple.move()
            self.snake.grow()

        # for i in range(1, self.snake.length):
        #     if self.is_collision(self.snake.snake_player_x[0],
        #                          self.snake.snake_player_y[0],
        #                          self.snake.snake_player_x[i],
        #                          self.snake.snake_player_y[i]):
        #         raise "Game Over"

        pygame.display.update()

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def show_game_over(self):
        self.screen.fill((200, 200, 200))
        font = pygame.font.SysFont('arial', 50)
        score_message = font.render(f"Your Score is: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score_message, (30, 30))
        game_over_message = font.render(f"Game Over! Press Enter to try again or Esc to exit.", True, (255, 255, 255))
        self.screen.blit(game_over_message, (30, 100))
        pygame.display.update()

    def run(self):
        pause = False
        running = True
        while running:

            self.screen.fill((100, 200, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.K_RETURN:
                    pause = True

                if not pause:
                    # if keystroke is pressed, check direction
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN:
                            self.snake.move_down()
                        if event.type == pygame.K_ESCAPE:
                            running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
            # self.play()


if __name__ == "__main__":
    game = Game()
    game.run()
