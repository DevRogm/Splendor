from dataclasses import dataclass, field
from game.utils import draw_el_and_save_their_edges, element_detection


@dataclass
class GameMenuView:
    view_elements: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path):
        # Prepare Game Menu title and display
        draw_el_and_save_their_edges(self, screen, images_path, "add_players.png", pos_y=300)

        # Select number of players - display
        draw_el_and_save_their_edges(self, screen, images_path, "select_num_of_players.png", pos_y=200)

        # Select 2 players
        draw_el_and_save_their_edges(self, screen, images_path, "2_players.png", pos_y=100, pos_x=200,
                                     element_name="select_2_players")
        # Select 3 players
        draw_el_and_save_their_edges(self, screen, images_path, "3_players.png", pos_y=100,
                                     element_name="select_3_players")
        # Select 4 players
        draw_el_and_save_their_edges(self, screen, images_path, "4_players.png", pos_y=100, pos_x=-200,
                                     element_name="select_4_players")

        # Enter player names - display
        draw_el_and_save_their_edges(self, screen, images_path, "enter_player_names.png", pos_y=0)

        # Back to previous view
        draw_el_and_save_their_edges(self, screen, images_path, "back.png", pos_x=-550, pos_y=-300,
                                     element_name='go_to_start_view')

    def action(self, game_view):
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values) and 'go_to' in element_key:
                return self.__getattribute__(element_key)(game_view)
            elif element_detection(element_values):
                return self.__getattribute__(element_key)()

    def select_2_players(self):
        print("Select 2 players")

    def select_3_players(self):
        print("Select 3 players")

    def select_4_players(self):
        print("Select 4 players")

    def go_to_start_view(self, game_view):
        game_view.change_view('start_view')
