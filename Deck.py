from Card import Card
import random


class Deck:

    cards_number = [
        ['Two', 2],
        ['Three', 3],
        ['Four', 4],
        ['Five', 5],
        ['Six', 6],
        ['Seven', 7],
        ['Eight', 8],
        ['Nine', 9],
        ['Ten', 10],
        ['Jack', 10],
        ['Queen', 10],
        ['King', 10],
        ['Ace', 11]
    ]
    colors = ('Hearts', 'Tiles', 'Clovers', 'Pikes')
    cards = []

    def __init__(self):
        for color in self.colors:
            for name, value in self.cards_number:
                self.cards.append(Card(name, color, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()
