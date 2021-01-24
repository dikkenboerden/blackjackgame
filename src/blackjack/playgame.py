from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.card import Card



def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('how many chips would you like to bet?'))
        except:
            print('sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print('sorry you do not have enough chips, you have:{}'.format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s')
        if x[0].lower() == 'h':
            hit (deck, hand)
        elif x[0].lower() == 's':
            print("player stands dealer's turn")
            playing = False
        else:
            print("sorry I did no undestand enter h or s")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player,dealer,chips):
    print("Bust player")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("player wins Dealer busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Bust player looses, dealer wins")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH')

def play():
    playing = True

    while True:
        print('welcome to black jack')

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

                # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

                # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

                # Inform Player of their chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            playing = False
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    play()