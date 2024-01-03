import sys
sys.path.insert(0, '/Users/dario/Desktop/Python Course/CardGame/CardGame/classes')
from classes.Card import Card
from classes.Deck import Deck
from classes.Player import Player

two_hearts = Card("Hearts", "Two")
#print(two_hearts)

new_deck = Deck()
#new_deck.printCards()
print(new_deck)
new_deck.shuffle()
print(new_deck)
print(len(new_deck.all_cards))

new_player = Player(new_deck.all_cards)
new_player.addCard(two_hearts)
new_player.printPlayerDeck()
print("REMOVING")
new_player.removeCard()
new_player.printPlayerDeck()