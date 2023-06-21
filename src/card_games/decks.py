from src.card_games.models import Deck

# Various Constant. Don't know where to put them.
SPADE = "spade"
HEART = "heart"
TRUMP = "trump"
DIAMOND = "diamond"

BLUE = "blue"
YELLOW = "yellow"
GREEN = "green"
PINK = "pink"
BLACK = "black"


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
    deck.add_cards(values=values, color=SPADE)
    deck.add_cards(values=values, color=TRUMP)
    deck.add_cards(values=values, color=HEART)
    deck.add_cards(values=values, color=DIAMOND)

    if shuffled:
        deck.shuffle()

    return deck


def get_the_crew_deck(shuffled=False):
    """Generic method to create the crew deck."""
    deck = Deck()
    values = [(i, str(i)) for i in range(1, 10)]
    spade_values = [(i, str(i)) for i in range(1, 5)]
    deck.add_cards(values=values, color=BLUE)
    deck.add_cards(values=values, color=YELLOW)
    deck.add_cards(values=values, color=PINK)
    deck.add_cards(values=values, color=GREEN)
    deck.add_cards(values=spade_values, color=BLACK)

    if shuffled:
        deck.shuffle()

    return deck
