from dealer import Dealer
from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def starting(self):
        self.player.add_card(self.deck.get_card())
        tmp1 = self.player.add_card(self.deck.get_card())
        p = ", ".join(map(lambda card: str(card), tmp1))

        tmp2 = self.dealer.add_card(self.deck.get_card())
        d = ", ".join(map(lambda card: str(card), tmp2))

        print(f"Your cards: {p}")
        print(f"Points: {self.player.total()}")
        print('')
        print(f"Dealer's cards: {d}")
        print(f"Points: {self.dealer.total()}")

    def choice(self):
        p_total = 0
        d_total = 0
        mx = 21
        while p_total < mx:
            q = input("Pass or add one? (p/a)\n")
            if q == "a":
                tmp1 = self.player.add_card(self.deck.get_card())
                p = ", ".join(map(lambda card: str(card), tmp1))
                p_total = self.player.total()
                print(f"Your cards: {p}")
                print(f"Points: {p_total}")
            elif q == "p":
                break
            else:
                print("Ty pidoras")

        while d_total <= 16:
            tmp = self.dealer.add_card(self.deck.get_card())
            p = ", ".join(map(lambda card: str(card), tmp))
            d_total = self.dealer.total()
            print(f"Dealer's cards: {p}")
            print(f"Points: {d_total}")
