from dataclasses import dataclass
from typing import Literal


@dataclass
class StoneMarker:
    stone: str
    joker: bool = False
    img: str = ''
    quantity: int = 0
