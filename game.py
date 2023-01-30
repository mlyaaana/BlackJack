from dealer import Dealer
from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.player.add_card(self.deck.get_card())
        tmp1 = self.player.add_card(self.deck.get_card())
        p_cards = ", ".join(map(lambda card: str(card), tmp1))
        p_total = self.player.total()

        tmp2 = self.dealer.add_card(self.deck.get_card())
        d_cards = ", ".join(map(lambda card: str(card), tmp2))
        d_total = self.dealer.total()

        print(f"Your cards: {p_cards}; {p_total}")
        print(f"Dealer's cards: {d_cards}; {d_total}")
        if self.blackjack(tmp1, p_total):
            print("You are lucky!\nBLACKJACK!")
            self.play_again()

    def process(self):
        p_total = 0
        d_total = 0
        mx = 21
        while p_total < mx:
            q = input("Pass or add one? (p/a)\n")
            if q == "a":
                tmp = self.player.add_card(self.deck.get_card())
                p = ", ".join(map(lambda card: str(card), tmp))
                p_total = self.player.total()
                print(f"Your cards: {p}; {p_total}")
            elif q == "p":
                p_total = self.player.total()
                break
            else:
                print("Type 'p' or 'a'")
                self.process()

        while d_total <= 16:
            tmp = self.dealer.add_card(self.deck.get_card())
            d = ", ".join(map(lambda card: str(card), tmp))
            d_total = self.dealer.total()
            print(f"Dealer's cards: {d}; {d_total}")
            if self.blackjack(tmp, d_total):
                print("Suddenly, dealer has blackjack\nDEFEAT")
                self.play_again()

        self.conclusion(p_total, d_total)

    def blackjack(self, l, total):
        if len(l) == 2 and total == 21:
            return True
            # print("You are lucky!\nBLACKJACK!")
            # print("Suddenly, dealer has blackjack\nDEFEAT")

    def conclusion(self, p_total, d_total):
        m = 21
        if p_total < d_total <= m:
            print(p_total, d_total, p_total < d_total)
            print("Dealer has a better score\nDEFEAT")
        elif p_total > m:
            print("Too much\nDEFEAT")
        elif m >= p_total > d_total or ((m >= p_total > d_total) and (d_total > m)):
            print("WIN!")
        else:
            print("DRAW")
        self.play_again()

    def play_again(self):
        q = input("Play again? (y/n)\n")
        if q == "y":
            self.reset()
            self.start()
            self.process()
        elif q == 'n':
            exit(1)
        else:
            print("Type 'y' or 'n'")
            self.play_again()

    def reset(self):
        self.deck = Deck()
        self.player.hand = []
        self.dealer.hand = []
