from dataclasses import dataclass, field
from game.utils import draw_el_and_save_their_edges, element_detection


@dataclass
class StartView:
    view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path):
        # Prepare game title and display
        draw_el_and_save_their_edges(self, screen, images_path, "splendor.png", pos_y=200)
        # Prepare Game option
        draw_el_and_save_their_edges(self, screen, images_path, "game_option.png",
                                     element_name='go_to_game_menu')
        # Prepare Statistics option
        draw_el_and_save_their_edges(self, screen, images_path, "statistics_option.png", pos_y=-80,
                                     element_name='go_to_statistics')
        # Prepare Quit option
        draw_el_and_save_their_edges(self, screen, images_path, "quit_option.png", pos_y=-160,
                                     element_name='game_quit')

    def action(self, game_view):
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                self.__getattribute__(element_key)(game_view)

    def go_to_game_menu(self, game_view):
        game_view.change_view('game_menu_view')

    def go_to_statistics(self, game_view):
        print("Go to statistics", self)

    def game_quit(self, game_view):
        print("Game quit", self)
