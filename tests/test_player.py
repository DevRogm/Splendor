import pytest
from game.game_elements.player import Player


class TestPlayer:

    @pytest.fixture
    def player(self):
        player = Player(name="Test Name")
        return player

    def test_player_init(self, player):
        assert player

    def test_player_too_long_name(self):
        with pytest.raises(ValueError):
            Player(name="Test tooooo long name")

    def test_player_markers_init(self, player):
        for marker_quantity in player.inventory.markers.values():
            assert marker_quantity == 0

    def test_player_stone_cards_init(self, player):
        for stone_cards_list in player.inventory.stone_cards.values():
            assert stone_cards_list == []

    def test_player_aristocratic_cards_init(self, player):
        assert player.inventory.aristocratic_cards == []
