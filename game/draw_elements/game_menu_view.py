from dataclasses import dataclass


@dataclass
class GameMenuView:
    pass

    def draw(self):
        print(self)