from src.card_games.battle import Bataille


def test_battle():
    battle = Bataille()
    assert len(battle.players) == 2
