# Joshua Martinez

import pygame


class Snake:

    def __init__(self, parent_screen):
        # The SNAKE
        self.parent_screen = parent_screen
        self.snake_player = pygame.image.load("resources/snake_player.png")
        self.snake_player_x = 0
        self.snake_player_y = 0

    def draw(self):
        self.parent_screen.blit(self.snake_player, (self.snake_player_x, self.snake_player_y))

    def move_right(self):
        self.snake_player_x += 10

    def move_left(self):
        self.snake_player_x -= 10

    def move_up(self):
        self.snake_player_y -= 10

    def move_down(self):
        self.snake_player_y += 10


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        icon = pygame.image.load("resources/snake.png")
        pygame.display.set_icon(icon)
        self.snake = Snake(self.screen)

    def run(self):

        running = True
        while running:

            self.screen.fill((100, 200, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    running = False

                # if keystroke is pressed, check direction
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("Left arrow pressed")
                    if event.key == pygame.K_RIGHT:
                        print("Right arrow pressed")
                    if event.key == pygame.K_UP:
                        print("Up arrow pressed")
                    if event.key == pygame.K_DOWN:
                        print("Down arrow pressed")

                # upon keystroke release, player will move
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
            self.snake.draw()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
