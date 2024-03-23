import operator
import datetime
from dataclasses import dataclass, field
from game.utils import get_img, draw_image, element_detection, display_results as draw_result


@dataclass
class ResultsView:
    active_view_elements: dict = field(default_factory=lambda: {})
    players = None
    is_save_stats = False

    def draw(self, screen):
        """
        A method that draws elements on the screen
        :param screen: Surface to display elements
        :return: None
        """
        splendor_img = get_img("game_results.png")
        draw_image(self, screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)
        self.display_results(screen)

        play_again_img = get_img("play_again.png")
        draw_image(self, screen, play_again_img, factor_pos_x=0.85, factor_pos_y=0.8, action_name='go_to_game_view')

        back_to_start_img = get_img("back_to_start_view.png")
        draw_image(self, screen, back_to_start_img, factor_pos_x=0.2, factor_pos_y=0.8, action_name='go_to_start_view')

    def display_results(self, screen):
        """
        A method that displays result on the screen
        :param screen: Surface to display elements
        :return: None
        """
        sorted_players = sorted(self.players, key=operator.attrgetter('points'), reverse=True)
        draw_result(screen, data=sorted_players)

    def action(self, game_view):
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values):
                return self.__getattribute__(element_key)()

    def go_to_start_view(self, game_view):
        game_view.game_board_view.reset_game()
        game_view.game_menu_view.temp_name = ''
        game_view.game_menu_view.players = {}
        game_view.game_menu_view.can_start_game = False
        game_view.game_menu_view.active_player = 1
        self.is_save_stats = False
        game_view.change_view('start_view')

    def go_to_game_view(self, game_view):
        game_view.game_board_view.reset_game(play_again=True)
        game_view.game_menu_view.active_player = self.players[1]
        game_view.change_view('game_board_view')
        self.is_save_stats = False
        return "play_again"

    def save_stats(self, db_worker):
        if not self.is_save_stats:
            for player in self.players:
                db_worker.update_data(player)
        self.is_save_stats = True
