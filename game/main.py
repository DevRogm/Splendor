import pygame
import os
from game.game_elements.game_board import GameBoard
from game.draw_elements.game_views import GameViews
from utils import element_detection

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(' . . o o O O SPLENDOR O O o o . . ')
clock = pygame.time.Clock()
running = True
dt = 0
test_game_board = True  # remove after work on game board

# Game Global Variables
images_path = os.path.abspath('../images')

# Init game_board and game_views
game_views = GameViews()

while running:
    # Display game view
    game_views.draw_view(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            action = game_views.do_action()
            if action == "start_game":
                players = game_views.game_menu_view.players
                game_views.game_board_view.game_board.game_preparation(players)
            if action == "quit":
                running = False
        if game_views.current_view == "game_menu_view" and game_views.game_menu_view.num_of_players:
            if event.type == pygame.KEYDOWN:
                game_views.game_menu_view.add_player_name(event.key)
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    dt = clock.tick(60) / 1000
pygame.quit()
