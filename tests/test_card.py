from blackjack.card import Card

def test_construction():
    card = Card('Hearts','Two')
    assert 'Hearts' == card.suit
    assert 'Two' == card.rank
    assert 2 == card.value
