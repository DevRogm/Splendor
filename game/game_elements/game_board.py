import random
from dataclasses import dataclass, field
from typing import List, ClassVar, Union
from player import Player
from game_data.markes_and_cards_data import aristocratic_cards
from stone_markers import StoneMarker
from stone_cards import StoneCard
from game_data.markes_and_cards_data import markers as markers_data, cards_3_3_4


@dataclass
class StoneMarkersInventory:
    markers_quantity_options: ClassVar = {
        2: 4,  # 2 players: 4 markers
        3: 5,  # 3 players: 5 markers
        4: 7,  # 4 players: 7 markers
    }
    markers: dict = field(default_factory=lambda: {})

    def add_marker(self, marker: str) -> None:
        """
        The method increases the stone number by 1 based on the received stone
        :param marker: Name of stone
        :return: None
        """
        self.markers[marker] += 1

    def remove_marker(self, marker: str) -> None:
        """
        The method reduces the stone number by 1 based on the received stone
        :param marker: Name of stone
        :return: None
        """
        self.markers[marker] -= 1

    def check_number_markers(self):
        pass


@dataclass
class AristocraticCardsInventory:
    cards: list = field(default_factory=lambda: [])

    def remove_card(self):
        pass

    def can_give_card(self):
        pass


@dataclass
class StoneCardsInventory:
    cards_lvl_1: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})
    cards_lvl_2: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})
    cards_lvl_3: dict[str, Union[List[StoneCard], StoneCard, None]] = field(
        default_factory=lambda: {'inverted_stack': [], 'card_1': None, 'card_2': None, 'card_3': None, 'card_4': None})

    def remove_card(self, lvl, stack):
        pass

    def lay_out_card(self):
        pass


@dataclass
class GameBoard:
    players: List[Player] = field(default_factory=lambda: [])
    stone_markers: StoneMarkersInventory = StoneMarkersInventory()
    aristocratic_cards: AristocraticCardsInventory = AristocraticCardsInventory()
    stone_cards: StoneCardsInventory = StoneCardsInventory()

    def game_preparation(self, num_of_player):
        self.add_players(num_of_player)
        self.prepare_stone_markers()
        self.prepare_aristocratic_cards()
        self.prepare_stone_cards()

    def add_players(self, num_of_player):
        for num in range(num_of_player):
            # TO DO: Allow to enter the players name
            # or choose existing players
            player = Player(name=f"Player_{num + 1}")
            self.players.append(player)

    def prepare_stone_markers(self):
        num_of_markers = self.stone_markers.markers_quantity_options[len(self.players)]
        for marker in markers_data:
            if not marker['stone'] == 'gold':
                self.stone_markers.markers[marker['stone']] = StoneMarker(**marker, quantity=num_of_markers)
            else:
                self.stone_markers.markers[marker['stone']] = StoneMarker(**marker, quantity=5)

    def prepare_stone_cards(self):
        pass

    def prepare_aristocratic_cards(self):
        num_of_cards = len(self.players) + 1
        cards = random.choices(aristocratic_cards, k=num_of_cards)
        self.aristocratic_cards.cards = cards

    def whose_turn(self):
        pass

    def check_the_winner(self):
        pass

    def show_available_actions(self):
        pass
