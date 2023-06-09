import random
import copy

#from .models import Card, Deck


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

    def size(self):
        return len(self._deck)

    def pop(self):
        return self._deck.pop()

    def get(self, index):
        if index < 0 or index > len(self._deck):
            raise Exception("Index out of range")
        return self._deck[index]


class PlayedCard(object):
    def __init__(self, card, player):
        self.card = card
        self.player = player


class Hand(object):
    def __init__ (self, player: int):
        self.player = player
        self.list = []

    def add(self, card: Card):
        self.list.append(card)

    def pop(self, index: int):
        _card = self.list.pop(index)
        return PlayedCard(_card, self.player)

    def size(self):
        return len(self.list)


class Bataille(object):
    def __init__ (self):
        self.hands = [Hand(1), Hand(2)]
        self.deck= Deck()

    def distribute(self):
        self.deck.shuffle()

        index = 0
        while (len(self.deck._deck)):
            _player = index % len(self.hands)
            self.hands[_player].add(self.deck.pop())
            index += 1

        # just go 2 by 2
        # for card in self.deck._deck:
        #     _list = list1 if index % 2 == 0 else list2
        #     _list.append(card)
        #     index += 1

        return self.hands

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

    def play(self):
        hand1, hand2 = b.distribute()
        print(hand1.size())
        assert hand1.size() == hand2.size()

        l=[]
        # hand1.empty()

        while(hand2.size() != 0 and hand1.size() !=0 ):
            # played_card = hand1.play()
            card1 = hand1.pop(0)
            card2 = hand2.pop(0)
            print()
            print(card1, card2)
            l = l + [card1, card2]
            print ("nombre de cartes a gagner ", len(l))
            hand1, hand2, l = b.compare(hand1, hand2, card1, card2, l)
            print(f"Deck 1: {hand1.size()} vs Deck 2: {hand2.size()}")

        if(hand1.size() == 0):
            print ("winner is player 2")
        else:
            print ("winner is player 1")

deck = Deck()
deck.shuffle()

b = Bataille()

b.play()

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
