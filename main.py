from Deck import Deck
from Dealer import Dealer
from Player import Player

while True:
    print("Welcome to Blackjack!")

    # create the deck
    deck = Deck()
    deck.shuffle()

    # create the dealer, the player and deal cards
    dealer = Dealer(deck)
    player = Player(100)
    dealer.ask_for_bet(player)
    dealer.deal_cards(player)
    dealer.show_cards(player)

    # player's turn, choose if he hits or stands
    while dealer.hit_or_stand(player):
        player.hand.show_cards()
        if player.hand.value == 21:
            dealer.player_wins(player)
        if player.hand.value > 21:
            dealer.player_busts(player)
            break
    if not player.busted:
        print("Dealer's turn")
        while dealer.hand.value < 17:
            card = deck.get_card()
            dealer.hand.add_card(card)
            dealer.hand.show_cards()
            if dealer.hand.value > 21:
                dealer.dealer_busts(player)

    if not player.busted and not dealer.busted:
        if player.hand.value >= dealer.hand.value:
            dealer.player_wins(player)
        else:
            dealer.dealer_wins(player)
    elif player.busted:
        dealer.dealer_wins()

    player.show_balance()

    play_again = input("Do you want to play again? (yes/no)")
    if play_again == 'no':
        break

