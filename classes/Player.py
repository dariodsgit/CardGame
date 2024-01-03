#Class used to hold cards and should be able to add or remove cards

class Player:
    
    def __init__(self,name):
        self.deck = []
        self.name = name
    #    for card in cards:
    #      self.deck.append(card)
    
    def printPlayerDeck(self):
        print(len(self.deck))
        for card in self.deck:
            print(card)
            
            
    def removeCard(self):
        try:
            return self.deck.pop(0)
        except IndexError:
            print("Il mazzo è vuoto.")
    
    def addCard(self,cards):
        #list of multiple cards
        if type(cards) == type([]):
            self.deck.extend(cards)
            #one single card
        else:
            self.deck.append(cards)
        
    def __str__(self):
        return f'Player {self.name}: has{len(self.deck)} cards.'