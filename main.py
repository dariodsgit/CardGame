import sys
sys.path.insert(0, '/Users/dario/Desktop/Python Course/CardGame/CardGame/classes')
from classes.Card import Card
from classes.Deck import Deck

two_hearts = Card("Hearts", "Two")
#print(two_hearts)

new_deck = Deck()
#new_deck.printCards()
print(new_deck)
new_deck.shuffle()
print(new_deck)
new_deck.dealOne()
print(len(new_deck.all_cards))
