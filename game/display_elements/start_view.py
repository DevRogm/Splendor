from dataclasses import dataclass, field
from game.utils import element_detection, get_img, draw_image
from typing import Callable


@dataclass
class StartView:
    active_view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen) -> None:
        """
        A method that draws elements on the screen
        :param screen: Surface to display elements
        :return: None
        """

        # Prepare game title and display
        splendor_img = get_img("splendor.png")
        draw_image(self, screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)

        # Prepare Game option
        game_option_img = get_img("game_option.png")
        draw_image(self, screen, game_option_img, factor_pos_x=0.5, factor_pos_y=0.5, action_name='go_to_game_menu')

        # Prepare Statistics option
        statistics_option_img = get_img("statistics_option.png")
        draw_image(self, screen, statistics_option_img, factor_pos_x=0.5, factor_pos_y=0.6,
                   action_name='go_to_statistics')

        # Prepare Quit option
        game_quit_img = get_img("quit_option.png")
        draw_image(self, screen, game_quit_img, factor_pos_x=0.5, factor_pos_y=0.7, action_name='game_quit')

    def action(self, game_view):
        """
        A method that does the action from the active elements
        # :param game_view: Surface to display elements
        :return: None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values):
                return self.__getattribute__(element_key)()

    @staticmethod
    def go_to_game_menu(game_view) -> None:
        """
        A method that changes the displaying view to game menu view
        :param game_view: Surface to display elements
        :return: None
        """
        game_view.change_view('game_menu_view')

    @staticmethod
    def go_to_statistics(game_view) -> None:
        """
        A method that changes the displaying view to statistics view
        :param game_view: Surface to display elements
        :return: None
        """
        game_view.change_view('statistics_view')

    @staticmethod
    def game_quit() -> str:
        """
        A method that returns string to exit the game
        :return: 'Quit' string
        """
        return "quit"
