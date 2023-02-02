from deck import Deck
from player import Player
from util import printer


class Game:
    m = 21
    dealer_max = 16

    def __init__(self):
        self.deck = Deck()
        self.player = Player(input("Enter your name\n"))
        self.dealer = Player("Dealer")

    def start(self):
        self.player.add_card(self.deck.get_card())
        p_total, p_cards, p_hand = self.give_card(self.player)
        d_total, d_cards, d_hand = self.give_card(self.dealer)

        printer(self.player, p_cards, p_total)
        printer(self.dealer, d_cards, d_total)

    def process(self):
        p_total, d_total = 0, 0
        p_hand, d_hand = [], []

        while p_total < self.m:
            q = input("Hit or stand? (h/s)\n")
            if q == "h":
                p_total, p_cards, p_hand = self.give_card(self.player)
                printer(self.player, p_cards, p_total)
            elif q == "s":
                # мб нужен вызов ace()
                p_total = self.player.total_up()
                break
            else:
                print("Enter 'h' or 's'")

        while d_total <= self.dealer_max:
            d_total, d_cards, d_hand = self.give_card(self.dealer)
            printer(self.dealer, d_cards, d_total)
            if p_total > self.m or p_total == 21:
                break

        self.conclusion(p_total, d_total, p_hand, d_hand)

    def give_card(self, player):
        hand = player.add_card(self.deck.get_card())
        total = player.total_up()
        cards = ", ".join(map(lambda card: str(card), hand))
        return total, cards, hand

    def conclusion(self, p_total, d_total, p_hand, d_hand):
        if len(p_hand) == 2 and p_total == self.m:
            print("\nYou are lucky!\nBLACKJACK!")
        elif len(d_hand) == 2 and d_total == self.m:
            print("\nSuddenly, dealer has blackjack\nDEFEAT")
        elif p_total < d_total <= self.m:
            print("\nDealer has a better score\nDEFEAT")
        elif p_total > self.m:
            print("\nToo much\nDEFEAT")
        elif self.m >= p_total > d_total or p_total < d_total > self.m:
            print("\nWIN!")
        else:
            print("\nDRAW")
        self.play_again()

    def play_again(self):
        q = input("\nPlay again? (y/n)\n")
        if q == "y":
            self.reset()
            self.start()
            self.process()
        elif q == 'n':
            print("Thanks for playing!")
            exit(1)
        else:
            print("Enter 'y' or 'n'")
            self.play_again()

    def reset(self):
        self.deck = Deck()
        self.player.hand = []
        self.dealer.hand = []
    #
    # def ace(self, hand, player):
    #     total = player.total()
    #     for card in hand:
    #         if card.rank == "A" in self.aces:
    #             t = player.total() + 10
    #             if t <= self.m:
    #                 card.points = 11
    #                 return player.total()
    #             else:
    #                 return total
    #     return total
