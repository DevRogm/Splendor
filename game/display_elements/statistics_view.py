from dataclasses import dataclass, field
from game.utils import element_detection, draw_statistic, draw_image, get_img
from game.game_db.db_worker import DBWorker
from typing import Any


@dataclass
class StatisticsView:
    active_view_elements: dict = field(default_factory=lambda: {})
    is_get_stats = False
    is_reset_stats = False

    def draw(self, screen) -> None:
        """
        A method that draws elements on the screen
        :param screen: Surface to display elements
        :return: None
        """
        # Prepare Statistics title and display
        statistics_option_img = get_img("statistics_option.png")
        draw_image(self, screen, statistics_option_img, factor_pos_x=0.5, factor_pos_y=0.1)

        # Prepare list of player with scores, - to do: add pagination and read data from db
        draw_statistic(screen, data=self.data)

        # Back to previous view button
        back_img = get_img("back.png")
        draw_image(self, screen, back_img, factor_pos_x=0.95, factor_pos_y=0.9, action_name='go_to_start_view')

        # Reset stats button
        reset_img = get_img("reset_stats.png")
        draw_image(self, screen, reset_img, factor_pos_x=0.08, factor_pos_y=0.9, action_name='reset_stats')

    def action(self, game_view) -> Any:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values) and element_key == 'reset_stats':
                return element_key

    def go_to_start_view(self, game_view) -> None:
        """
        A method that changes the view to Start View
        :param game_view: Instance of GameViews
        :return: None
        """
        self.is_get_stats = False
        self.is_reset_stats = False
        game_view.change_view('start_view')

    def reset_stats(self, db_worker):
        if not self.is_reset_stats:
            db_worker.reset_data()
        self.is_reset_stats = True
        self.is_get_stats = False

    def get_stats(self, db_worker):
        if not self.is_get_stats:
            self.__setattr__('data', db_worker.read_data())
        self.is_get_stats = True
