import pytest
from game.game_elements.aristocratic_cards import AristocraticCard


class TestAristocraticCards:
    data = {'requirements': {'emerald': 3, 'sapphire': 3, 'diamond': 3}, 'points': 3, 'img': 'card.png'}

    @pytest.fixture
    def card(self):
        card = AristocraticCard(**self.data)
        return card

    def test_card_init(self, card):
        assert card

    def test_card_requirements(self, card):
        assert type(card.requirements) is dict
