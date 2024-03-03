from dataclasses import dataclass, field
from game.utils import draw_el_and_save_their_edges, element_detection, draw_statistic


@dataclass
class StatisticsView:
    view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path):
        # Prepare Statistics title and display
        draw_el_and_save_their_edges(self, screen, images_path, "statistics_option.png", pos_y=300)

        # Prepare list of player with scores, with pagination
        draw_statistic("lol", screen)
        # Prepare Statistics title and display
        draw_el_and_save_their_edges(self, screen, images_path, "back.png", pos_x=-550, pos_y=-300,
                                     element_name='back_to_start_view')

    def action(self, game_view):
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                self.__getattribute__(element_key)(game_view)

    def back_to_start_view(self, game_view):
        game_view.change_view('start_view')

