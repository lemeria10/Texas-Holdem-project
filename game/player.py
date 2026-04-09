import random
import time
class Player():
    def __init__(self,type="pc",cards=[],total_Amount_bet=0,name="",amount=0):
        self.name = name
        self.type = type
        self.cards = cards
        self.total_Amount_bet = total_Amount_bet
        self.amount= amount
 #human vs pc       

    def place_initial_bet(self):

        while True:
            amount = input(f"Enter the initial bet amount.current is ${self.amount}:")

            if amount.isdigit():
                n = int(amount)
                if n>0 and n<=self.amount:
                    self.amount=self.amount-n
                    return n 
                
                print("Invalid amount entered")
                print(f"amount must range from 1 to {self.amount}")
                print("Please try again.")
            else:
                print(f"enter a number between 1 and {self.amount} ")


    def auto_match_or_raise(self, amount):
        print("PC is thinking...")
        # Simulate thinking time
        time.sleep(2)
        to_do=random.randint(1,2)
        raise_amount=random.randint(10,250)

        if raise_amount>self.amount:
            to_do=1

        if to_do==1:
            if self.amount>amount:
                self.amount-amount
                
                print(f"Matching your action. Bet {amount}")
                return amount
            else:
                return "l"
                
                self.amount=self.amount-raise_amount
                print(f"I am going to raise by {raise_amount}")
                return raise_amount
    def update_amount_bet(self, amount):
         self.total_Amount_bet =self.total_Amount_bet+amount

    def reset_amount_bet(self):
             self.total_Amount_bet=0

               







        

