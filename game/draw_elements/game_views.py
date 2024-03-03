from dataclasses import dataclass
from game.draw_elements.start_view import StartView
from game.draw_elements.statistics_view import StatisticsView
from game.draw_elements.game_menu_view import GameMenuView
from game.draw_elements.game_board_view import GameBoardView
from game.draw_elements.results_view import ResultsView


@dataclass
class GameViews:
    start_view: StartView = StartView()
    game_menu_view: GameMenuView = GameMenuView()
    statistics_view: StatisticsView = StatisticsView()
    game_board_view: GameBoardView = GameBoardView()
    results_view: ResultsView = ResultsView()
    current_view: str = 'start_view'

    def draw_view(self, screen, images_path):
        view = self.__getattribute__(self.current_view)
        view.draw(screen, images_path)

    def change_view(self, new_view):
        self.current_view = new_view

    def do_action(self):
        view = self.__getattribute__(self.current_view)
        return view.action(self)
