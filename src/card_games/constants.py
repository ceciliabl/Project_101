from enum import Enum


# -----------------------------------------------------------------------------
# Various Constant.
# blong: Don't know where to put them.
# -----------------------------------------------------------------------------
class CARD_COLORS(Enum):
    SPADE = "spade"
    HEART = "heart"
    TRUMP = "trump"
    DIAMOND = "diamond"


class THECREW_COLORS(Enum):
    BLUE = "blue"
    YELLOW = "yellow"
    GREEN = "green"
    PINK = "pink"


THECREW_TRUMP = "black"


SPADE = "spade"
HEART = "heart"
TRUMP = "trump"
DIAMOND = "diamond"

BLUE = "blue"
YELLOW = "yellow"
GREEN = "green"
PINK = "pink"
BLACK = "black"

DEFAULT_SUIT = (
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
