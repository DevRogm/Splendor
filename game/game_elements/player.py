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
    aristocratic_cards: List[AristocraticCard] = field(default_factory=lambda: [])

    def add_marker(self, marker: str) -> None:
        """
        The method increases the stone number by 1 based on the received stone
        :param marker: Name of stone
        :return: None
        """
        self.markers[marker].quantity += 1

    def remove_marker(self, marker: str) -> None:
        """
        The method reduces the stone number by 1 based on the received stone
        :param marker: Name of stone
        :return: None
        """
        self.markers[marker].quantity -= 1

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
    inventory: PlayerInventory = PlayerInventory()
    points: int = 0

    def __post_init__(self):
        if len(self.name) > 20:
            raise ValueError("Too long name, max. characters is a 20")

    def take_markers(self, marker: StoneMarker) -> None:
        """
        The method takes marker from the table.
        Calls the add_marker method from players inventory and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.add_marker(marker.stone)

    def return_markers(self, marker: str) -> None:
        """
        The method removes marker from players inventory.
        Calls the remove_marker method from players inventory and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.remove_marker(marker)

    def reserve_card(self):
        pass

    def buy_card(self):
        pass
