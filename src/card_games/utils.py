from src.card_games.tests.factories import PlayerFactory


def get_anonymous_players(number: int):
    """Get a list of Fake players.
    Generated using faker and factory-boy
    :param number: Number of player needed.
    :return: [Player<Toto>, Player<Titi>].
    """
    return [PlayerFactory.create() for i in range(number)]
