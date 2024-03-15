import pygame
from game.display_elements.game_views import GameViews
from utils import get_img

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(' . . o o O O SPLENDOR O O o o . . ')
clock = pygame.time.Clock()
running = True
dt = 0
table = get_img('table.png')
table_img = pygame.image.load(table)

# Init game_board and game_views
game_views = GameViews()

while running:
    screen.blit(pygame.transform.scale(table_img, (1280, 720)), (0, 0))
    # Display game view
    game_views.display_view(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            action = game_views.do_action()
            if action == "start_game" or action == "play_again":
                players = game_views.game_menu_view.players
                game_views.game_board_view.game_preparation(players, action)
            if game_views.game_board_view.show_results:
                game_views.change_view("results_view")
                game_views.results_view.players = game_views.game_board_view.players
                game_views.game_board_view.show_results = False
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
