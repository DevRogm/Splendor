from dataclasses import dataclass, field
from game.utils import element_detection, draw_simple_text, draw_requirements, draw_image, get_img
from game_data.markes_and_cards_data import markers
from game.game_elements.game_board import GameBoard


@dataclass
class GameBoardView(GameBoard):
    active_view_elements: dict = field(default_factory=lambda: {})
    player_areas: dict = field(default_factory=lambda: {})

    def draw(self, screen) -> None:
        # Draw Markers
        for marker in enumerate(markers):
            img_name = f"{marker[1]['stone']}.png"
            if marker[1]['stone'] == 'gold':
                action_name = None
            else:
                action_name = f"take_{marker[1]['stone']}_marker"
            img = get_img(img_name)
            draw_image(self, screen, img, factor_pos_x=0.6 + (0.07 * marker[0]), factor_pos_y=0.85,
                       action_name=action_name)

        # Draw Marker Quantities
        for count, (element_key, element_values) in enumerate(self.stone_markers.markers.items()):
            quantity = str(self.stone_markers.markers[element_key].quantity)
            draw_simple_text(screen, quantity, factor_pos_x=0.6 + (0.07 * count), factor_pos_y=0.78, font_size=20,
                             color=(227, 206, 0))

        # Draw Reverse Cards
        for lvl_card in range(3, 0, -1):
            img_name = f"{lvl_card}_lvl_cards.png"
            img = get_img(img_name)
            draw_image(self, screen, img, factor_pos_x=0.6, factor_pos_y=0.85 - (lvl_card * 0.2))

        # Draw Stone Cards
        for column, cards_lvl in enumerate(['cards_lvl_1', 'cards_lvl_2', 'cards_lvl_3']):
            cards = self.stone_cards.__getattribute__(cards_lvl)
            for row, (card_key, card_val) in enumerate(cards.items()):
                if card_key != 'inverted_stack':
                    # Draw main card
                    if card_val:
                        stone_card_action = f"{cards_lvl}__{card_key}"
                        card_img = get_img(card_val.img)

                        draw_image(self, screen, card_img, factor_pos_x=0.6 + (row * 0.087),
                                   factor_pos_y=0.65 - (column * 0.2), action_name=stone_card_action)

                        # Draw gem
                        gem_name = card_val.bonus + "_gem.png"
                        gem_img = get_img(gem_name)
                        draw_image(self, screen, gem_img, factor_pos_x=0.62 + (row * 0.087),
                                   factor_pos_y=0.59 - (column * 0.2))

                        # Draw requirements
                        for req_count, (stone_name, quantity) in enumerate(card_val.requirements.items()):
                            draw_requirements(screen, stone_name, quantity, factor_pos_x=0.575 + (row * 0.087),
                                              factor_pos_y=0.718 - (column * 0.2) - (req_count * 0.03),
                                              stone_requirements=True)

                        # Draw card bonus
                        if card_val.points:
                            draw_simple_text(screen, str(card_val.points), factor_pos_x=0.575 + (row * 0.087),
                                             factor_pos_y=0.58 - (column * 0.2), font_size=36, font_name="Gargi")
                    else:
                        card_img = get_img("shadow_card.png")
                        draw_image(self, screen, card_img, factor_pos_x=0.6 + (row * 0.087),
                                   factor_pos_y=0.65 - (column * 0.2))
        # Draw Aristo Cards
        for column, aristo_card in enumerate(self.aristocratic_cards.cards):
            aristo_img = get_img(aristo_card['img'])
            draw_image(self, screen, aristo_img, factor_pos_x=0.6 + (column * 0.087),
                       factor_pos_y=0.08)
            for row, (card_name, quantity) in enumerate(aristo_card['requirements'].items()):
                draw_requirements(screen, card_name, quantity, factor_pos_x=0.575 + (column * 0.087),
                                  factor_pos_y=0.12 - (row * 0.03),
                                  cards_requirements=True)
        # Draw Action
        take_3_img = get_img("take_3_markers_active.png") if self.active_action == "take_3" else get_img(
            "take_3_markers.png")
        draw_image(self, screen, take_3_img, factor_pos_x=0.63, factor_pos_y=0.95, action_name="take_3")

        take_2_img = get_img("take_2_markers_active.png") if self.active_action == "take_2" else get_img(
            "take_2_markers.png")
        draw_image(self, screen, take_2_img, factor_pos_x=0.73, factor_pos_y=0.95, action_name="take_2")

        buy_card_img = get_img("buy_card_active.png") if self.active_action == "buy_card" else get_img(
            "buy_card.png")
        draw_image(self, screen, buy_card_img, factor_pos_x=0.83, factor_pos_y=0.95, action_name="buy_card_action")

        reserve_card_img = get_img("reserve_card_active.png") if self.active_action == "reserve_card" else get_img(
            "reserve_card.png")
        draw_image(self, screen, reserve_card_img, factor_pos_x=0.93, factor_pos_y=0.95,
                   action_name="reserve_card_action")

        # Draw Players Area
        for count, player in enumerate(self.players):
            # Draw Name
            if count <= 1:
                offset_x = (0.25 * count)
                offset_y = 0
            else:
                offset_x = (0.25 * count - 0.5)
                offset_y = 0.5

            if player.name == self.active_player.name:
                color = (227, 206, 0)
            else:
                color = (255, 255, 255)
            draw_simple_text(screen, player.name, factor_pos_x=0.04 + offset_x,
                             factor_pos_y=0.03 + offset_y, font_size=24, color=color)

            # Draw Cards and Markers
            for column, card_markers in enumerate(markers):
                if card_markers['stone'] != "gold" and len(player.inventory.stone_cards[card_markers['stone']]) > 0:
                    card_img = get_img(f"player_{card_markers['stone']}_card.png")
                    draw_image(self, screen, card_img, factor_pos_x=0.035 + offset_x + (column * 0.045),
                               factor_pos_y=0.14 + offset_y)
                    draw_simple_text(screen, "x" + str(len(player.inventory.stone_cards[card_markers['stone']])),
                                     factor_pos_x=0.035 + offset_x + (column * 0.045),
                                     factor_pos_y=0.2 + offset_y, font_size=16, color=(255, 255, 255))
                if card_markers['stone'] != "gold" and player.inventory.markers[card_markers['stone']].quantity > 0:
                    marker_img = get_img(f"{card_markers['stone']}_player.png")
                    draw_image(self, screen, marker_img, factor_pos_x=0.035 + offset_x + (column * 0.045),
                               factor_pos_y=0.25 + offset_y,
                               action_name=f"{player.name}_return_{card_markers['stone']}_marker")
                    draw_simple_text(screen, "x" + str(player.inventory.markers[card_markers['stone']].quantity),
                                     factor_pos_x=0.035 + offset_x + (column * 0.045),
                                     factor_pos_y=0.29 + offset_y, font_size=16, color=(255, 255, 255))
                elif card_markers['stone'] == "gold" and player.inventory.markers[card_markers['stone']].quantity > 0:
                    marker_img = get_img(f"{card_markers['stone']}_player.png")
                    draw_image(self, screen, marker_img, factor_pos_x=0.215 + offset_x,
                               factor_pos_y=0.045 + offset_y, action_name=f"{player.name}_return_gold_marker")
                    draw_simple_text(screen, "x" + str(player.inventory.markers[card_markers['stone']].quantity),
                                     factor_pos_x=0.19 + offset_x,
                                     factor_pos_y=0.045 + offset_y, font_size=16, color=(255, 255, 255))

            # Draw Reserved Cards
            for reserved_count, (reserved_card_num, reserved_card) in enumerate(
                    player.inventory.reserved_cards.items()):
                if reserved_card is None:
                    shadow_img = get_img("shadow_card.png")
                    draw_image(self, screen, shadow_img, factor_pos_x=0.05 + (reserved_count * 0.0765) + offset_x,
                               factor_pos_y=0.4 + offset_y)
                else:
                    card_img = get_img(reserved_card.img)
                    draw_image(self, screen, card_img, factor_pos_x=0.05 + (reserved_count * 0.0765) + offset_x,
                               factor_pos_y=0.4 + offset_y,
                               action_name=f"{player.name}_reserved_card_{reserved_count}")

                    # Gems
                    gem_name = reserved_card.bonus + "_gem.png"
                    gem_img = get_img(gem_name)
                    draw_image(self, screen, gem_img, factor_pos_x=0.07 + (reserved_count * 0.0765) + offset_x,
                               factor_pos_y=0.34 + offset_y)

                    # Draw requirements
                    for req_count, (stone_name, quantity) in enumerate(reserved_card.requirements.items()):
                        draw_requirements(screen, stone_name, quantity,
                                          factor_pos_x=0.025 + (reserved_count * 0.0765) + offset_x,
                                          factor_pos_y=0.468 - (req_count * 0.03) + offset_y,
                                          stone_requirements=True)

                    # Draw card bonus
                    if reserved_card.points:
                        draw_simple_text(screen, str(reserved_card.points),
                                         factor_pos_x=0.025 + (reserved_count * 0.0765) + offset_x,
                                         factor_pos_y=0.33 + offset_y, font_size=36, font_name="Gargi")

            # Display Points
            draw_simple_text(screen, "Score: " + str(player.points), factor_pos_x=0.04 + offset_x,
                             factor_pos_y=0.055 + offset_y, font_size=14, color=(255, 255, 255))

            # Draw Aristocratic Cards
            if player.inventory.aristocratic_cards:
                crown_img = get_img("crown.png")
                draw_image(self, screen, crown_img, factor_pos_x=0.16 + offset_x,
                           factor_pos_y=0.043 + offset_y)
                draw_simple_text(screen, "x" + str(player.inventory.aristocratic_cards),
                                 factor_pos_x=0.13 + offset_x,
                                 factor_pos_y=0.045 + offset_y, font_size=16, color=(255, 255, 255))

    def action(self, game_view) -> None:
        """
        A method that calls another method with an action on the found element
        :param game_view: Instance of GameView
        :return: None
        """
        for element_key, element_values in self.active_view_elements.items():
            if element_detection(element_values) and not self.active_action == "return_markers":
                if "marker" in element_key:
                    self.take_marker(element_key)
                elif "cards_lvl" in element_key and self.active_action == "buy_card":
                    self.buy_card(element_key)
                elif "cards_lvl" in element_key and self.active_action == "reserve_card":
                    self.reserve_card(element_key)
                elif f"{self.active_player.name}_reserved_card" in element_key and self.active_action == "buy_card":
                    self.buy_reserved_card(element_key)
                else:
                    try:
                        self.__getattribute__(element_key)()
                    except AttributeError:
                        pass
            elif element_detection(element_values) and self.active_action == "return_markers":
                if f"{self.active_player.name}_return_" in element_key:
                    marker_name = element_key.split("_")[2]
                    self.return_marker(marker_name)

    def take_marker(self, marker_name):
        marker = marker_name.split("_")[1]
        if self.active_action == 'take_3' and marker not in self.temp_markers and len(self.temp_markers) < 3 and \
                self.stone_markers.markers[marker].quantity > 0:
            self.temp_markers.append(marker)
            self.stone_markers.remove_marker(marker)
            if len(self.temp_markers) == 3:
                self.can_finish_turn()
        elif self.active_action == 'take_2' and len(self.temp_markers) < 2 and (
                not self.temp_markers or marker in self.temp_markers):
            if self.stone_markers.markers[marker].quantity >= 4 or (
                    self.stone_markers.markers[marker].quantity >= 3 and self.temp_markers):
                self.temp_markers.append(marker)
                self.stone_markers.remove_marker(marker)
                if len(self.temp_markers) == 2:
                    self.can_finish_turn()

    def return_marker(self, marker_name):
        self.active_player.return_markers(marker_name)
        self.stone_markers.add_marker(marker_name, ply_num=len(self.players))
        self.can_finish_turn()

    # CHOOSE ACTION
    def take_3(self):
        if self.temp_markers:
            [self.stone_markers.add_marker(marker, len(self.players)) for marker in self.temp_markers]
        self.temp_markers = []
        self.active_action = 'take_3'

    def take_2(self):
        if self.temp_markers:
            [self.stone_markers.add_marker(marker, len(self.players)) for marker in self.temp_markers]
        self.temp_markers = []
        self.active_action = 'take_2'

    def buy_card_action(self):
        self.active_action = 'buy_card'

    def reserve_card_action(self):
        self.active_action = 'reserve_card'

    def buy_card(self, card):
        lvl, num = card.split("__")
        card_obj = self.stone_cards.return_card_obj(lvl, num)
        can_buy, marker_to_return = self.active_player.can_buy(card_obj)
        if can_buy:
            removed_card_from_table = self.stone_cards.remove_card(lvl, num)
            self.active_player.buy_card(removed_card_from_table, marker_to_return)
            if marker_to_return:
                for marker_name, quantity in marker_to_return.items():
                    [self.stone_markers.add_marker(marker_name, len(self.players)) for _ in range(quantity)]
            self.stone_cards.lay_out_cards()
            self.can_finish_turn()

    def buy_reserved_card(self, card):
        card_obj = self.active_player.inventory.reserved_cards.get(int(card.split('_')[3]) + 1)
        can_buy, marker_to_return = self.active_player.can_buy(card_obj)
        if can_buy:
            self.active_player.buy_card(card_obj, marker_to_return)
            self.active_player.inventory.reserved_cards[int(card.split('_')[3]) + 1] = None
            if marker_to_return:
                for marker_name, quantity in marker_to_return.items():
                    [self.stone_markers.add_marker(marker_name, len(self.players)) for _ in range(quantity)]
            self.stone_cards.lay_out_cards()
            self.can_finish_turn()

    def reserve_card(self, card):
        lvl, num = card.split("__")
        card_obj = self.stone_cards.return_card_obj(lvl, num)
        if None in list(self.active_player.inventory.reserved_cards.values()):
            self.active_player.reserve_card(card_obj)
            self.stone_cards.remove_card(lvl, num)
            if self.stone_markers.markers['gold'].quantity > 0:
                self.stone_markers.remove_marker('gold')
                self.active_player.take_markers('gold')
            self.stone_cards.lay_out_cards()
            self.can_finish_turn()
            # dodac znacznik golda graczowi o ile taki znacznik jeszcze jest na stol

    def can_finish_turn(self):
        for marker in self.temp_markers:
            self.active_player.take_markers(marker)
        self.temp_markers = []
        self.active_action = None
        if self.active_player.inventory.check_number_markers() > 10:
            self.active_action = "return_markers"
        else:
            self.active_action = None
            self.change_active_player()
        # autocomplete card
        # reset all temps
        # reset active action
        # check all player markers
        # wait for return markers if more than 10
        # check all player markers
        # check can take aristo card
        # change player
