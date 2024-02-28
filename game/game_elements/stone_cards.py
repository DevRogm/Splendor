from dataclasses import dataclass


@dataclass
class StoneCard:
    bonus: str
    lvl: int
    points: int
    requirements: dict
    img: str
