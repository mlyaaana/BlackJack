from card import Card


class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)
        return self.hand

    def total(self):
        total = 0
        for card in self.hand:
            total += int(card.points)
        return total
