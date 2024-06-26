import random
from dataclasses import dataclass, field
from typing import List, ClassVar, Union, Literal
from game.game_elements.player import Player
from game.game_elements.stone_markers import StoneMarker
from game.game_elements.stone_cards import StoneCard
from game_data.markes_and_cards_data import markers as markers_data, aristocratic_cards, cards_lvl_1, cards_lvl_2, \
    cards_lvl_3
from game.utils import ExitLoop


@dataclass
class StoneMarkersInventory:
    markers_quantity_options: ClassVar = {
        2: 4,  # 2 players: 4 markers
        3: 5,  # 3 players: 5 markers
        4: 7,  # 4 players: 7 markers
    }
    markers: dict = field(default_factory=lambda: {})

    def add_marker(self, marker: str, ply_num: int) -> None:
        """
        The method increases the stone number by 1 based on the received stone
        :param marker: Name of stone
        :param ply_num: Num of players
        :return: None
        """
        if self.markers[marker].stone == 'gold' and self.markers[marker].quantity < 5:
            self.markers[marker].quantity += 1
        else:
            if self.markers[marker].quantity < self.markers_quantity_options[ply_num]:
                self.markers[marker].quantity += 1

    def remove_marker(self, marker: str) -> None:
        """
        The method reduces the stone number by 1 based on the received stone
        :param marker: Name of stone
        :return: None
        """
        if self.markers[marker].quantity > 0:
            self.markers[marker].quantity -= 1

    def check_number_markers(self):
        pass


@dataclass
class AristocraticCardsInventory:
    cards: list = field(default_factory=lambda: [])

    def remove_card(self):
        pass

    def can_give_card(self, player_cards):
        for aristo_card in self.cards:
            try:
                for stone, requirements in aristo_card['requirements'].items():
                    if len(player_cards[stone]) < requirements:
                        raise ExitLoop
                idx = self.cards.index(aristo_card)
                self.cards.pop(idx)
                return True
            except ExitLoop:
                continue
        return None


@dataclass
class StoneCardsInventory:
    cards_lvl_1: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})
    cards_lvl_2: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})
    cards_lvl_3: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})

    def remove_card(self, lvl, card):
        card_to_return = self.__getattribute__(lvl).copy()
        self.__getattribute__(lvl)[card] = None
        return card_to_return[card]

    def lay_out_cards(self) -> None:
        """
        The method places cards on the table from the stack
        :return: None
        """
        for attribute in vars(self):
            cards_lvl = self.__getattribute__(attribute)
            for card in cards_lvl.keys():
                if card.startswith('card') and not cards_lvl[card] and cards_lvl['inverted_stack']:
                    cards_lvl[card] = cards_lvl['inverted_stack'].pop(0)

    def return_card_obj(self, lvl, card):
        return self.__getattribute__(lvl)[card]


@dataclass
class GameBoard:
    players: List[Player] = field(default_factory=lambda: [])
    stone_markers: StoneMarkersInventory = StoneMarkersInventory()
    aristocratic_cards: AristocraticCardsInventory = AristocraticCardsInventory()
    stone_cards: StoneCardsInventory = StoneCardsInventory()
    active_player: Player | None = None
    active_action: str | None = None
    temp_markers: list[StoneMarker] = field(default_factory=lambda: [])
    show_results: bool = False

    def game_preparation(self, ply: dict, action) -> None:
        """
        The method prepares the game based on the given number of players.
        Calls the methods responsible for adding players, setup stone markers, aristocratic and stones cards
        :param ply:
        :param action:
        :return: None
        """
        if action != 'play_again':
            self.add_players(ply)
        if len(ply) in [2, 3, 4]:
            self.prepare_stone_markers()
            self.prepare_aristocratic_cards()
            self.prepare_stone_cards()
        self.active_player = self.players[0]

    def add_players(self, players: dict) -> None:
        """
        The method that adds players to the game based on the number of players.
        :param players:
        :return: None
        """
        if 2 <= len(players) <= 4:
            for player_name in players.values():
                player = Player(name=player_name)
                self.players.append(player)
        else:
            raise ValueError("Wrong number of players")

    def prepare_stone_markers(self) -> None:
        """
        The method prepares stone markers based on number of players
        :return:
        """
        num_of_markers = self.stone_markers.markers_quantity_options[len(self.players)]
        for marker in markers_data:
            if not marker['stone'] == 'gold':
                self.stone_markers.markers[marker['stone']] = StoneMarker(**marker, quantity=num_of_markers)
            else:
                self.stone_markers.markers[marker['stone']] = StoneMarker(**marker, quantity=5)

    def prepare_stone_cards(self) -> None:
        """
        The method prepares the stone cards, shuffles the cards at all levels, creates stacks of cards and arranges
        the cards on the table
        :return:
        """
        cards_l1 = cards_lvl_1.copy()
        cards_l2 = cards_lvl_2.copy()
        cards_l3 = cards_lvl_3.copy()
        random.shuffle(cards_l1)
        random.shuffle(cards_l2)
        random.shuffle(cards_l3)

        self.stone_cards.cards_lvl_1['inverted_stack'] = [StoneCard(**card_lvl_1) for card_lvl_1 in cards_l1]
        self.stone_cards.cards_lvl_2['inverted_stack'] = [StoneCard(**card_lvl_2) for card_lvl_2 in cards_l2]
        self.stone_cards.cards_lvl_3['inverted_stack'] = [StoneCard(**card_lvl_3) for card_lvl_3 in cards_l3]

        self.stone_cards.lay_out_cards()

    def prepare_aristocratic_cards(self) -> None:
        """
        The method prepares aristocratic cards based on number of players
        :return: None
        """
        num_of_cards = len(self.players) + 1
        random.shuffle(aristocratic_cards)
        self.aristocratic_cards.cards = aristocratic_cards[:num_of_cards]

    def change_active_player(self):
        player_idx = self.players.index(self.active_player)
        self.active_player.check_points()
        if player_idx + 1 >= len(self.players):
            player_idx = 0
        else:
            player_idx += 1
        self.active_player = self.players[player_idx]

    def is_the_last_round(self, players):
        last_round = False
        for player in players:
            if player.points >= 15:
                last_round = True
        return last_round
