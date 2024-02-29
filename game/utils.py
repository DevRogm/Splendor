import pygame
import os


def draw_img(screen, images_path, image_name, pos_x=0, pos_y=0):
    img_path = os.path.join(images_path, image_name)
    img = pygame.image.load(img_path)
    img_position = (
        screen.get_width() / 2 - img.get_width() / 2 - pos_x, screen.get_height() / 2 - img.get_height() / 2 - pos_y)
    screen.blit(img, img_position)
