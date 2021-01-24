from dataclasses import dataclass, field

@dataclass
class Chips:
    total: int = 100
    bet : int = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet