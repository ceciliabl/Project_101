import random

from src.card_games.models import Deck, Card, CardMission
from src.card_games.constants import (
    SPADE, HEART, DIAMOND, TRUMP,
    BLUE, BLACK, PINK, GREEN, YELLOW
)


# -----------------------------------------------------------------------------
def generate_suit(color, values):
    """Generate a colored suit of Card."""
    suit = []
    for value in values:
        if isinstance(value, tuple):
            _value = value[0]
            _name = value[1]
        else:
            _value = value
            _name = None

        suit.append(Card(color, _value, _name))

    return suit


def get_regular_52_cards_deck(shuffled=False):
    """Generic method to create a regular 52 cards games.
    As value is one.
    """
    values = (
        (1, "A"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "J"),
        (12, "Q"),
        (13, "K"),
    )

    deck = Deck()
    deck.add_cards(generate_suit(values=values, color=SPADE))
    deck.add_cards(generate_suit(values=values, color=TRUMP))
    deck.add_cards(generate_suit(values=values, color=HEART))
    deck.add_cards(generate_suit(values=values, color=DIAMOND))

    if shuffled:
        deck.shuffle()

    return deck


# -----------------------------------------------------------------------------
def get_the_crew_deck(shuffled=False):
    """Generic method to create the crew cards deck."""
    deck = Deck()
    values = [(i, str(i)) for i in range(1, 10)]
    spade_values = [(i, str(i)) for i in range(1, 5)]
    deck.add_cards(generate_suit(color=BLUE, values=values))
    deck.add_cards(generate_suit(color=YELLOW, values=values))
    deck.add_cards(generate_suit(color=PINK, values=values))
    deck.add_cards(generate_suit(color=GREEN, values=values))
    deck.add_cards(generate_suit(color=BLACK, values=spade_values))

    if shuffled:
        deck.shuffle()

    return deck


# -----------------------------------------------------------------------------
def get_the_crew_mission_deck(shuffled=False):
    """Generic method to create the crew missions deck."""
    _card_missions = []

    # blong: For each value form 1 to 10 exclusive, we create a CardMission
    # with a single Card.
    values = [(i, str(i)) for i in range(1, 10)]
    for value in values:
        _card_missions.append(CardMission(
            cards=[Card(display_name=value[1], value=value[0], color=BLUE)],
            level=1,
        ))
        _card_missions.append(CardMission(
            cards=[Card(display_name=value[1], value=value[0], color=YELLOW)],
            level=1,
        ))
        _card_missions.append(CardMission(
            cards=[Card(display_name=value[1], value=value[0], color=GREEN)],
            level=1,
        ))
        _card_missions.append(CardMission(
            cards=[Card(display_name=value[1], value=value[0], color=PINK)],
            level=1,
        ))

    if shuffled:
        random.shuffle(_card_missions)

    return _card_missions
