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
        self.captain = None
        self.communications = []
        self.missions = []

    def distribute_deck(self, shuffle=False):
        """Distribute all deck cards. When playing with 3 players
        Distribution is odd. First player has +1 card.
        """
        if shuffle:
            self.deck.shuffle()

        while self.deck.size() > 0:
            for _player in self.players:
                if self.deck.is_empty():
                    continue

                card = self.deck.pop()
                # blong: Find a better synthax to find a given card.
                # here we want to know if the card is the 4 black => captain.
                if card.value == 4 and card.color == "black":
                    self.captain = _player
                _player.add(card)

    def display_current_state(self):
        print("*****************************")
        print("The Crew: Current State")
        print(f"Captain: {self.captain}")
        # self.deck.display_current_state()
        if self.missions:
            print(f"Missions:")
            for mission in self.missions:
                print(f"{mission}")
        else:
            print("No Missions - Enjoy the sea <3")
        print(f"Players:")
        for player in self.players:
            player.display_current_state()
        print("*****************************")


if __name__ == "__main__":
    the_crew = TheCrew()
    the_crew.distribute_deck(shuffle=True)
    the_crew.display_current_state()

    # result = input("Display Current State? (y,n)")
    # if result:
    #     the_crew.display_current_state()
