from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    points: int = 0
    markers: dict = field(
        default_factory=lambda: {'emerald': 0, 'sapphire': 0, 'ruby': 0, 'diamond': 0, 'onyx': 0, 'gold': 0})
    stone_cards: dict = field(
        default_factory=lambda: {'emerald': [], 'sapphire': [], 'ruby': [], 'diamond': [], 'onyx': [], 'gold': []})
    aristocratic_cards: dict = field(default_factory=lambda: {})

    def __post_init__(self):
        if len(self.name) > 20:
            raise ValueError("Too long name, max. characters is a 20")
