import pytest

from src.card_games.the_crew import TheCrew


def test_the_crew_is_instantiable():
    the_crew = TheCrew()
    assert isinstance(the_crew, TheCrew)


@pytest.fixture
def the_crew():
    return TheCrew()


def test_the_crew_distribute(the_crew):
    assert the_crew.deck.size() == 40
    the_crew.distribute_deck()
    assert the_crew.deck.size() == 0

    for _player in the_crew.players:
        assert len(_player.cards) != 0

    the_crew.display_current_state()
