from dataclasses import dataclass


@dataclass
class StatisticsView:
    pass

    def draw(self):
        print(self)