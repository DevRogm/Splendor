import pytest
from game.game_elements.stone_markers import StoneMarker
from game_data.markes_and_cards_data import markers


class TestStoneMarkers:
    @pytest.fixture
    def marker(self):
        marker = StoneMarker(**markers[5])
        return marker

    def test_marker_init(self, marker):
        assert marker

    def test_marker_is_joker(self, marker):
        assert marker.joker

