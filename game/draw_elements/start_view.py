import pygame
import os
from dataclasses import dataclass
from game.utils import draw_img


@dataclass
class StartView:
    pass

    def draw(self, screen, images_path):
        # Prepare game title and display
        draw_img(screen, images_path, "splendor.png", pos_y=200)

        # Prepare Game option
        draw_img(screen, images_path, "game_option.png")

        # Prepare Statistics option
        draw_img(screen, images_path, "statistics_option.png", pos_y=-80)

        # Prepare Quit option
        quit_option_img_path = os.path.join(images_path, "quit_option.png")
        draw_img(screen, images_path, "quit_option.png", pos_y=-160)
