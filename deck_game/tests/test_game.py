import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_card_order(self):
        self.game.add_card("Spades", "3")
        self.game.add_card("Hearts", "K")
        self.assertFalse(self.game.card_beats(0, 1))

    def test_high_card_wins(self):
        self.game.add_card("Clubs", "J")
        self.game.add_card("Spades", "A")
        self.assertTrue(self.game.card_beats(0, 1))

    def test_equal_card_tie(self):
        self.game.add_card("Hearts", "10")
        self.game.add_card("Diamonds", "10")
        self.assertFalse(self.game.card_beats(0, 1))

    def test_joker_wins(self):
        self.game.add_card("Diamonds", "5")
        self.game.add_joker("Red")
        self.assertTrue(self.game.card_beats(1, 0))

    def test_two_jokers_tie(self):
        self.game.add_joker("Red")
        self.game.add_joker("Black")
        self.assertFalse(self.game.card_beats(0, 1))

    def test_suit_tiebreaker(self):
        self.game.add_card("Spades", "9")
        self.game.add_card("Hearts", "9")
        self.assertFalse(self.game.card_beats(0, 1))

if __name__ == "__main__":
    unittest.main()
