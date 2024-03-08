import random
import pygame
import os


def draw_elements(view, screen, images_path, image_name, pos_x=0, pos_y=0, element_name=None) -> None:
    """
    A methods that draws element and save them edges if an element name passed
    :param view: current view
    :param screen: Surface for displaying elements
    :param images_path: Paths of all images
    :param image_name: Name of the image
    :param pos_x: Position x for the element
    :param pos_y: Position y for the element
    :param element_name: Name of the element
    :return: None
    """
    img_path = os.path.join(images_path, image_name)
    img = pygame.image.load(img_path)
    img_position = (
        screen.get_width() / 2 - img.get_width() / 2 - pos_x, screen.get_height() / 2 - img.get_height() / 2 - pos_y)
    screen.blit(img, img_position)
    el_edges = (img_position, (img_position[0] + img.get_width(), img_position[1] + img.get_height()))

    if element_name:
        view.view_elements.setdefault(element_name, el_edges)


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


def draw_simple_text(screen, text, pos_x=0, pos_y=0, font_size=36):
    my_font = pygame.font.SysFont('ARIAL', font_size)
    player_name = my_font.render(text.upper(), True, (227, 206, 0))
    player_name_position = (
        screen.get_width() / 2 - player_name.get_width() / 2 - pos_x,
        screen.get_height() / 2 - pos_y)
    screen.blit(player_name, player_name_position)


def draw_marker_quantities(screen, text, pos_x=0, pos_y=0):
    my_font = pygame.font.SysFont('ARIAL', 20)
    player_name = my_font.render(text.upper(), True, (227, 206, 0))
    player_name_position = (pos_x, pos_y)
    screen.blit(player_name, player_name_position)


def draw_game_area(screen, game_area):
    if not game_area:
        game_area = pygame.Surface((screen.get_width() / 2, screen.get_height()))
    pygame.draw.rect(game_area, (250, 0, 0), (0, 0, game_area.get_width(),
                                              game_area.get_height()), 1)
    screen.blit(game_area, (screen.get_width() / 2, 0))
    return game_area


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


def draw_markers_area(screen, game_area_surface):
    pygame.draw.rect(game_area_surface, (250, 0, 0), (0, 0, game_area_surface.get_width(),
                                                      game_area_surface.get_height()), 1)
    screen.blit(game_area_surface, (220, 0))


def draw_stone_requirements(view, screen, stone_name, quantity, pos_x=0, pos_y=0) -> None:
    colors = {'emerald': (32, 102, 0, 100),
              'sapphire': (83, 142, 199),
              'onyx': (82, 68, 68, 100),
              'diamond': (226, 219, 219, 100),
              'ruby': (159, 0, 0, 100),
              }
    pygame.draw.circle(screen, colors[stone_name], (screen.get_width() / 2 - pos_x, screen.get_height() / 2 - pos_y),
                       10, 0)

    my_font = pygame.font.SysFont('ARIAL', 18, True)
    stone_quantity = my_font.render(str(quantity), True, (0, 0, 0))
    stone_quantity_position = (
        screen.get_width() / 2 - pos_x - 5,
        screen.get_height() / 2 - pos_y - 8)
    screen.blit(stone_quantity, stone_quantity_position)


def draw_card_requirements(view, screen, stone_name, quantity, pos_x=0, pos_y=0) -> None:
    colors = {'emerald': (32, 102, 0, 100),
              'sapphire': (83, 142, 199),
              'onyx': (82, 68, 68, 100),
              'diamond': (226, 219, 219, 100),
              'ruby': (159, 0, 0, 100),
              }
    pygame.draw.rect(screen, colors[stone_name], (screen.get_width() / 2 - pos_x, screen.get_height() / 2 - pos_y,
                                                  15, 20))

    my_font = pygame.font.SysFont('ARIAL', 18, True)
    card_quantity = my_font.render(str(quantity), True, (0, 0, 0))
    card_quantity_position = (
        screen.get_width() / 2 - pos_x + 3,
        screen.get_height() / 2 - pos_y + 2)
    screen.blit(card_quantity, card_quantity_position)


def draw_statistic(screen, font_size=26, data=None) -> None:
    """
    A method that displays player scores
    :param screen:  Surface for displaying elements
    :param data: Data from db
    :return: None
    """

    # Dummy data, data from database will be added
    dummy_data = {
        1: {'nickname': "Lenny", "score": 24, "date": "21-03-2021"},
        2: {'nickname': "Lenny", "score": 22, "date": "23-02-2021"},
        3: {'nickname': "Lenny", "score": 21, "date": "13-01-2021"},
        4: {'nickname': "Lenny", "score": 14, "date": "23-03-2021"},
        5: {'nickname': "Lenny", "score": 12, "date": "12-05-2021"}
    }
    my_font = pygame.font.SysFont('ARIAL', font_size)
    player_score = my_font.render("Lp.       Nickname        Score             Date", True, (227, 206, 0))
    screen.blit(player_score, (400, 200))
    for data_key, data_values in dummy_data.items():
        player_score = my_font.render(
            f"{data_key}.{12 * ' '}{data_values['nickname']}{14 * ' '}{data_values['score']}{12 * ' '}{data_values['date']}",
            True, (227, 206, 0))
        screen.blit(player_score, (400, 200 + data_key * 50))


def draw_image(view, screen, img_path, factor_pos_x=0.0, factor_pos_y=0.0, action_name=None) -> None:
    k_x = screen.get_width() / 1280
    k_y = screen.get_height() / 720
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (img.get_width()*k_x, img.get_height()*k_y))
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
