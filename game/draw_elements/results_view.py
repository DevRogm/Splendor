from dataclasses import dataclass
from game.utils import get_img, draw_image


@dataclass
class ResultsView:
    pass

    def draw(self, screen):
        splendor_img = get_img("game_results.png")
        draw_image(self, screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)

    def action(self, game_view):
        pass