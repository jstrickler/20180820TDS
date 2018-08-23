#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        self._cards.append("Joker-One")
        self._cards.append("Joker-Two")

class EuchreDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for rank in range(2,9):
            for suit in self.SUITS:
                self._cards.remove('{}-{}'.format(rank, suit))
