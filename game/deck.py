from card import Card
import random

class Deck():
    def __init__(self):
        ranks=Card.RANKS
        suites=Card.SUITES
        deck=[]#datatype in an array

        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite,rank=rank)
                deck.append(card)
                print(len(deck))
                print("rank", rank)
                print("suite", suite)
                print("-"*10)

        self.deck = deck

    def shuffle(self):
        newDeck =[]
        deck=self.deck

        while True:
            if len(deck)==1:
                card=deck[0]
                newDeck.append(card)
                break
            n=random.randint(0, len(deck)-1)
            card=deck[n]
            deck.pop(n)
            newDeck.append(card)
        print("new deck length:", len(newDeck))
        print("old deck length:", len(deck))
        for card in newDeck:
            card.printCard()
            print("----")
        self.deck = newDeck

        
    def printDeck(self):
        deck=self.deck
        print("Deck length:", len(deck))
        print("-----------")
        for card in deck:
            
            card.printCard()
            print("-----------")

    
    def burn_Card(self):

        # take the top card put it below the deck
        #self.deck
        print("before burn card")
        self.printDeck()
        print("after burn card")
        topCard=self.deck[0]
        self.deck.pop(0)
        self.deck.append(topCard)
        self.printDeck()
        

    def give_card(self):
        # add a card to the end of the deck
        topCard=self.deck[0]
        self.deck.pop(0)
        return topCard
        
        
if __name__ == "__main__":
    d1=Deck()
    d1.shuffle()
    d1.burn_Card()
    card = d1.give_card()
    print("given card:")
    card.printCard()
    d1.printDeck()