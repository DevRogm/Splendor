from dataclasses import dataclass, field
from game.game_elements.stone_markers import StoneMarker
from game.game_elements.aristocratic_cards import AristocraticCard
from game.game_elements.stone_cards import StoneCard
from game_data.markes_and_cards_data import markers as markers_data
from typing import List
from itertools import zip_longest


@dataclass
class PlayerInventory:
    markers: dict = field(default_factory=lambda: {})
    stone_cards: dict[str, List[StoneCard]] = field(
        default_factory=lambda: {'emerald': [], 'sapphire': [], 'ruby': [], 'diamond': [], 'onyx': []})
    aristocratic_cards: int = 0
    reserved_cards: dict[int, StoneCard] = field(default_factory=lambda: {1: None, 2: None, 3: None})

    def check_number_markers(self) -> int:
        """
        The method checks number of markers
        :return: Number of markers
        """
        return sum(stone.quantity for stone in self.markers.values())

    def _stone_markers_init(self) -> None:
        """
        The method sets the initial stone markers with a quantity of 0
        :return: None
        """
        for marker in markers_data:
            self.markers[marker['stone']] = StoneMarker(**marker, quantity=0)

    def __post_init__(self):
        self._stone_markers_init()


@dataclass
class Player:
    name: str
    points: int = 0
    inventory = None

    def __post_init__(self):
        self.__setattr__('inventory', PlayerInventory())
        if len(self.name) > 20:
            raise ValueError("Too long name, max. characters is a 20")

    def take_markers(self, marker: str) -> None:
        """
        The method takes marker from the table.
        Calls the add_marker method from players inventory and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.markers[marker].quantity += 1

    def return_markers(self, marker_name: str, quantity: int) -> None:
        """
        The method removes marker from players inventory.
        Calls the remove_marker method from players inventory and pass the name of the stone as a string
        :param marker_name: Marker object
        :param quantity: Number of marker to return
        :return: None
        """
        self.inventory.markers[marker_name].quantity -= quantity

    def reserve_card(self):
        pass

    def can_buy(self, card):
        temp_markers_to_return = {}
        for stone_name, stone_quantity in card.requirements.items():
            if all_stones_by_type := (len(self.inventory.stone_cards[stone_name]) +
                                      self.inventory.markers[stone_name].quantity >= stone_quantity):
                print("Poszło bez golda")
                print("SUPER")
                if (markers_to_return := stone_quantity - len(self.inventory.stone_cards[stone_name])) > 0:
                    temp_markers_to_return[stone_name] = markers_to_return

            elif all_stones_by_type + self.inventory.markers["gold"].quantity >= stone_quantity:
                print("Poszło z goldem")
                print("SUPER")

            else:
                print("Brak zasobów")
                return False
        print("temp_markers_to_return", temp_markers_to_return)
        return temp_markers_to_return

    def buy_card(self, card, markers_to_return):
        for marker_name, quantity in markers_to_return.items():

            print("DO oddaniam", marker_name, quantity)
            self.return_markers(marker_name, quantity)
            print("Zasoby po oddaniu", self.inventory.markers[marker_name])
        self.inventory.stone_cards[card.bonus].append(card)
