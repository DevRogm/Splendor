import pytest
from game.game_elements.game_board import GameBoard


class TestGameBoard:

    @pytest.fixture
    def game_board(self):
        game_board = GameBoard()
        return game_board

    def test_game_board_init(self, game_board):
        assert game_board

    @pytest.mark.parametrize("players, expected", (
            ({1: "Player_1"}, 0),
            ({1: "Player_1", 2: "Player_2"}, 2),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3"}, 3),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3", 4: "Player_4"}, 4),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3", 4: "Player_4", 5: "Player_5"}, 0),
    ))
    def test_game_preparation_players(self, game_board, players, expected):
        if len(players) in [2, 3, 4]:
            game_board.game_preparation(players)
            assert len(game_board.players) == expected
        else:
            with pytest.raises(ValueError):
                game_board.game_preparation(players)
            assert len(game_board.players) == expected

    @pytest.mark.parametrize("players, expected", (
            ({1: "Player_1", 2: "Player_2"}, 4),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3"}, 5),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3", 4: "Player_4"}, 7),
    ))
    def test_game_preparation_stone_markers(self, game_board, players, expected):
        game_board.game_preparation(players)
        for stone in game_board.stone_markers.markers.values():
            if stone.stone == 'gold':
                assert stone.quantity == 5
            else:
                assert stone.quantity == expected

    @pytest.mark.parametrize("players, expected", (
            ({1: "Player_1", 2: "Player_2"}, 3),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3"}, 4),
            ({1: "Player_1", 2: "Player_2", 3: "Player_3", 4: "Player_4"}, 5),
    ))
    def test_game_preparation_aristocratic_cards(self, game_board, players, expected):
        game_board.game_preparation(players)
        assert len(game_board.aristocratic_cards.cards) == expected

    def test_game_preparation_stone_cards_in_stacks(self, game_board):
        game_board.game_preparation({1: "Player_1", 2: "Player_2", 3: "Player_3", 4: "Player_4"})
        assert len(game_board.stone_cards.cards_lvl_1['inverted_stack']) == 40
        assert len(game_board.stone_cards.cards_lvl_2['inverted_stack']) == 30
        assert len(game_board.stone_cards.cards_lvl_3['inverted_stack']) == 20

    def test_game_preparation_lay_out_stone_cards(self, game_board):
        for attribute in vars(game_board.stone_cards):
            cards_lvl = game_board.stone_cards.__getattribute__(attribute)
            for card in cards_lvl.keys():
                if card.startswith('card'):
                    assert cards_lvl[card]
