import pytest
from card import Card
from card import Deck  # Assuming card.py contains your class definition

# Test card creation
def test_card_initialization():
    card = Card("Hearts", "Ace")
    assert card.suit == "Hearts"
    assert card.value == "Ace"

# Test card display format
def test_card_display():
    card = Card("Diamonds", "King")
    assert str(card) == "King of Diamonds"

# Test full deck creation (should have 52 cards)
def test_deck_creation():
    deck = Deck()
    assert len(deck.cards) == 52

# Test if first card in the deck is Ace of Hearts
def test_first_card_in_deck():
    deck = Deck()
    assert str(deck.cards[0]) == "Ace of Hearts"

if __name__ == "__main__":
    pytest.main()
