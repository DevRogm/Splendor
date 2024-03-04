from dataclasses import dataclass, field
from game.utils import draw_el_and_save_their_edges, element_detection, draw_statistic
from typing import Type


@dataclass
class StatisticsView:
    view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path) -> None:
        """
        A method that calls other methods which draw some elements and return the edges of those elements
        :param screen: Surface to display elements
        :param images_path: Path of images
        :return: None
        """
        # Prepare Statistics title and display
        draw_el_and_save_their_edges(self, screen, images_path, "statistics_option.png", pos_y=300)

        # Prepare list of player with scores, - to do: add pagination and read data from db
        draw_statistic(screen)

        # Back to previous view button
        draw_el_and_save_their_edges(self, screen, images_path, "back.png", pos_x=-550, pos_y=-300,
                                     element_name='back_to_start_view')

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                self.__getattribute__(element_key)(game_view)

    def back_to_start_view(self, game_view) -> None:
        """
        A method that changes the view to Start View
        :param game_view: Instance of GameViews
        :return: None
        """
        game_view.change_view('start_view')
