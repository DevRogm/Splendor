from dataclasses import dataclass, field
from typing import List
from player import Player


@dataclass
class GameBoard:
    players: List[Player]
    markers: dict[str, int] = field(
        default_factory=lambda: {'emerald': 0, 'sapphire': 0, 'ruby': 0, 'diamond': 0, 'onyx': 0, 'gold': 0})
    aristocratic_cards: list = field(default_factory=lambda: [])
    stone_cards_lvl_1: dict[str, list] = field(
        default_factory=lambda: {'inverted_stack': [], 'stack_1': [], 'stack_2': [], 'stack_3': [], 'stack_4': []})
    stone_cards_lvl_2: dict[str, list] = field(
        default_factory=lambda: {'inverted_stack': [], 'stack_1': [], 'stack_2': [], 'stack_3': [], 'stack_4': []})
    stone_cards_lvl_3: dict[str, list] = field(
        default_factory=lambda: {'inverted_stack': [], 'stack_1': [], 'stack_2': [], 'stack_3': [], 'stack_4': []})


