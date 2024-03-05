from dataclasses import dataclass, field
from game.utils import draw_elements, element_detection, draw_simple_text
from typing import List


@dataclass
class GameMenuView:
    view_elements: dict = field(default_factory=lambda: {})
    num_of_players: int = 2
    temp_name: str = ''
    active_player: int = 1
    players: dict = field(default_factory=lambda: {})
    can_start_game: bool = False

    def draw(self, screen, images_path):
        if not self.can_start_game:
            # Prepare Game Menu title and display
            draw_elements(self, screen, images_path, "add_players.png", pos_y=300)

            # Select number of players - display
            draw_elements(self, screen, images_path, "select_num_of_players.png", pos_y=200)

            # Select 2 players
            draw_elements(self, screen, images_path, "2_players.png", pos_y=100, pos_x=200,
                                         element_name="select_2_players")
            if self.num_of_players == 2:
                draw_elements(self, screen, images_path, "selected.png", pos_y=100, pos_x=180)

            # Select 3 players
            draw_elements(self, screen, images_path, "3_players.png", pos_y=100,
                                         element_name="select_3_players")
            if self.num_of_players == 3:
                draw_elements(self, screen, images_path, "selected.png", pos_y=100, pos_x=-20)

            # Select 4 players
            draw_elements(self, screen, images_path, "4_players.png", pos_y=100, pos_x=-200,
                                         element_name="select_4_players")
            if self.num_of_players == 4:
                draw_elements(self, screen, images_path, "selected.png", pos_y=100, pos_x=-220)

            # Enter player names - display
            draw_elements(self, screen, images_path, "enter_player_names.png", pos_y=0)

            text = f"Player {self.active_player}: {self.temp_name}"
            draw_simple_text(screen, text, pos_y=-50)

        # Back to previous view
        draw_elements(self, screen, images_path, "back.png", pos_x=-550, pos_y=-300,
                                     element_name='go_to_start_view')

        if self.can_start_game:
            draw_elements(self, screen, images_path, "start_game.png", pos_x=-400, pos_y=-150,
                                         element_name='go_to_game_view')

            for player_k, player_v in self.players.items():
                if player_v:
                    text = f"Player {player_k}: {player_v}"
                    draw_simple_text(screen, text, pos_y=250 - player_k * 70)

    def action(self, game_view):
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values):
                return self.__getattribute__(element_key)()

    def select_2_players(self):
        if not self.can_start_game:
            self.num_of_players = 2

    def select_3_players(self):
        if not self.can_start_game:
            self.num_of_players = 3

    def select_4_players(self):
        if not self.can_start_game:
            self.num_of_players = 4

    def add_player_name(self, char_id):
        if char_id == 13 and len(self.temp_name) >= 1:
            self.players[self.active_player] = self.temp_name
            if self.active_player == self.num_of_players:
                self.can_start_game = True
            else:
                self.active_player += 1
            self.temp_name = ''
        if char_id == 8 and len(self.temp_name) >= 1:
            self.temp_name = self.temp_name[:-1]
        if not self.can_start_game and char_id in list(range(97, 123)) and len(self.temp_name) <= 20:
            self.temp_name += chr(char_id)

    def go_to_game_view(self, game_view):
        game_view.change_view('game_board_view')
        return "start_game"

    def go_to_start_view(self, game_view):
        self.players = dict.fromkeys([1, 2, 3, 4], '')
        self.can_start_game = False
        self.active_player = 1
        game_view.change_view('start_view')
