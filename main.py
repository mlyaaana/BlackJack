# import random
#
# def create_deck(suit, num) -> []:
#     deck = []
#     for i in num:
#         for j in range(4):
#             temp = suit[j] + i
#             deck.append(temp)
#     random.shuffle(deck)
#     return deck
#
#
# def total_up(hand, d):
#     total = 0
#     for i in range(2, 11):
#         for card in hand:
#             if card in ["♥️A", "♦️A", "♣️A", "♠️A"]:
#                 if total >= 11:
#                     total += 1
#                 else:
#                     total += 11
#             else:
#                 if card in d[i]:
#                     total += i
#     return total
#
#
# def game(suit, num, d):
#     deck = create_deck(suit, num)
#     player_cards = []
#     dealer_cards = []
#
#     for i in range(2):
#         player_cards.append(deck[i])
#         deck.pop(i)
#     dealer_cards.append(deck[0])
#     deck.pop(0)
#     p_total = total_up(player_cards, d)
#     d_total = total_up(dealer_cards, d)
#     print(f"Your cards and total: {player_cards} {p_total}")
#     print(f"Dealer's cards and total: {dealer_cards} {d_total}")

# d = Deck()
# p = Player()
# print(d)
# p.add_card(d.get_card())
# c = p.add_card(d.get_card())
# print(", ".join(map(lambda card: str(card), c)))
# print(p.total())
# print(d)
from game import Game

MAX = 21

def intro():
    q = input("Hi! Do you want to start? (y/n)\n")

    if q == "y":
        return True
    elif q == "n":
        exit(1)
    else:
        print("Ty pidoras")
        intro()


if __name__ == '__main__':
    g = Game()
    intro()
    g.starting()
    g.choice()
