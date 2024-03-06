from dataclasses import dataclass, field
from game.utils import draw_elements, element_detection, draw_game_area, draw_player_area, draw_markers_area
from game_data.markes_and_cards_data import markers
from game.game_elements.game_board import GameBoard

@dataclass
class GameBoardView:
    game_board: GameBoard = None
    view_elements: dict = field(default_factory=lambda: {})
    players_num: int = 4
    game_area = None
    player_areas: dict = field(default_factory=lambda: {})

    def draw(self, screen, images_path) -> None:
        """
        A method that calls other methods which draw some elements and return the edges of those elements
        :param screen: Surface to display elements
        :param images_path: Path of images
        :return: None
        """

        # Game Area
        self.game_area = draw_game_area(screen, self.game_area)

        # Player Area
        for player in range(1, self.players_num + 1):
            self.player_areas.setdefault(player, draw_player_area(screen, player, self.players_num, self.player_areas))

        # Draw Markers
        for marker in enumerate(markers):
            pos_y = -screen.get_height() / 3
            pos_x = - screen.get_width() * 0.05 - (100 * marker[0])
            img_name = f"{marker[1]['stone']}.png"
            element_name = f"take_{marker[1]['stone']}_marker"
            draw_elements(self, screen, images_path, img_name, pos_x=pos_x, pos_y=pos_y,
                          element_name=element_name)

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                if "take_" in element_key:
                    self.take_marker(element_key)
                else:
                    self.__getattribute__(element_key)(game_view)

    def take_marker(self, marker_name):
        marker = marker_name.split("_")[1]
        self.game_board.stone_markers.remove_marker(marker)

