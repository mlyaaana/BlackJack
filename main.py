from game import Game


def intro():
    q = input("Hi! Do you want to start? (y/n)\n")

    if q == "y":
        return True
    elif q == "n":
        exit(1)
    else:
        print("Type 'y' or 'n'")
        intro()


if __name__ == '__main__':
    intro()
    g = Game()
    g.start()
    g.process()
