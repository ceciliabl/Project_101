import random



class Card(object):
    def __init__(self,color,value):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.value} {self.color}"


class Deck(object):
    def __init__(self):
        self.values = (1,2,3,4,5,6,7,8,9,10,11,12,13)
        self.colors = ("carreaux","pique","coeur","trèfle")
        self._deck = []
        for color in self.colors:
            for value in self.values:
                card = Card(color,value)
                self._deck.append(card)

    def shuffle(self):
        random.shuffle(self._deck)
