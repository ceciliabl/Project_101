from src.card_games import decks


def test_deck_factory_create_battle_deck():
    deck = decks.get_regular_52_cards_deck(shuffled=False)
    shuffled_deck = decks.get_regular_52_cards_deck(shuffled=True)

    assert deck.size() == shuffled_deck.size() == 52


def test_deck_factory_create_the_crew_deck():
    deck = decks.get_the_crew_deck()
    shuffled_deck = decks.get_the_crew_deck(shuffled=True)

    assert deck.size() == shuffled_deck.size() == 40
