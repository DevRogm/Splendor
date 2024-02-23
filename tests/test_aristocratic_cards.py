import pytest
from game.game_elements.aristocratic_cards import AristocraticCard
from game_data.markes_and_cards_data import aristocratic_cards


class TestAristocraticCards:
    @pytest.fixture
    def card(self):
        card = AristocraticCard(**aristocratic_cards[0])
        return card

    def test_card_init(self, card):
        assert card

    def test_card_requirements_type(self, card):
        assert type(card.requirements) is dict

    def test_card_requirements_length(self, card):
        assert len(card.requirements) >= 1
