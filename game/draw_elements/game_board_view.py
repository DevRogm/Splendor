from dataclasses import dataclass


@dataclass
class GameBoardView:
    pass

    def draw(self):
        print(self)