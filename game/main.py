import pygame
from game.game_elements.game_board import GameBoard
from game.draw_elements.game_views import GameViews
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(' . . o o SPLENDOR o o . . ')
clock = pygame.time.Clock()
running = True
dt = 0

# Game Global Variables


# Init game_board and game_views
game_board = GameBoard()
game_views = GameViews()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
