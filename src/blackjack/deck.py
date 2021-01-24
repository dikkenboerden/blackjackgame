from dataclasses import dataclass, field
import blackjack.config as myconfig
from blackjack.card import Card
from typing import List
import random as random

@dataclass
class Deck:
    _deck: List[Card] = field(default_factory=list, repr=False, init=False)

    def __post_init__(self):
        for suit in myconfig.suits:
            for rank in myconfig.ranks:
                self._deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' +deck_comp

    @property
    def deck(self) -> []:
        return self._deck

    def shuffle(self) -> []:
        return random.shuffle(self.deck)

    def deal(self) -> Card:
        return self.deck.pop(0)

if __name__ == '__main__':
    d = Deck()
    print(d)
