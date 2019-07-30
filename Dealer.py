from Hand import Hand


class Dealer:

    def __init__(self, deck):
        self.deck = deck
        self.hand = 0
        self.busted = False

    def ask_for_bet(self, player):
        while True:
            bet_value = int(input("How much you want to bet?"))
            if player.bet(bet_value):
                break
        return bet_value

    def deal_cards(self, player):
        player_hand = self.__create_hand()
        player.add_hand(player_hand)

        dealer_hand = self.__create_hand()
        self.hand = dealer_hand

    def __create_hand(self):
        first_card = self.deck.get_card()
        second_card = self.deck.get_card()
        return Hand(first_card, second_card)

    def show_cards(self, player):
        player.hand.show_cards()

        print(f"Dealer card is {self.hand.cards[0]} with a value of {self.hand.cards[0].value}")

    def hit_or_stand(self, player):
        result = input("Hit or stand? (hit/stand)")

        if result == 'hit':
            card = self.deck.get_card()
            player.hand.add_card(card)
            return True
        elif result == 'stand':
            return False

    def player_busts(self, player):
        player.lose_bet()
        player.busted = True
        print("You busted!")

    def dealer_busts(self, player):
        player.win_bet()
        player.won = True
        self.busted = True
        print("Dealer busted!")

    def player_wins(self,player):
        player.win_bet()
        player.won = True
        print("You win!")

    def dealer_wins(self, player):
        player.lose_bet()
        print("Dealer win!")
