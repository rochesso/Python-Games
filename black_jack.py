"""We need shuffle from random"""
import random
import os

# All constants we need to create the cards
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """Deck class will use Card class to create each card"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def print_card(self):
        """Print suit and rank of the card"""
        return self.rank + " of " + self.suit + f" ({self.value})"

    def __str__(self):
        return self.rank + " of " + self.suit + f" ({self.value})"


class Deck:
    """Create the 52 cards of the game"""

    def __init__(self):
        # Card class being used to create the 52 cards of the game
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        """Make the deck random"""
        random.shuffle(self.deck)

    def deal(self):
        """Remove one card from the deck"""
        return self.deck.pop()

    def __str__(self):
        return '\n'.join(x.print_card() for x in self.deck)


class Hand:
    def __init__(self, name):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.name = name

    def add_cards(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def hit(self, deck):
        card = deck.deal()
        self.add_cards(card)
        self.adjust_for_ace()

    def show_one(self):
        print(f"Second {self.name}'s card is {self.cards[1]}")

    def show_all(self):
        print(f"{self.name}'s cards: ", *self.cards, sep="\n")
        print(f"{self.name}'s value: {self.value}")

    def __str__(self):
        return '\n'.join(x.print_card() for x in self.cards)


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):

        while True:

            try:
                self.bet = int(
                    input('How many chips would you like to bet? '))
            except:
                print('Sorry, please provide an integer')
            else:
                if self.bet <= 0:
                    print(
                        f'Sorry, try a number greater than 0!')

                elif self.bet > self.total:
                    print(
                        f'Sorry, you do not have enough chips! You have: {self.total}')
                else:
                    break


class Game:

    def __init__(self, player1, player2):
        self.playing = True
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Hand(player1)
        self.dealer = Hand(player2)

    def hit_or_stand(self, hand):
        while True:
            x = ''
            while x == '':
                x = input('Hit or Stand? h/s: ')

            if x[0].lower() == 'h':
                hand.hit(self.deck)

            elif x[0].lower() == 's':
                self.playing = False

            else:
                print('Sorry, I did not understand! Enter h or s only!')
                continue
            break

    def show_some(self):
        self.dealer.show_one()
        print("")
        self.player.show_all()
        print("----------------")

    def show_all(self):
        self.dealer.show_all()
        print("")
        self.player.show_all()
        print("----------------")

    def push(self):
        print(f'{self.player.name} and {self.dealer.name} tie! Push!')


def play_game():
    player_chips = Chips()
    dealer_chips = Chips()
    while True:
        game = Game("Arthur", "Dealer")

        def current_game():
            os.system('clear')
            print("----------------")
            print('Welcome to BLACKJACK')
            print("----------------")
            print(f'{game.player.name} vs {game.dealer.name}')
            print("----------------")
            print(f'Dealer total: {dealer_chips.total}')
            print(f'Player total: {player_chips.total}')
            print("----------------")

        current_game()

        game.player.hit(game.deck)
        game.player.hit(game.deck)

        game.dealer.hit(game.deck)
        game.dealer.hit(game.deck)

        if not player_chips.total or not dealer_chips.total:
            if player_chips.total <= 0:
                print(f'{game.player.name} do not have more chips to play!')

            else:
                print(f'{game.dealer.name} do not have more chips to play!')

            break

        print("")
        while True:
            if (player_chips.total and dealer_chips.total) > 0:
                player_chips.take_bet()
                if player_chips.bet > dealer_chips.total:
                    print(f'{game.dealer.name} only has {dealer_chips.total}')
                    continue
                else:
                    dealer_chips.bet = player_chips.bet
                    current_game()
                    game.show_some()
                    break

        while game.playing:
            game.hit_or_stand(game.player)
            current_game()
            game.show_some()

            if game.player.value > 21:
                current_game()
                game.show_all()
                print(f'{game.dealer.name} wins!')
                dealer_chips.win_bet()
                player_chips.lose_bet()
                break

        if game.player.value <= 21:

            while game.dealer.value < game.player.value:
                game.dealer.hit(game.deck)

            current_game()
            game.show_all()

            if game.dealer.value > 21:
                print(f'{game.player.name} wins!')
                dealer_chips.lose_bet()
                player_chips.win_bet()
            elif game.dealer.value > game.player.value:
                print(f'{game.dealer.name} wins!')
                dealer_chips.win_bet()
                player_chips.lose_bet()
            elif game.dealer.value < game.player.value:
                print(f'{game.player.name} wins!')
                dealer_chips.lose_bet()
                player_chips.win_bet()
            else:
                game.push()

        print("----------------")
        print(f'{game.dealer.name} total: {dealer_chips.total}')
        print(f'{game.player.name} total: {player_chips.total}')

        new_game = ''
        while new_game == '':
            new_game = input('Would you like to play again? y/n: ')

        if new_game[0].lower() == 'y':
            continue

        else:
            print('Thanks for playing!')
            break

    print(f'{game.dealer.name} total: {dealer_chips.total}')
    print(f'{game.player.name} total: {player_chips.total}')


play_game()
