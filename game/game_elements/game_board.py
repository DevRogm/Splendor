import random
from dataclasses import dataclass, field
from typing import List, ClassVar, Union, Literal
from game.game_elements.player import Player
from game.game_elements.stone_markers import StoneMarker
from game.game_elements.stone_cards import StoneCard
from game_data.markes_and_cards_data import markers as markers_data, aristocratic_cards, cards_lvl_1, cards_lvl_2, \
    cards_lvl_3


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


@dataclass
class GameBoard:
    players: List[Player] = field(default_factory=lambda: [])
    stone_markers: StoneMarkersInventory = StoneMarkersInventory()
    aristocratic_cards: AristocraticCardsInventory = AristocraticCardsInventory()
    stone_cards: StoneCardsInventory = StoneCardsInventory()

    def game_preparation(self, num_of_player: Literal[2, 3, 4]) -> None:
        """
        The method prepares the game based on the given number of players.
        Calls the methods responsible for adding players, setup stone markers, aristocratic and stones cards
        :param num_of_player:
        :return: None
        """
        self.add_players(num_of_player)
        if num_of_player in [2, 3, 4]:
            self.prepare_stone_markers()
            self.prepare_aristocratic_cards()
            self.prepare_stone_cards()

    def add_players(self, num_of_player: Literal[2, 3, 4]) -> None:
        """
        The method that adds players to the game based on the number of players.
        :param num_of_player:
        :return:
        """
        if 2 <= num_of_player <= 4:
            for num in range(num_of_player):
                # TO DO: Allow to enter the players name
                # or choose existing players
                player = Player(name=f"Player_{num + 1}")
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
        random.shuffle(cards_lvl_1)
        random.shuffle(cards_lvl_2)
        random.shuffle(cards_lvl_3)

        self.stone_cards.cards_lvl_1['inverted_stack'] = [StoneCard(**card_lvl_1) for card_lvl_1 in cards_lvl_1]
        self.stone_cards.cards_lvl_2['inverted_stack'] = [StoneCard(**card_lvl_2) for card_lvl_2 in cards_lvl_2]
        self.stone_cards.cards_lvl_3['inverted_stack'] = [StoneCard(**card_lvl_3) for card_lvl_3 in cards_lvl_3]

        self.stone_cards.lay_out_cards()

    def prepare_aristocratic_cards(self) -> None:
        """
        The method prepares aristocratic cards based on number of players
        :return: None
        """
        num_of_cards = len(self.players) + 1
        cards = random.choices(aristocratic_cards, k=num_of_cards)
        self.aristocratic_cards.cards = cards

    def whose_turn(self):
        pass

    def check_the_winner(self):
        pass

    def show_available_actions(self):
        pass
