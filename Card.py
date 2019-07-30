class Card:

    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.name} of {self.color}"

    def is_ace(self):
        return self.name == 'Ace'

