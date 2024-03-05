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


def draw_statistic(screen, data=None) -> None:
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
    my_font = pygame.font.SysFont('ARIAL', 26)
    player_score = my_font.render("Lp.       Nickname        Score             Date", True, (227, 206, 0))
    screen.blit(player_score, (400, 200))
    for data_key, data_values in dummy_data.items():
        player_score = my_font.render(
            f"{data_key}.{12 * ' '}{data_values['nickname']}{14 * ' '}{data_values['score']}{12 * ' '}{data_values['date']}",
            True, (227, 206, 0))
        screen.blit(player_score, (400, 200 + data_key * 50))


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


def draw_simple_text(screen, text, pos_x=0, pos_y=0):
    my_font = pygame.font.SysFont('ARIAL', 36)
    player_name = my_font.render(text.upper(), True, (227, 206, 0))
    player_name_position = (
        screen.get_width() / 2 - player_name.get_width() / 2,
        screen.get_height() / 2 - pos_y)
    screen.blit(player_name, player_name_position)


def draw_game_area(screen):
    game_area_surface = pygame.Surface((screen.get_width() / 2, screen.get_height()))
    pygame.draw.rect(game_area_surface, (250, 0, 0), (0, 0, screen.get_width() / 2,
                                                      screen.get_height()), 1)
    screen.blit(game_area_surface, (screen.get_width() / 2, 0))

    def draw_player_area(screen):
        pygame.draw.rect(screen, (250, 0, 0), (screen.get_width() / 2, 0, screen.get_width() / 2,
                                               screen.get_height()), 2)

    def draw_stone_card(screen):
        pass

    def draw_reverse_card(screen):
        pass

    def draw_markers(screen):
        pass

    def draw_aristocratic_card(screen):
        pass
