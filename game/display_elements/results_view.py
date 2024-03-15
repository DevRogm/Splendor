import operator
from dataclasses import dataclass, field
from game.utils import get_img, draw_image, draw_simple_text, element_detection


@dataclass
class ResultsView:
    active_view_elements: dict = field(default_factory=lambda: {})
    players = None

    def draw(self, screen):
        splendor_img = get_img("game_results.png")
        draw_image(self, screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)
        self.print_results(screen)

        play_again_img = get_img("play_again.png")
        draw_image(self, screen, play_again_img, factor_pos_x=0.85, factor_pos_y=0.8, action_name='go_to_game_view')

        back_to_start_img = get_img("back_to_start_view.png")
        draw_image(self, screen, back_to_start_img, factor_pos_x=0.2, factor_pos_y=0.8, action_name='go_to_start_view')

    def print_results(self, screen):
        sorted_players = sorted(self.players, key=operator.attrgetter('points'), reverse=True)
        text = f"Lp. NAME POINTS NUM OF CARDS NUM OF ARISTO"
        draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.3, color=(227, 206, 0), font_size=30)
        for count, player in enumerate(sorted_players, start=1):
            text = f"{count} {player.name} {player.points} {self.count_cards(player)} {player.inventory.aristocratic_cards}"
            draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.3 + (count * 0.08), color=(227, 206, 0),
                             font_size=30)

    def count_cards(self, player):
        num_of_cards = sum([len(stone_cards) for stone_cards in player.inventory.stone_cards.values()])
        return num_of_cards

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
        game_view.change_view('start_view')

    def go_to_game_view(self, game_view):
        game_view.game_board_view.reset_game(play_again=True)
        game_view.game_menu_view.active_player = self.players[1]
        game_view.change_view('game_board_view')
        return "play_again"
