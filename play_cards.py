#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck
from jokerdeck import EuchreDeck

d1 = CardDeck("Thelma")  #  create INSTANCE of CardDeck CLASS

d2 = CardDeck("Louise")

print(d1)
print(d2)

d1.shuffle()
print(d1.cards)

for i in range(5):
    x = d1.deal()
    print("x:", x)

print(d1.dealer)

for name in "Teddy", 5, ['a', 'b'], 'Joe':
    try:
        d1.dealer = name
    except TypeError as err:
        print(err)
    else:
        print(d1.dealer)

j1 = JokerDeck('Benny')

print(j1)
j1.shuffle()
print(j1.deal())
print(j1.cards)

e1 = EuchreDeck('Mitchell')

print(e1.cards)

print(len(d1), len(j1), len(e1))
