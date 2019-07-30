class Player:

    def __init__(self, balance):
        self.balance = balance
        self.hand = 0
        self.bet_value = 0
        self.busted = False
        self.won = False

    def bet(self, amount):
        if amount <= self.balance:
            self.bet_value = amount
            return True
        else:
            print("Not enough money")
            return False

    def add_hand(self, hand):
        self.hand = hand

    def win_bet(self):
        self.balance += self.bet_value

    def lose_bet(self):
        self.balance -= self.bet_value

    def show_balance(self):
        print(f"You have {self.balance} credits now")

