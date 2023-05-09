import random
import copy

#from .models import Card, Deck


class Card(object):
    """A card is defined by a color and a value"""

    def __init__(self,color,value):
        """Constructor of the class Card"""
        self.value = value
        self.color = color

    def __str__(self):
        """Return a string representation of the card."""
        return f"{self.value} {self.color}"


class Deck(object):
    """A deck is defined by a list of cards"""

    def __init__(self):
        """Constructor of the class Deck"""
        self.values = (1,2,3,4,5,6,7,8,9,10,11,12,13)
        self.colors = ("carreaux","pique","coeur","trèfle")
        self._deck = []
        for color in self.colors:
            for value in self.values:
                card = Card(color,value)
                self._deck.append(card)

    def shuffle(self):
        """Shuffle the deck of cards"""
        random.shuffle(self._deck)

    def size(self):
        """Return the curent size of the deck"""
        return len(self._deck)

    def pop(self):
        """Return the last card of the deck and remove it from the deck"""
        return self._deck.pop()

    def get(self, index):
        """Return the card at the given index"""
        if index < 0 or index > len(self._deck):
            raise Exception("Index out of range")
        return self._deck[index]


class PlayedCard(object):
    """A played card is defined by a card and a player.
    It is used to compare cards between players during a game.
    Ex: played_card1 = PlayedCard(card1, 1)
    """

    def __init__(self, card: Card, player):
        """Constructor of the class PlayedCard"""
        self.card = card
        self.player = player


class Player(object):
    """A player is defined by a PrimaryKey (pk), a name and a list of cards"""

    def __init__ (self, pk: int, name: str):
        """Constructor of the class Player"""
        self.pk = pk
        self.name = name
        self.hand = []

    def add(self, card: Card):
        """Add a card to the player's hand"""
        self.hand.append(card)

    def pop(self, index: int):
        """Remove a card from the player's hand and return it
        :param index: index of the card to remove
        :return: the removed card
        :return_type: PlayedCard
        """
        _card = self.hand.pop(index)
        return PlayedCard(_card, self)

    def size(self):
        return len(self.hand)


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

    def __init__ (self):
        """Constructor of the class Bataille"""
        self.players = [Player(1, "Cecilia"), Player(2, "Jiben2")]
        self.deck= Deck()

    def distribute(self):
        """Shuffle the deck and distribute the cards between the two players.
        Return the hands of the two players to match current compare method.
        """

        self.deck.shuffle()

        index = 0
        while (len(self.deck._deck)):
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
    deck = Deck()
    deck.shuffle()

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
