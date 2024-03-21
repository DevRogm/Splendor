from dataclasses import dataclass, field
from game.utils import element_detection, draw_statistic, draw_image, get_img
from game.game_db.db_worker import DBWorker


@dataclass
class StatisticsView:
    active_view_elements: dict = field(default_factory=lambda: {})

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
        draw_statistic(screen)

        # Back to previous view button
        back_img = get_img("back.png")
        draw_image(self, screen, back_img, factor_pos_x=0.95, factor_pos_y=0.9, action_name='back_to_start_view')

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values):
                self.__getattribute__(element_key)(game_view)

    @staticmethod
    def back_to_start_view(game_view) -> None:
        """
        A method that changes the view to Start View
        :param game_view: Instance of GameViews
        :return: None
        """
        game_view.change_view('start_view')


    def get_stats(self):
        db_worker = DBWorker()
        print(db_worker)

