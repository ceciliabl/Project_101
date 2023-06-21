from src.card_games import decks, utils

"""
Currently this file is the entry point to play a game of The Crew.
Just call python src/card_games/the_crew.py to play a game on your terminal.
"""


class TheCrew(object):
    """A game of The Crew is defined by a deck of cards and muliple players.
    Game follow the following rules:
    - The deck is shuffled and distributed between the players.
    - TODO...
    """

    def __init__(self, players=None):
        """Constructor of the class Bataille"""
        if players is None:
            players = utils.get_anonymous_players(3)

        self.players = players
        self.deck = decks.get_the_crew_deck()

    def distribute_deck(self):
        """Distribute all deck cards. When playing with 3 players
        Distribution is odd. First player has +1 card.
        """
        while self.deck.size() > 0:
            for _player in self.players:
                if self.deck.is_empty():
                    continue

                card = self.deck.pop()
                _player.add(card)


if __name__ == "__main__":
    the_crew = TheCrew()
    the_crew.distribute_deck()
