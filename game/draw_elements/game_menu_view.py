from dataclasses import dataclass, field
from game.utils import draw_el_and_save_their_edges, element_detection


@dataclass
class GameMenuView:
    view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path):
        pass

    def action(self, game_view):
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                self.__getattribute__(element_key)(game_view)

    def go_to_game_menu(self, game_view):
        pass

    def go_to_statistics(self, game_view):
        pass

    def game_quit(self, game_view):
        pass
