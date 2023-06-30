import random

from abc import ABC
from enum import Enum

from src.card_games.constants import (
    BLUE, BLACK, PINK, GREEN, YELLOW
)


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

    def add_cards(self, cards: [Card]):
        """Add Cards to the deck."""
        for card in cards:
            self.add_card(card)

    def add_card(self, card: Card):
        return self.cards.append(card)

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
        self.cards = []
        self.folds = []

    def __str__(self):
        return f"{self.pk} {self.name}"

    def display_current_state(self, with_cards:bool = False):
        print(f"{self.__str__()}: #cards: {len(self.cards)} #folds: {len(self.folds)}")
        if with_cards:
            self._display_cards()

    def _display_cards(self):
        from tabulate import tabulate
        cards_data = []
        suit = self._filter_suit(BLUE)
        cards_data.append(
            [
                ' '.join([card.display_name for card in self._filter_suit(BLUE)]),
                ' '.join([card.display_name for card in self._filter_suit(GREEN)]),
                ' '.join([card.display_name for card in self._filter_suit(YELLOW)]),
                ' '.join([card.display_name for card in self._filter_suit(PINK)]),
                ' '.join([card.display_name for card in self._filter_suit(BLUE)]),
            ]
        )
        print(tabulate(cards_data, headers=["BLUE", "GREEN", "YELLOW", "PINK", "BLACK"]))

    def _filter_suit(self, color, ordered=False):
        suit = list(filter(lambda c: c.color == color, self.cards))
        if ordered:
            suit.sort(key=lambda c: c.value)
        return suit

    def do_order_cards(self):
        # TODO: Factorized.
        blue_cards = self._filter_suit(BLUE, ordered=True)
        pink_cards = self._filter_suit(PINK, ordered=True)
        green_cards = self._filter_suit(GREEN, ordered=True)
        yellow_cards = self._filter_suit(YELLOW, ordered=True)
        black_cards = self._filter_suit(BLACK, ordered=True)

        _cards = []
        if blue_cards:
            _cards.extend(blue_cards)
        if pink_cards:
            _cards.extend(pink_cards)
        if green_cards:
            _cards.extend(green_cards)
        if yellow_cards:
            _cards.extend(yellow_cards)
        if black_cards:
            _cards.extend(black_cards)

        self.cards = _cards

    def add(self, card: Card):
        """Add a card to the player's cards"""
        self.cards.append(card)

    def pop(self, index: int):
        """Remove a card from the player's cards and return a PlayedCard
        :param index: index of the card to remove
        :return: the removed card
        :return_type: PlayedCard
        """
        _card = self.cards.pop(index)
        return PlayedCard(_card, self)

    def size(self):
        return len(self.cards)



class PlayedCard(object):
    """A played card is defined by a card and a player.
    It is used to compare cards between players during a game.
    Ex: played_card1 = PlayedCard(card1, 1)
    """

    def __init__(self, card: Card, player: Player):
        """Constructor of the class PlayedCard"""
        self.card = card
        self.player = player


class Fold(object):
    """A Fold is defined ba a list of PlayedCard.
    It is used to hold the list of each card played by players during card games.
    """

    def __init__(self, expected_cards):
        self.expected_cards = expected_cards
        self.played_cards = []

    def display_current_state(self):
        return f"         TODO           "

    def add(self, played_card: PlayedCard):
        # blong: Should we check validity here ?!
        # Not sure, a fold model should have this knowledge. Seems we should have
        # A FoldHandler to control Player-Fold interaction based on current
        # played game.
        # if not self._is_played_card_valid(played_card):
        #     return False

        self.played_cards.append(played_card)
        return True

    def _first(self):
        return self.played_cards[0] if len(self.played_cards) else None


class MissionStatus(Enum):
    DONE = "done"
    FAILED = "failed"
    TODO = "todo"


class BaseMission(ABC):
    status: MissionStatus = MissionStatus.TODO
    player: Player = None
    level: int

    def is_accomplished(self):
        raise Exception("Not Implemented")


class CardMission(BaseMission):
    cards: [Card]

    def __init__(self, cards: [Card], level: int):
        """Constructor of the class CardMission"""
        self.cards = cards
        self.level = level

    def __str__(self):
        _cards = [card.__str__() for card in self.cards]
        return f"Win {','.join(_cards)}"

    def display_current_state(self, index=None):
        index = "" if index is None else f"[{index}] "

        _cards = [card.__str__() for card in self.cards]
        print(f"{index}{self.__str__()}: #player: {self.player}")


    def is_accomplished(self):
        pass
