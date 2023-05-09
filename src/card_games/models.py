

class Card(object):
    """A card is defined by a color and a value"""

    def __init__(self,color,value):
        """Constructor of the class Card"""
        self.value = value
        self.color = color

    def __str__(self):
        """Return a string representation of the card."""
        return f"{self.value} {self.color}"
