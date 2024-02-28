import pytest
from game.game_elements.player import Player
from game.game_elements.game_board import GameBoard
from game.game_elements.stone_markers import StoneMarker
from game_data.markes_and_cards_data import markers


class TestGameBoard:

    @pytest.fixture
    def game_board(self):
        game_board = GameBoard()
        return game_board

    def test_game_board_init(self, game_board):
        assert game_board

    @pytest.mark.parametrize("num_of_players, expected", (
            (1, 0),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 0),
    ))
    def test_game_preparation_players(self, game_board, num_of_players, expected):
        if num_of_players in [2, 3, 4]:
            game_board.game_preparation(num_of_players)
            assert len(game_board.players) == num_of_players
        else:
            with pytest.raises(ValueError):
                game_board.game_preparation(num_of_players)
            assert len(game_board.players) == 0
