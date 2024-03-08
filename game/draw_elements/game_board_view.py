from dataclasses import dataclass, field
from game.utils import element_detection, draw_player_area, draw_simple_text, draw_requirements, draw_image, get_img
from game_data.markes_and_cards_data import markers
from game.game_elements.game_board import GameBoard


@dataclass
class GameBoardView(GameBoard):
    active_view_elements: dict = field(default_factory=lambda: {})
    player_areas: dict = field(default_factory=lambda: {})

    def draw(self, screen) -> None:
        # Player Area
        for player in range(1, self.players.__len__() + 1):
            self.player_areas.setdefault(player,
                                         draw_player_area(screen, player, self.players.__len__(), self.player_areas))

        # Draw Markers
        for marker in enumerate(markers):
            img_name = f"{marker[1]['stone']}.png"
            action_name = f"take_{marker[1]['stone']}_marker"
            img = get_img(img_name)
            draw_image(self, screen, img, factor_pos_x=0.57 + (0.07 * marker[0]), factor_pos_y=0.85,
                       action_name=action_name)

        # Draw Marker Quantities
        for count, (element_key, element_values) in enumerate(self.active_view_elements.items()):
            if "marker" in element_key:
                marker_name = element_key.split("_")[1]
                quantity = str(self.stone_markers.markers[marker_name].quantity)
                draw_simple_text(screen, quantity, factor_pos_x=0.57 + (0.07 * count), factor_pos_y=0.78, font_size=20,
                                 color=(227, 206, 0))

        # Draw Reverse Cards
        for lvl_card in range(3, 0, -1):
            img_name = f"{lvl_card}_lvl_cards.png"
            img = get_img(img_name)
            draw_image(self, screen, img, factor_pos_x=0.57, factor_pos_y=0.85 - (lvl_card * 0.2))

        # Draw Stone Cards
        for column, cards_lvl in enumerate(['cards_lvl_1', 'cards_lvl_2', 'cards_lvl_3']):
            cards = self.stone_cards.__getattribute__(cards_lvl)
            for row, (card_key, card_val) in enumerate(cards.items()):
                if card_key != 'inverted_stack':
                    # Draw main card
                    card_img = get_img(card_val.img)
                    draw_image(self, screen, card_img, factor_pos_x=0.57 + (row * 0.087),
                               factor_pos_y=0.65 - (column * 0.2))
                    # Draw gem
                    gem_name = card_val.bonus + "_gem.png"
                    gem_img = get_img(gem_name)
                    draw_image(self, screen, gem_img, factor_pos_x=0.59 + (row * 0.087),
                               factor_pos_y=0.59 - (column * 0.2))

                    # Draw requirements
                    for req_count, (stone_name, quantity) in enumerate(card_val.requirements.items()):
                        # print(req_count, stone_name, quantity)
                        draw_requirements(screen, stone_name, quantity, factor_pos_x=0.545 + (row * 0.087),
                                          factor_pos_y=0.718 - (column * 0.2) - (req_count * 0.03),
                                          stone_requirements=True)

                    # Draw card bonus
                    if card_val.points:
                        draw_simple_text(screen, str(card_val.points), factor_pos_x=0.545 + (row * 0.087),
                                         factor_pos_y=0.59 - (column * 0.2), font_size=30)

        # # Draw Aristo Cards
        for column, aristo_card in enumerate(self.aristocratic_cards.cards):
            aristo_img = get_img(aristo_card['img'])
            draw_image(self, screen, aristo_img, factor_pos_x=0.57 + (column * 0.087),
                       factor_pos_y=0.08)
            print(aristo_card)
            for row, (card_name, quantity) in enumerate(aristo_card['requirements'].items()):
                draw_requirements(screen, card_name, quantity, factor_pos_x=0.545 + (column * 0.087),
                                  factor_pos_y=0.12 - (row * 0.03),
                                  cards_requirements=True)
        #
        # # Draw Players Area

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values):
                if "marker" in element_key:
                    self.take_marker(element_key)
                else:
                    self.__getattribute__(element_key)(game_view)

    def take_marker(self, marker_name):
        marker = marker_name.split("_")[1]
        self.stone_markers.remove_marker(marker)
