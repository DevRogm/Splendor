from dataclasses import dataclass, field
from game.utils import element_detection, draw_game_area, draw_player_area, draw_simple_text, \
    draw_marker_quantities, draw_stone_requirements, draw_card_requirements, draw_image, get_img
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
                draw_simple_text(screen, quantity, factor_pos_x=0.57 + (0.07 * count), factor_pos_y=0.78, font_size=20)

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

            #         # Draw requirements
            #         # print("----------------")
            #         n = 0
            #         for stone_name, quantity in card_val.requirements.items():
            #             # print(stone_name, quantity)
            #             draw_stone_requirements(self, screen, stone_name, quantity, pos_x=cards_pos[0] + 30,
            #                                     pos_y=cards_pos[1] - 45 + 23 * n)
            #             n += 1

        # # Draw Aristo Cards
        # n = 0
        # for aristo_card in self.game_board.aristocratic_cards.cards:
        #     cards_pos = - screen.get_width() / 10.5, screen.get_height() / 2.5
        #     draw_elements(self, screen, images_path, aristo_card['img'], pos_x=cards_pos[0] + n * -100,
        #                   pos_y=cards_pos[1])
        #     m = 0
        #     for card_name, quantity in aristo_card['requirements'].items():
        #         # print(stone_name, quantity)
        #         draw_card_requirements(self, screen, card_name, quantity, pos_x=cards_pos[0] + 40 - n * 100,
        #                                pos_y=cards_pos[1] - 19 + m * 20)
        #         m += 1
        #     n += 1
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
