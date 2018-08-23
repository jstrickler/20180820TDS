#!/usr/bin/env python
import random


class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        print("Dealer is:", dealer)
        self._make_deck()
        self.dealer = dealer
        # return self

    def _make_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                card = '{}-{}'.format(r, s)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()


    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):   # property getter
        return self._dealer

    # dealer = property(dealer)
    @dealer.setter
    def dealer(self, value):  # property setter
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    def __len__(self):
        return len(self._cards)
