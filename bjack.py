import random

class Card:
    RANK_NAMES = {
        "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
        "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
        "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{Card.RANK_NAMES[self.rank]} of {self.suit}"
    
class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Shoe:
    def __init__(self, num_decks=2, penetration=random.randint(0.4, 0.8)):
     
        self.num_decks = num_decks
        self.penetration = penetration

        self.cards = self._build_shoe()
        self.initial_size = len(self.cards)                  # e.g., 104 for 2 decks
        self.cut_index = int(self.initial_size * penetration) # e.g., ~62 cards dealt

        self.discard_pile = []
        self.shuffle()


print(self.penetration)