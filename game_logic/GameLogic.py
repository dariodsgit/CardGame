#Create the two players

from classes.Deck import Deck
from classes.Player import Player

player_one = Player()
player_two = Player()
deck_1 = Deck()
deck_2 = Deck()

def creatingPlayers():
    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        deck_1.addCard(new_deck.dealOne())
        deck_2.addCard(new_deck.dealOne())
    player_one = Player(deck_1,'Greg')
    player_two = Player(deck_2,'Teo')
    print(player_one.printPlayerDeck())
    print(player_two.printPlayerDeck())
