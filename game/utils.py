import random
import pygame
import os
import datetime


def element_detection(element_edges: tuple) -> bool:
    """
    A method that detects view elements on mouse click
    :param element_edges:
    :return:
    """
    el_pos_x = element_edges[0][0]
    el_pos_y = element_edges[0][1]
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    el_pos_x_end = element_edges[1][0]
    el_pos_y_end = element_edges[1][1]

    if el_pos_x <= mouse_x <= el_pos_x_end and el_pos_y <= mouse_y <= el_pos_y_end:
        return True
    else:
        return False


def draw_player_area(screen, player, player_num, player_areas):
    if len(player_areas) != player_num:
        player_area_surface = pygame.Surface((screen.get_width() / 4, screen.get_height() / 2))
    else:
        player_area_surface = player_areas[player]
    pygame.draw.rect(player_area_surface, (250, 0, 0), (0, 0, player_area_surface.get_width(),
                                                        player_area_surface.get_height()), 1)
    player_positions = {1: (0, 0), 2: (player_area_surface.get_width(), 0), 3: (0, player_area_surface.get_height()),
                        4: (player_area_surface.get_width(), player_area_surface.get_height())}
    screen.blit(player_area_surface, player_positions[player])
    return player_area_surface


def draw_statistic(screen, font_size=26, data=None) -> None:
    my_font = pygame.font.SysFont('ARIAL', font_size)

    pos_x = screen.get_width() * 0.04
    pos_y = screen.get_height() * 0.2

    surface_rank = pygame.Surface((screen.get_width() * 0.05, screen.get_height() * 0.6), pygame.SRCALPHA)
    rank = my_font.render("Rank", True, (227, 206, 0))
    surface_rank.blit(rank, (surface_rank.get_width() / 2 - rank.get_width() / 2, 0))

    surface_name = pygame.Surface((screen.get_width() * 0.15, screen.get_height() * 0.6), pygame.SRCALPHA)
    name = my_font.render("Name", True, (227, 206, 0))
    surface_name.blit(name, (surface_name.get_width() / 2 - name.get_width() / 2, 0))

    surface_points = pygame.Surface((screen.get_width() * 0.1, screen.get_height() * 0.6), pygame.SRCALPHA)
    points = my_font.render("Points", True, (227, 206, 0))
    surface_points.blit(points, (surface_points.get_width() / 2 - points.get_width() / 2, 0))

    surface_games = pygame.Surface((screen.get_width() * 0.1, screen.get_height() * 0.6), pygame.SRCALPHA)
    games = my_font.render("Games", True, (227, 206, 0))
    surface_games.blit(games, (surface_games.get_width() / 2 - games.get_width() / 2, 0))

    surface_cards = pygame.Surface((screen.get_width() * 0.1, screen.get_height() * 0.6), pygame.SRCALPHA)
    cards = my_font.render("Cards", True, (227, 206, 0))
    surface_cards.blit(cards, (surface_cards.get_width() / 2 - cards.get_width() / 2, 0))

    surface_aristo = pygame.Surface((screen.get_width() * 0.1, screen.get_height() * 0.6), pygame.SRCALPHA)
    aristo = my_font.render("Aristo", True, (227, 206, 0))
    surface_aristo.blit(aristo, (surface_aristo.get_width() / 2 - aristo.get_width() / 2, 0))

    surface_last_game = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.6), pygame.SRCALPHA)
    last_game = my_font.render("Last Game", True, (227, 206, 0))
    surface_last_game.blit(last_game, (surface_last_game.get_width() / 2 - last_game.get_width() / 2, 0))

    for count, player_score in enumerate(data[:10], 1):
        rank_ply = my_font.render(str(player_score[0]), True, (227, 206, 0))
        surface_rank.blit(rank_ply, (
            surface_rank.get_width() / 2 - rank_ply.get_width() / 2, surface_rank.get_height() * 0.1 * count))

        name_ply = my_font.render(str(player_score[2]).upper(), True, (227, 206, 0))
        surface_name.blit(name_ply, (
            surface_name.get_width() / 2 - name_ply.get_width() / 2, surface_name.get_height() * 0.1 * count))

        points_ply = my_font.render(str(player_score[3]), True, (227, 206, 0))
        surface_points.blit(points_ply, (
            surface_points.get_width() / 2 - points_ply.get_width() / 2, surface_points.get_height() * 0.1 * count))

        games_ply = my_font.render(str(player_score[6]), True, (227, 206, 0))
        surface_games.blit(games_ply, (
            surface_games.get_width() / 2 - games_ply.get_width() / 2, surface_games.get_height() * 0.1 * count))

        cards_ply = my_font.render(str(player_score[4]), True, (227, 206, 0))
        surface_cards.blit(cards_ply, (
            surface_cards.get_width() / 2 - cards_ply.get_width() / 2, surface_cards.get_height() * 0.1 * count))

        aristo_ply = my_font.render(str(player_score[5]), True, (227, 206, 0))
        surface_aristo.blit(cards_ply, (
            surface_aristo.get_width() / 2 - aristo_ply.get_width() / 2, surface_aristo.get_height() * 0.1 * count))

        last_game_ply = my_font.render(str(player_score[-1].strftime("%Y-%m-%d %H:%M:%S")), True, (227, 206, 0))
        surface_last_game.blit(last_game_ply, (
            surface_last_game.get_width() / 2 - last_game_ply.get_width() / 2,
            surface_last_game.get_height() * 0.1 * count))

    screen.blit(surface_rank, (pos_x, pos_y))
    offset_x = screen.get_width() * 0.02 + surface_rank.get_width()
    screen.blit(surface_name, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_name.get_width()
    screen.blit(surface_points, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_points.get_width()
    screen.blit(surface_games, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_games.get_width()
    screen.blit(surface_cards, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_cards.get_width()
    screen.blit(surface_aristo, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_aristo.get_width()
    screen.blit(surface_last_game, (pos_x + offset_x, pos_y))


def display_results(screen, font_size=26, data=None) -> None:
    my_font = pygame.font.SysFont('ARIAL', font_size)

    surface_rank = pygame.Surface((screen.get_width() * 0.05, screen.get_height() * 0.6), pygame.SRCALPHA)
    rank = my_font.render("Rank", True, (227, 206, 0))
    surface_rank.blit(rank, (surface_rank.get_width() / 2 - rank.get_width() / 2, 0))

    surface_name = pygame.Surface((screen.get_width() * 0.15, screen.get_height() * 0.6), pygame.SRCALPHA)
    name = my_font.render("Name", True, (227, 206, 0))
    surface_name.blit(name, (surface_name.get_width() / 2 - name.get_width() / 2, 0))

    surface_points = pygame.Surface((screen.get_width() * 0.1, screen.get_height() * 0.6), pygame.SRCALPHA)
    points = my_font.render("Points", True, (227, 206, 0))
    surface_points.blit(points, (surface_points.get_width() / 2 - points.get_width() / 2, 0))

    for count, player_score in enumerate(data, 1):
        rank_ply = my_font.render(str(count), True, (227, 206, 0))
        surface_rank.blit(rank_ply, (
            surface_rank.get_width() / 2 - rank_ply.get_width() / 2, surface_rank.get_height() * 0.1 * count))

        name_ply = my_font.render(str(player_score.name).upper(), True, (227, 206, 0))
        surface_name.blit(name_ply, (
            surface_name.get_width() / 2 - name_ply.get_width() / 2, surface_name.get_height() * 0.1 * count))

        points_ply = my_font.render(str(player_score.points), True, (227, 206, 0))
        surface_points.blit(points_ply, (
            surface_points.get_width() / 2 - points_ply.get_width() / 2, surface_points.get_height() * 0.1 * count))

    pos_x = screen.get_width() * 0.5 - (
                surface_rank.get_width() + surface_points.get_width() + surface_name.get_width() + 1 * (
                    screen.get_width() * 0.02)) / 2
    pos_y = screen.get_height() * 0.3

    screen.blit(surface_rank, (pos_x, pos_y))
    offset_x = screen.get_width() * 0.02 + surface_rank.get_width()
    screen.blit(surface_name, (pos_x + offset_x, pos_y))
    offset_x += screen.get_width() * 0.02 + surface_name.get_width()
    screen.blit(surface_points, (pos_x + offset_x, pos_y))


def draw_image(view, screen, img_path, factor_pos_x=0.0, factor_pos_y=0.0, action_name=None) -> None:
    k_x = screen.get_width() / 1280
    k_y = screen.get_height() / 720
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (img.get_width() * k_x, img.get_height() * k_y))
    pos_x = screen.get_width() * factor_pos_x - img.get_width() / 2
    pos_y = screen.get_height() * factor_pos_y - img.get_height() / 2
    screen.blit(img, (pos_x, pos_y))
    element_edges = ((pos_x, pos_y), (pos_x + img.get_width(), pos_y + img.get_height()))
    if action_name:
        view.active_view_elements.setdefault(action_name, element_edges)


def get_img(img_name):
    images_path = os.path.abspath('../images')
    img_full_path = os.path.join(images_path, img_name)
    return img_full_path


def draw_simple_text(screen, text, factor_pos_x=0.0, factor_pos_y=0.0, font_size=36, font_name="ARIAL",
                     color=(0, 0, 0)):
    my_font = pygame.font.SysFont(font_name, font_size)
    text = my_font.render(text.upper(), True, color)
    pos_x = screen.get_width() * factor_pos_x - text.get_width() / 2
    pos_y = screen.get_height() * factor_pos_y - text.get_height() / 2
    screen.blit(text, (pos_x, pos_y))


def draw_requirements(screen, stone_card_name, quantity, factor_pos_x=0.0, factor_pos_y=0.0, font_size=18,
                      stone_requirements=False):
    colors = {'emerald': (32, 102, 0, 100),
              'sapphire': (83, 142, 199),
              'onyx': (82, 68, 68, 100),
              'diamond': (226, 219, 219, 100),
              'ruby': (159, 0, 0, 100),
              }
    pos_x = screen.get_width() * factor_pos_x
    pos_y = screen.get_height() * factor_pos_y
    if stone_requirements:
        pygame.draw.circle(screen, colors[stone_card_name], (pos_x, pos_y),
                           10, 0)
    else:
        pygame.draw.rect(screen, colors[stone_card_name], (pos_x - 8, pos_y - 8,
                                                           15, 20))
    my_font = pygame.font.SysFont('ARIAL', font_size, True)
    stone_card_quantity = my_font.render(str(quantity), True, (0, 0, 0))
    stone_card_quantity_position = (screen.get_width() * factor_pos_x - 5, screen.get_height() * factor_pos_y - 7)
    screen.blit(stone_card_quantity, stone_card_quantity_position)


class ExitLoop(BaseException):
    pass
