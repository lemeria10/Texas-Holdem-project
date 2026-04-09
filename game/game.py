from player import Player
from deck import Deck
class Game():
    def __init__(self):
        self.main_pot = 0
        self.current_pot = 0
        deck=Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards=[deck.give_card(), deck.give_card()]
        pc_cards=[deck.give_card(), deck.give_card()]
        self.human = Player(type="human", cards=human_cards,total_Amount_bet=0, name="Nick", amount=2000)
        self.pc = Player(type="pc", cards=pc_cards,total_Amount_bet=0, name="Nick", amount=2000)

        self.deck = deck
        self._turn=self.human
    @property
    def turn(self):
        return self._turn
    @turn.setter
    def turn(self, player):

        if isinstance(player, Player):
            self._turn = player

        else:
            raise ValueError("Turn must be set to a Player instance")   
   

        

if __name__ == "__main__":
    game=Game()
    game.deck.printDeck()
    print("This is the deck:")
    print("This is the pc cards:")
    game.pc.cards[0].printCard()
    game.pc.cards[1].printCard()
    print("This is the deck:")
    print("This is the human cards:")
    game.human.cards[0].printCard()
    game.human.cards[1].printCard()

