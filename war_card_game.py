"""We need shuffle from random"""
import random

# All constants we need to create the cards
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """Deck class will use Card class to create each card"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def print_card(self):
        """Print suit and rank of the card"""
        print(self.rank + " of " + self.suit + f" ({self.value})")

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """Create the 52 cards of the game"""

    def __init__(self):
        self.all_cards = []

        # Card class being used to create the 52 cards of the game
        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        """Make the deck random"""
        random.shuffle(self.all_cards)

    def deal_one(self):
        """Remove one card from the deck"""
        return self.all_cards.pop()

    def __str__(self):
        return f"Deck has {(len(self.all_cards))} cards."


class Player:
    """Will create the players of the game"""

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """Removes the top card of the deck"""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """Add cards to the bottom of the deck"""

        # If it's a list and multiple cards will be added
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)

        # If it's a single card
        else:
            self.all_cards.append(new_cards)

    def __str__(self): 
        return f"{self.name} has {len(self.all_cards)} cards."


class GameSetup:
    """Setup the start of the game"""

    def __init__(self, player_one, player_two):
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.new_deck = Deck()
        self.new_deck.shuffle()

    def deck_setup(self):
        """Gives 26 cards for each player"""
        for _ in range(26):

            self.player_one.add_cards(self.new_deck.deal_one())
            self.player_two.add_cards(self.new_deck.deal_one())

    def __str__(self):
        return f"{self.player_one} vs {self.player_two}"

    def player_one_wins(self):
        """Player one wins the game"""

        print(f"{self.player_two.name} out of cards! {self.player_one.name} wins!")

    def player_two_wins(self):
        """Player two wins the game"""

        print(f"{self.player_one.name} out of cards! {self.player_two.name} wins!")


def play_game(player_one, player_two):
    """Game logic / Start the game"""

    game = GameSetup(player_one, player_two)
    game.deck_setup()

    game_on = True
    game_round = 0
    war = 10

    while game_on:

        game_round += 1
        print(f"Round: {game_round}")

        if len(game.player_one.all_cards) == 0:
            game.player_two_wins()
            game_on = False
            break

        if len(game.player_two.all_cards) == 0:
            game.player_one_wins()
            game_on = False
            break

        # Start a new Round
        player_one_cards = []
        player_one_cards.append(game.player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(game.player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:
                game.player_one.add_cards(player_one_cards)
                game.player_one.add_cards(player_two_cards)

                break

            if player_one_cards[-1].value < player_two_cards[-1].value:
                game.player_two.add_cards(player_one_cards)
                game.player_two.add_cards(player_two_cards)

                break

            print("War!")

            if len(game.player_one.all_cards) < war:
                game.player_two_wins()
                game_on = False
                break

            if len(game.player_two.all_cards) < war:
                game.player_one_wins()
                game_on = False
                break

            for _ in range(war):
                player_one_cards.append(game.player_one.remove_one())
                player_two_cards.append(game.player_two.remove_one())


play_game("Arthur", "Mileny")
