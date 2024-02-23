from dataclasses import dataclass


@dataclass
class AristocraticCard:
    requirements: dict
    points: int
    img: str
