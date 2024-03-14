import operator
from dataclasses import dataclass
from game.utils import get_img, draw_image, draw_simple_text


@dataclass
class ResultsView:
    players = None

    def draw(self, screen):
        splendor_img = get_img("game_results.png")
        draw_image(self, screen, splendor_img, factor_pos_x=0.5, factor_pos_y=0.2)
        self.print_results(screen)

    def print_results(self, screen):
        sorted_players = sorted(self.players, key=operator.attrgetter('points'), reverse=True)
        text = f"Lp. NAME POINTS NUM OF CARDS NUM OF ARISTO"
        draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.3, color=(227, 206, 0), font_size=30)
        for count, player in enumerate(sorted_players, start=1):
            text = f"{count} {player.name} {player.points} {self.count_cards(player)} {player.inventory.aristocratic_cards}"
            draw_simple_text(screen, text, factor_pos_x=0.5, factor_pos_y=0.3 + (count * 0.08), color=(227, 206, 0),
                             font_size=30)

    def count_cards(self, player):
        num_of_cards = sum([len(stone_cards) for stone_cards in player.inventory.stone_cards.values()])
        return num_of_cards

    def action(self, game_view):
        pass
