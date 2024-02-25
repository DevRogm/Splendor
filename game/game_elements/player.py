from dataclasses import dataclass, field
from game.game_elements.stone_markers import StoneMarker


@dataclass
class PlayerInventory:
    markers: dict[str, int] = field(
        default_factory=lambda: {'emerald': 0, 'sapphire': 0, 'ruby': 0, 'diamond': 0, 'onyx': 0, 'gold': 0})
    stone_cards: dict[str, list] = field(
        default_factory=lambda: {'emerald': [], 'sapphire': [], 'ruby': [], 'diamond': [], 'onyx': [], 'gold': []})
    aristocratic_cards: list = field(default_factory=lambda: [])

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

    def check_number_markers(self) -> int:
        """
        The method checks number of markers
        :return: Number of markers
        """
        return sum(self.markers.values())


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
        The method takes marker object from the table.
        Calls the add_marker method and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.add_marker(marker.stone)

    def return_markers(self, marker: StoneMarker) -> None:
        """
        The method return marker from players inventory.
        Calls the return_marker method and pass the name of the stone as a string
        :param marker: Marker object
        :return: None
        """
        self.inventory.remove_marker(marker.stone)

    def reserve_card(self):
        pass

    def buy_card(self):
        pass
