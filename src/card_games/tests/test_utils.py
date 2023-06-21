from src.card_games import utils


def test_get_anonumous_players():
    players_2 = utils.get_anonymous_players(2)
    players_3 = utils.get_anonymous_players(3)

    assert len(players_2) == 2
    assert len(players_3) == 3
