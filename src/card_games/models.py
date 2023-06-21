import random


class Card(object):
    """A card is defined by a color and a value"""

    def __init__(self, color: str, value: int, display_name: str = None):
        """Constructor of the class Card"""
        self.color = color
        self.value = value
        self.display_name = display_name

    def __str__(self):
        if self.display_name:
            return f"{self.display_name} {self.color}"
        """Return a string representation of the card."""
        return f"{self.value} {self.color}"


class Deck(object):
    """A deck is defined by a list of cards"""

    def __init__(self):
        """Constructor of the class Deck"""
        self.cards = []

    def display_current_state(self):
        print(f"Deck #cards: {len(self.cards)}")

    def add_cards(self, values: list or tuple, color: str):
        """Add values cards with the given color.
        :param: values (list, tuples)
        :param: color

        Ex:
          deck.add_cards(values=((1, "As"), (2, "2")), color=deck.SPADE)
        """
        for value in values:
            if isinstance(value, tuple):
                _value = value[0]
                _name = value[1]
            else:
                _value = value
                _name = None

            self.add_card(color, _value, _name)

    def add_card(self, color:str, value: int, display_name=None):
        self.cards.append(Card(color, value, display_name))

    def shuffle(self):
        """Shuffle the deck of cards"""
        random.shuffle(self.cards)

    def is_empty(self):
        return len(self.cards) == 0

    def size(self):
        """Return the curent size of the deck"""
        return len(self.cards)

    def pop(self):
        """Return the last card of the deck and remove it from the deck"""
        return self.cards.pop()

    def get(self, index):
        """Return the card at the given index"""
        if index < 0 or index > len(self.cards):
            raise Exception("Index out of range")
        return self.cards[index]


class Player(object):
    """A player is defined by a PrimaryKey (pk), a name and a list of cards"""

    def __init__ (self, pk: int, name: str):
        """Constructor of the class Player"""
        self.pk = pk
        self.name = name
        self.hand = []
        self.folds = []

    def __str__(self):
        return f"{self.pk} {self.name}"

    def display_current_state(self):
        print(f"{self.__str__()}: #cards: {len(self.hand)} #folds: {len(self.folds)}")

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


class PlayedCard(object):
    """A played card is defined by a card and a player.
    It is used to compare cards between players during a game.
    Ex: played_card1 = PlayedCard(card1, 1)
    """

    def __init__(self, card: Card, player: Player):
        """Constructor of the class PlayedCard"""
        self.card = card
        self.player = player
