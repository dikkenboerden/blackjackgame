from dataclasses import dataclass, field
import blackjack.config as myconfig

@dataclass()
class Card:
    suit: str
    rank: str

    _value: int = field(repr=False, init=False)

    def __post_init__(self):
        self.value = self.rank

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self,rank) -> None:
        self._value = myconfig.values[rank]

