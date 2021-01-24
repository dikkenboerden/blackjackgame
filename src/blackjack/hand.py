from dataclasses import dataclass, field
from blackjack.card import Card
from blackjack.deck import Deck

@dataclass
class Hand:
    __cards : list = field(default_factory=list, init=[])
    __value : int = 0
    __aces : int = 0

    def add_card(self,card):
        self.__cards.append(card)
        self.__value += card.value

        # track our aces
        if card.rank == 'Ace':
            self.__aces += 1

    def adjust_for_ace(self):
        # if total value > 21 and I still have an ace
        # than change my ace to be a 1 instead of an 11
        while self.__value > 21 and self.__aces:
            self.__value -= 10
            self.__aces -= 1

    @property
    def value(self) -> int:
        return self.__value

    @property
    def cards(self) -> []:
        return self.__cards

if __name__ == '__main__':
    deck = Deck()
    player = Hand()

    deck.shuffle()
    pulled_card = deck.deal()
    print(pulled_card)
    player.add_card(pulled_card)
    print(player.value)
    player.add_card(deck.deal())
    print(player.value)