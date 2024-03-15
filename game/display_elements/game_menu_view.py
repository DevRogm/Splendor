from dataclasses import dataclass, field
from game.utils import element_detection, draw_simple_text, draw_image, get_img
from typing import List, Callable, Any


@dataclass
class GameMenuView:
    active_view_elements: dict = field(default_factory=lambda: {})
    num_of_players: int = 2
    temp_name: str = ''
    active_player: int = 1
    players: dict = field(default_factory=lambda: {})
    can_start_game: bool = False

    def draw(self, screen) -> None:
        """
        A method that draws elements on the screen
        :param screen: Surface to display elements
        :return: None
        """
        if not self.can_start_game:
            # Prepare Game Menu title
            add_players_img = get_img("add_players.png")
            draw_image(self, screen, add_players_img, factor_pos_x=0.5, factor_pos_y=0.1)

            # Select number of players - display
            select_num_of_players_img = get_img("select_num_of_players.png")
            draw_image(self, screen, select_num_of_players_img, factor_pos_x=0.5, factor_pos_y=0.3)

            # Select 2 players
            selected_img = get_img("selected.png")
            select_2_players_img = get_img("2_players.png")
            draw_image(self, screen, select_2_players_img, factor_pos_x=0.4, factor_pos_y=0.4,
                       action_name="select_2_players")
            if self.num_of_players == 2:
                draw_image(self, screen, selected_img, factor_pos_x=0.415, factor_pos_y=0.4)

            # Select 3 players
            select_3_players_img = get_img("3_players.png")
            draw_image(self, screen, select_3_players_img, factor_pos_x=0.5, factor_pos_y=0.4,
                       action_name="select_3_players")
            if self.num_of_players == 3:
                draw_image(self, screen, selected_img, factor_pos_x=0.515, factor_pos_y=0.4)

            # Select 4 players
            select_4_players_img = get_img("4_players.png")
            draw_image(self, screen, select_4_players_img, factor_pos_x=0.6, factor_pos_y=0.4,
                       action_name="select_4_players")
            if self.num_of_players == 4:
                draw_image(self, screen, selected_img, factor_pos_x=0.615, factor_pos_y=0.4)

            # Enter player names - display
            enter_player_names_img = get_img("enter_player_names.png")
            draw_image(self, screen, enter_player_names_img, factor_pos_x=0.5, factor_pos_y=0.5)

            # Player Name
            text = f"Player {self.active_player}: {self.temp_name}"
            draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.6, color=(227, 206, 0))

            # Back to previous view button
            back_img = get_img("back.png")
            draw_image(self, screen, back_img, factor_pos_x=0.95, factor_pos_y=0.9, action_name='go_to_start_view')

        else:
            start_game_img = get_img("start_game.png")
            draw_image(self, screen, start_game_img, factor_pos_x=0.5, factor_pos_y=0.8, action_name='go_to_game_view')

            for player_k, player_v in self.players.items():
                if player_v:
                    text = f"Player {player_k}: {player_v}"
                    draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.2 + player_k * 0.1,
                                     color=(227, 206, 0))

    def action(self, game_view) -> Any | None:
        """
        A method that does the action from the active elements
        :param game_view: Surface to display elements
        :return: Any or None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values) and 'select' in element_key:
                num_of_players = int(element_key.split("_")[1])
                return self.select_num_of_players(num_of_players)

    def select_num_of_players(self, num_of_players) -> None:
        """
        A method that selects number of players
        :return: None
        """
        if not self.can_start_game:
            self.num_of_players = num_of_players

    def add_player_name(self, char_id) -> None:
        """
        A method allows to enter the player's name
        :param char_id: id of characters
        :return: None
        """
        # char_id == 13 -> Enter
        if char_id == 13 and len(self.temp_name) >= 1:
            self.players[self.active_player] = self.temp_name
            if self.players.__len__() >= self.num_of_players:
                self.can_start_game = True
            else:
                self.active_player += 1
            self.temp_name = ''
        # char_id == 8 -> Backspace
        elif char_id == 8 and len(self.temp_name) >= 1:
            self.temp_name = self.temp_name[:-1]
        if not self.can_start_game and char_id in list(range(97, 123)) and len(self.temp_name) <= 6:
            self.temp_name += chr(char_id)

    @staticmethod
    def go_to_game_view(game_view) -> str:
        """
        A method that changes the displaying view to main game view and returns string 'start_game
        :param game_view: Surface to display elements
        :return: 'start_game' string
        """
        game_view.change_view('game_board_view')
        return "start_game"

    def go_to_start_view(self, game_view) -> None:
        """
        A method that changes the displaying view to start view and resets entered players
        :param game_view: Surface to display elements
        :return: None
        """
        self.temp_name = ''
        self.players = {}
        self.can_start_game = False
        self.active_player = 1
        game_view.change_view('start_view')
