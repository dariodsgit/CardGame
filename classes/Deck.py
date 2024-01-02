#instantiate a new deck
#create all 52 card object, hold as a list ofCard objects, shuffle a deck througha method random
#pop method from cards list 
import random

from Card import Card
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven':7,'Eight':8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen':12,
          'King': 13, 'Ace': 14}

class Deck:
  
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def __str__(self):
        elements_str = "\n".join(str(card) for card in self.all_cards)
        return f"MyClass with value: {elements_str}"
    
    def printCards(self):
        for card in self.all_cards:
            print(card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def dealOne(self):
        return self.all_cards.pop()