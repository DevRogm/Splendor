import pytest
from game.game_elements.stone_cards import StoneCard
from game_data.markes_and_cards_data import cards_3_3_4


class TestStoneCards:
    @pytest.fixture
    def card(self):
        card = StoneCard(**cards_3_3_4[0])
        return card

    def test_card_init(self, card):
        assert card

    def test_card_requirements_type(self, card):
        assert type(card.requirements) is dict

    def test_card_requirements_length(self, card):
        assert len(card.requirements) >= 1
