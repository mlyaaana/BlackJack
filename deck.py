import random
from itertools import product

from card import Card


class Deck:
    suits = ["♥️", "♦️", "♣️", "♠️"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.deck = self.__create_deck()

    def __create_deck(self):
        deck = []
        for suit, rank in product(self.suits, self.ranks):
            if rank == "A":
                points = 1
            elif rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                points = int(rank)
            else:
                points = 10
            c = Card(suit=suit, rank=rank, points=points)
            deck.append(c)
        random.shuffle(deck)
        return deck

    def get_card(self):
        return self.deck.pop(0)

    def __str__(self):
        deck = []
        for i in self.deck:
            deck.append(str(i))
        return ", ".join(deck)
