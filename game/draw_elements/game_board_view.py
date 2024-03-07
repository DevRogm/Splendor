from dataclasses import dataclass, field
from game.utils import draw_elements, element_detection, draw_game_area, draw_player_area, draw_simple_text, \
    draw_marker_quantities, draw_stone_requirements
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
            pos_y = -screen.get_height() / 2.8
            pos_x = - screen.get_width() * 0.05 - (100 * marker[0])
            img_name = f"{marker[1]['stone']}.png"
            element_name = f"take_{marker[1]['stone']}_marker"
            draw_elements(self, screen, images_path, img_name, pos_x=pos_x, pos_y=pos_y,
                          element_name=element_name)

        # Draw Marker Quantities
        for element_key, element_values in self.view_elements.items():
            if "marker" in element_key:
                marker_name = element_key.split("_")[1]
                quantity = str(self.game_board.stone_markers.markers[marker_name].quantity)
                pos_x = (element_values[0][0] + element_values[1][0]) / 2.01
                pos_y = (element_values[0][1] + element_values[1][1]) / 2.2
                draw_marker_quantities(screen, quantity, pos_x=pos_x, pos_y=pos_y)

        # Draw Reverse Cards
        for lvl_card in range(3, 0, -1):
            img_name = f"{lvl_card}_lvl_cards.png"
            cards_pos = - screen.get_width() * 0.055, -260 + lvl_card * 140
            draw_elements(self, screen, images_path, img_name, pos_x=cards_pos[0], pos_y=cards_pos[1])

        # Draw Stone Cards
        for cards_lvl in ['cards_lvl_1', 'cards_lvl_2', 'cards_lvl_3']:
            cards = self.game_board.stone_cards.__getattribute__(cards_lvl)
            for card_key, card_val in cards.items():
                if card_key != 'inverted_stack':
                    cards_pos = 20 - screen.get_width() * 0.1 - (int(card_key.split("_")[1]) * 0.8 * 140), -260 - (
                            -int(cards_lvl.split("_")[2]) * 140)
                    # Draw main card
                    draw_elements(self, screen, images_path, card_val.img, pos_x=cards_pos[0], pos_y=cards_pos[1])
                    # Draw gem
                    draw_elements(self, screen, images_path, card_val.bonus + "_gem.png", pos_x=cards_pos[0] - 30,
                                  pos_y=cards_pos[1] + 45)
                    # Draw requirements
                    # print("----------------")
                    n = 0
                    for stone_name, quantity in card_val.requirements.items():
                        # print(stone_name, quantity)
                        draw_stone_requirements(self, screen, stone_name, quantity, pos_x=cards_pos[0] + 30,
                                                pos_y=cards_pos[1] - 45 + 23 * n)
                        n += 1

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.view_elements.items():
            if element_detection(element_values):
                if "marker" in element_key:
                    self.take_marker(element_key)
                else:
                    self.__getattribute__(element_key)(game_view)

    def take_marker(self, marker_name):
        marker = marker_name.split("_")[1]
        self.game_board.stone_markers.remove_marker(marker)
