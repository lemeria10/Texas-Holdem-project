class Card:
    def __init__(self, suite, rank):
        acceptedRanks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        acceptedSuits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']

        if not isinstance(suite,str):
            raise TypeError(f"Suite expected to be a string, got {type(suite).__name__}")
        if not isinstance(rank,str):
            raise TypeError(f"Rank expected to be a string, got {type(rank).__name__}")
        
        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        if rankUpper in acceptedRanks:
            pass
        else:
            raise TypeError(f"Added rank not in rank list {acceptedRanks}")
        if suiteUpper in acceptedSuits:
            pass
        else:
            raise TypeError(f"Added suite not in suite list {acceptedSuits}")
        
        self.suite = suiteUpper
        self.rank = rankUpper

    def printCard(self):
        print("Rank", self.rank)
        print("Suite", self.suite)


if __name__ == "__main__":
    card1=Card(suite="Hearts", rank="A")
    card1.printCard()

    card2=Card(suite="Spades", rank="10")
    card2.printCard()