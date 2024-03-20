import random
import pygame
import os


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

