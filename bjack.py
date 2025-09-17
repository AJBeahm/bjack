import random

bal = 0
game = 0

deck = [
    {'name': 'Two of Hearts', 'value': 2},
    {'name': 'Three of Hearts', 'value': 3},
    {'name': 'Four of Hearts', 'value': 4},
    {'name': 'Five of Hearts', 'value': 5},
    {'name': 'Six of Hearts', 'value': 6},
    {'name': 'Seven of Hearts', 'value': 7},
    {'name': 'Eight of Hearts', 'value': 8},
    {'name': 'Nine of Hearts', 'value': 9},
    {'name': 'Ten of Hearts', 'value': 10},
    {'name': 'Jack of Hearts', 'value': 10},
    {'name': 'Queen of Hearts', 'value': 10},
    {'name': 'King of Hearts', 'value': 10},
    {'name': 'Ace of Hearts', 'value': 11},

    {'name': 'Two of Diamonds', 'value': 2},
    {'name': 'Three of Diamonds', 'value': 3},
    {'name': 'Four of Diamonds', 'value': 4},
    {'name': 'Five of Diamonds', 'value': 5},
    {'name': 'Six of Diamonds', 'value': 6},
    {'name': 'Seven of Diamonds', 'value': 7},
    {'name': 'Eight of Diamonds', 'value': 8},
    {'name': 'Nine of Diamonds', 'value': 9},
    {'name': 'Ten of Diamonds', 'value': 10},
    {'name': 'Jack of Diamonds', 'value': 10},
    {'name': 'Queen of Diamonds', 'value': 10},
    {'name': 'King of Diamonds', 'value': 10},
    {'name': 'Ace of Diamonds', 'value': 11},

    {'name': 'Two of Clubs', 'value': 2},
    {'name': 'Three of Clubs', 'value': 3},
    {'name': 'Four of Clubs', 'value': 4},
    {'name': 'Five of Clubs', 'value': 5},
    {'name': 'Six of Clubs', 'value': 6},
    {'name': 'Seven of Clubs', 'value': 7},
    {'name': 'Eight of Clubs', 'value': 8},
    {'name': 'Nine of Clubs', 'value': 9},
    {'name': 'Ten of Clubs', 'value': 10},
    {'name': 'Jack of Clubs', 'value': 10},
    {'name': 'Queen of Clubs', 'value': 10},
    {'name': 'King of Clubs', 'value': 10},
    {'name': 'Ace of Clubs', 'value': 11},

    {'name': 'Two of Spades', 'value': 2},
    {'name': 'Three of Spades', 'value': 3},
    {'name': 'Four of Spades', 'value': 4},
    {'name': 'Five of Spades', 'value': 5},
    {'name': 'Six of Spades', 'value': 6},
    {'name': 'Seven of Spades', 'value': 7},
    {'name': 'Eight of Spades', 'value': 8},
    {'name': 'Nine of Spades', 'value': 9},
    {'name': 'Ten of Spades', 'value': 10},
    {'name': 'Jack of Spades', 'value': 10},
    {'name': 'Queen of Spades', 'value': 10},
    {'name': 'King of Spades', 'value': 10},
    {'name': 'Ace of Spades', 'value': 11},
]



random.shuffle(deck)

##def draw_card():
    ##return deck.pop()

##def make_hand():

##card = draw_card()
##print(card)

def welcome():
    """Ask if the user wants to play. Return starting balance or None if they quit."""
    while True:
        ans = input("Would you like to play? (Y/N): ").strip().upper()
        if ans == "Y":
            print("Okay, here's 100 chips.")
            return 100               # <-- give the caller a balance
        elif ans == "N":
            print("Goodbye")
            return None              # <-- exit cleanly
        else:
            print("Please enter Y or N.")

def ask_bet(bal: int, min_bet: int = 1) -> int:
    """Keep asking until the bet is a whole number between min_bet and bal."""
    while True:
        raw = input(f"Place your bet (${min_bet}–${bal}): ").strip()
        try:
            bet = int(raw)
        except ValueError:
            print("Please enter a whole number (e.g., 10).")
            continue

        if bet < min_bet:
            print(f"Bet must be at least ${min_bet}.")
            continue
        if bet > bal:
            print("You can't bet more than your current balance.")
            continue

        return bet                   # <-- important!

if __name__ == "__main__":
    bal = welcome()                  # <-- get starting balance
    if bal:                          # None/0 means they didn’t start
        bet = ask_bet(bal)           # <-- now we enter ask_bet
        print(f"You bet ${bet}.")
        bal -= bet
        print(f"Remaining balance: ${bal}")

