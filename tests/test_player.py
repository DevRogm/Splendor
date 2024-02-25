import pytest
from game.game_elements.player import Player
from game.game_elements.stone_markers import StoneMarker
from game_data.markes_and_cards_data import markers


class TestPlayer:

    @pytest.fixture
    def stone_markers(self):
        stone_markers = [StoneMarker(**stone_marker) for stone_marker in markers]
        return stone_markers

    @pytest.fixture
    def player(self):
        player = Player(name="Test Name")
        return player

    def test_init(self, player):
        assert player

    def test_too_long_name(self):
        with pytest.raises(ValueError):
            Player(name="Test tooooo long name")

    def test_markers_init(self, player):
        for marker_quantity in player.inventory.markers.values():
            assert marker_quantity == 0

    def test_stone_cards_init(self, player):
        for stone_cards_list in player.inventory.stone_cards.values():
            assert stone_cards_list == []

    def test_aristocratic_cards_init(self, player):
        assert player.inventory.aristocratic_cards == []

    def test_add_stone_markers_to_inventory(self, player, stone_markers):
        for stone_marker in stone_markers:
            player.take_markers(stone_marker)
        assert list(player.inventory.markers.values()) == [1 for _ in range(6)]

    def test_number_of_all_markers(self, player, stone_markers):
        assert player.inventory.check_number_markers() == 6
