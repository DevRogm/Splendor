import pygame
from dataclasses import dataclass, field
from game.utils import draw_elements, element_detection, get_img
import os


@dataclass
class StartView:
    active_view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen):
        # Prepare game title and display
        splendor_img = get_img("splendor.png")
        self.draw_image(screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)

        # Prepare Game option
        game_option_img = get_img("game_option.png")
        self.draw_image(screen, game_option_img, factor_pos_x=0.5, factor_pos_y=0.5, action_name='go_to_game_menu')

        # Prepare Statistics option
        statistics_option_img = get_img("statistics_option.png")
        self.draw_image(screen, statistics_option_img, factor_pos_x=0.5, factor_pos_y=0.6,
                        action_name='go_to_statistics')

        # Prepare Quit option
        game_quit_img = get_img("quit_option.png")
        self.draw_image(screen, game_quit_img, factor_pos_x=0.5, factor_pos_y=0.7, action_name='game_quit')

    def draw_image(self, screen, img_path, factor_pos_x=0.0, factor_pos_y=0.0, action_name=None) -> None:
        img = pygame.image.load(img_path)
        pos_x = screen.get_width() * factor_pos_x - img.get_width() / 2
        pos_y = screen.get_height() * factor_pos_y - img.get_height() / 2
        screen.blit(img, (pos_x, pos_y))
        element_edges = ((pos_x, pos_y), (pos_x + img.get_width(), pos_y + img.get_height()))
        if action_name:
            self.active_view_elements.setdefault(action_name, element_edges)

    def action(self, game_view):
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values):
                return self.__getattribute__(element_key)()

    def go_to_game_menu(self, game_view):
        print("GO TO GAME MENU")
        # game_view.change_view('game_menu_view')

    def go_to_statistics(self, game_view):
        print("GO TO STATISTICS")
        # game_view.change_view('statistics_view')

    def game_quit(self):
        return "quit"
