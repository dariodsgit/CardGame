#Create the two players

from classes.Deck import Deck
from classes.Player import Player

class GameLogic:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.deck_1 = Deck()
        self.deck_2 = Deck()
        self.creatingPlayers()

    def creatingPlayers(self):
        new_deck = Deck()
        new_deck.shuffle()

        for x in range(26):
            self.deck_1.addCard(new_deck.dealOne())
            self.deck_2.addCard(new_deck.dealOne())
        
        self.player_one = Player(self.deck_1, 'Greg')
        self.player_two = Player(self.deck_2, 'Teo')
        print(self.player_one.printPlayerDeck())
        print(self.player_two.printPlayerDeck())
