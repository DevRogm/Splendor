from dataclasses import dataclass
from typing import Literal


@dataclass
class StoneMarker:
    stone: str
    joker: bool = False
    quantity: int = 7

    def __post_init__(self) -> None:
        self.quantity = self.max = 5 if self.joker else self.quantity

    def sub_marker(self, num_of_markers: Literal[1, 2]) -> None:
        if self.quantity > 0 and num_of_markers == 1:
            self.quantity -= 1
        elif self.quantity >= 4 and num_of_markers == 2 and not self.joker:
            self.quantity -= 2

    def add_marker(self, num_of_markers: int) -> None:
        if self.quantity + num_of_markers > self.max:
            raise ValueError(f"Too many markers returned. The maximum number of markers is a {self.max}")
        self.quantity += num_of_markers
