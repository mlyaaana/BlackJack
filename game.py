from deck import Deck
from player import Player


class Game:
    m = 21
    aces = ["♥️A", "♦️A", "♣️A", "♠️A"]

    def __init__(self):
        self.deck = Deck()
        self.player = Player(input("Enter your name\n"))
        self.dealer = Player("Dealer")

    def start(self):
        self.player.add_card(self.deck.get_card())
        tmp1 = self.player.add_card(self.deck.get_card())
        p_total = self.ace(tmp1, self.player)
        p_cards = ", ".join(map(lambda card: str(card), tmp1))

        tmp2 = self.dealer.add_card(self.deck.get_card())
        d_total = self.ace(tmp2, self.dealer)
        d_cards = ", ".join(map(lambda card: str(card), tmp2))

        print(f"{self.player.name}: {p_cards}; {p_total}")
        print(f"{self.dealer.name}: {d_cards}; {d_total}")

        if self.blackjack(tmp1, p_total):
            print("\nYou are lucky!\nBLACKJACK!")
            self.play_again()

    def process(self):
        p_total, d_total = 0, 0

        while p_total < self.m:
            q = input("Hit or stand? (h/s)\n")
            if q == "h":
                tmp = self.player.add_card(self.deck.get_card())
                p_total = self.ace(tmp, self.player)
                p = ", ".join(map(lambda card: str(card), tmp))
                print(f"{self.player.name}: {p}; {p_total}")
            elif q == "s":
                p_total = self.player.total()
                break
            else:
                print("Enter 'h' or 's'")
                self.process()

        while d_total <= 16:
            tmp = self.dealer.add_card(self.deck.get_card())
            d_total = self.ace(tmp, self.dealer)
            d = ", ".join(map(lambda card: str(card), tmp))
            print(f"{self.dealer.name}: {d}; {d_total}")
            if p_total > self.m:
                break
            if self.blackjack(tmp, d_total):
                print("\nSuddenly, dealer has blackjack\nDEFEAT")
                self.play_again()

        self.conclusion(p_total, d_total)

    def blackjack(self, hand, total):
        if len(hand) == 2 and total == self.m:
            return True

    def conclusion(self, p_total, d_total):
        if p_total < d_total <= self.m:
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

    def ace(self, hand, player):
        total = player.total()
        for card in hand:
            if str(card) in self.aces:
                t = player.total() + 10
                if t <= self.m:
                    card.points = 11
                    return player.total()
                else:
                    return total
        return total
