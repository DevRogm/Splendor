from dataclasses import dataclass
from markes_and_cards_data import aristocratic_cards


@dataclass
class AristocraticCard:
    requirements: dict
    points: int
    img: str
