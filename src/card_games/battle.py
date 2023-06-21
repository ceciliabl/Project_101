from src.card_games import decks, utils

"""
Currently this file is the entry point to play a game of Bataille.
Just call python src/card_games/battle.py to play a game on your terminal.
"""


class Bataille(object):
    """A game of Bataille is defined by a deck of cards and two players.
    Game follow the following rules:
    - The deck is shuffled and distributed between the two players
    - Each player plays the first card of his deck
    - The player with the highest card wins and takes the two cards
    - If both cards are equal, a "bataille" is declared
    - Each player plays the first card of his deck
    - The player with the highest card wins and takes all the cards
    - Or a new "bataille" is declared... etc
    """

    def __init__ (self, players=None):
        """Constructor of the class Bataille"""
        if players is None:
            players = utils.get_anonymous_players(2)

        self.players = players
        self.deck = decks.get_regular_52_cards_deck()

    def distribute(self):
        """Shuffle the deck and distribute the cards between the two players.
        Return the hands of the two players to match current compare method.
        """
        self.deck.shuffle()

        index = 0
        while (self.deck.size() > 0):
            for _player in self.players:
                _player.add(self.deck.pop())
                index += 1

        return self.players[0].hand, self.players[1].hand

    # blong: does not work. Because card1 and card2 are now PlayedCard.
    # def compare(played_card1, played_card2)
    # ex: card1 = played_card.card
    # but now played card ownes player and card info
    def compare(self, list1, list2, card1, card2, l):
        if card1.value < card2.value:
            list2 = list2 + l
            print("j2 gagne, carte j1 ", len(list1))
            print("j2 gagne, carte j2 ", len(list2))
            l.clear()
            return list1, list2, l
        elif card2.value < card1.value:
            list1 = list1 + l
            print("j1 gagne, carte j1 ",len(list1))
            print("j1 gagne, carte j2 ", len(list2))
            l.clear()
            return list1, list2, l
        else:
            print()
            print("BATAILLE")
            print()
            if(len(list2) != 0 and len(list1) != 0):
                c3 = list1.pop(0)
                c4 = list2.pop(0)
                l = l + [c3 , c4]

                print ("nombre de cartes a gagner ", len(l))
                return list1, list2, l
            else:
                return list1, list2, l


if __name__ == "__main__":
    b = Bataille()
    list1, list2 = b.distribute()
    print(len(list1))
    assert len(list1) == len(list2)

    l=[]

    while(len (list2)!=0 and len(list1) !=0 ):
        card1 = list1.pop(0)
        card2 = list2.pop(0)
        print()
        print(card1, card2)
        l = l + [card1, card2]
        print ("nombre de cartes a gagner ", len(l))
        list1, list2, l = b.compare(list1, list2, card1, card2, l)
        print(f"Deck 1: {len(list1)} vs Deck 2: {len(list2)}")

    if(len(list1)==0):
        print ("winner is player 2")
    else:
        print ("winner is player 1")
