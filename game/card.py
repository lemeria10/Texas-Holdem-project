class Card():
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITES = ['HEART', 'DIAMOND', 'CLUB', 'SPADE']
    def __init__(self, suite, rank):


        if not isinstance(suite,str):
            raise TypeError(f"Suite expected to be a string, got {type(suite).__name__}")
        if not isinstance(rank,str):
            raise TypeError(f"Rank expected to be a string, got {type(rank).__name__}")
        
        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank not in rank list {Card.RANKS}")
        if suiteUpper in Card.SUITES:
            pass
        else:
            raise TypeError(f"Added suite not in suite list {Card.SUITES}")
        
        self.suite = suiteUpper
        self.rank = rankUpper

    def printCard(self):
        print("Rank", self.rank)
        print("Suite", self.suite)


if __name__ == "__main__":
    card1=Card(suite="Heart", rank="A")
    card1.printCard()

    card2=Card(suite="Spade", rank="10")
    card2.printCard()