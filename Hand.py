class Hand:

    def __init__(self, first_card, second_card):
        self.value = 0
        self.cards = []
        self.aces = 0

        self.add_card(first_card)
        self.add_card(second_card)

    def add_card(self, card):
        if card.is_ace():
            self.aces += 1
            self.adjust_for_ace()
        else:
            self.value += card.value
            self.cards.append(card)

    def show_cards(self):
        print(f"Your cards are: ", end='')
        for card in self.cards:
            print(card, end=', ')
        print(f"with a value of {self.value}")

    def adjust_for_ace(self):
        if self.aces > 0:
            for i in range(0, self.aces):
                if self.value <= 10:
                    self.value += 11
                else:
                    self.value += 1