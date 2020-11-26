class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self) -> str:
        return self.rank + " of " + self.suit

    values = {"Two": }
two_hearts = Card("Hearts", "Two")
print(two_hearts)