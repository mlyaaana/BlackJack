import functools

from card import Card


class Player:
    m = 21
    aces = ["♥️", "♦️", "♣️", "♠️"]

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)
        return self.hand

    # def total(self):
    #     # return functools.reduce(lambda l, r: l + r.points, self.hand)
    #     total = 0
    #     for card in self.hand:
    #         total += int(card.points)
    #     return total

    def total_up(self):
        def total():
            amount = 0
            for c in self.hand:
                amount += int(c.points)
            return amount

        t = total()
        for card in self.hand:
            if card.rank == "A":
                temp = t + 10
                if temp <= self.m:
                    card.points = 11
                    return total()
                else:
                    return total()
        return t
