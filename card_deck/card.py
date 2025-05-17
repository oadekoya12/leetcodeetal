# Step 1: Define the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

# Step 2: Create a deck class
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def show_deck(self):
        for card in self.cards:
            print(card)
