import pygame
import os


def draw_el_and_save_their_edges(view, screen, images_path, image_name, pos_x=0, pos_y=0, element_name=None):
    img_path = os.path.join(images_path, image_name)
    img = pygame.image.load(img_path)
    img_position = (
        screen.get_width() / 2 - img.get_width() / 2 - pos_x, screen.get_height() / 2 - img.get_height() / 2 - pos_y)
    screen.blit(img, img_position)
    el_edges = (img_position, (img_position[0] + img.get_width(), img_position[1] + img.get_height()))

    if element_name:
        view.view_elements.setdefault(element_name, el_edges)


def element_detection(element_edges):
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

