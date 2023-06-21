import factory

from src.card_games.models import Card, Deck, PlayedCard, Player


class CardFactory(factory.Factory):
    class Meta:
        model = Card

    value = 1
    color = "heart"


class DeckFactory(factory.Factory):
    class Meta:
        model = Deck


class PlayerFactory(factory.Factory):
    class Meta:
        model = Player

    pk = factory.Sequence(lambda n: n)
    name = factory.Faker("name")


class PlayedCardFactory(factory.Factory):
    class Meta:
        model = PlayedCard

    card = factory.SubFactory(CardFactory)
    player = factory.SubFactory(PlayerFactory)
