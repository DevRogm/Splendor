from dataclasses import dataclass, field
from game.game_elements.stone_markers import StoneMarker
from game.game_elements.aristocratic_cards import AristocraticCard
from game.game_elements.stone_cards import StoneCard
from game_data.markes_and_cards_data import markers as markers_data
from typing import List


@dataclass
class PlayerInventory:
    markers: dict = field(default_factory=lambda: {})
    stone_cards: dict[str, List[StoneCard]] = field(
        default_factory=lambda: {'emerald': [], 'sapphire': [], 'ruby': [], 'diamond': [], 'onyx': [], 'gold': []})
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

    def return_markers(self, marker: str) -> None:
        """
        The method removes marker from players inventory.
        Calls the remove_marker method from players inventory and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.markers[marker].quantity -= 1

    def reserve_card(self):
        pass

    def buy_card(self, card):
        print(self.name, "Kupuje kartę")
        print(card)
        self.inventory.stone_cards[card.bonus].append(card)
