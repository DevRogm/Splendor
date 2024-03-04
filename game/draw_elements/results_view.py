from dataclasses import dataclass


@dataclass
class ResultsView:
    pass

    def draw(self):
        print(self)