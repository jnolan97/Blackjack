import random
class Blackjack():
    def __init__(self,cards_dict,dealer,player):
        self.cards_dict = cards_dict
        self.dealer = dealer
        self.player = player
    
    # Constructs dictionary of cards with suite and number representing kind
    def makeDeck(self):
        self.cards_dict = {}
        suites = ['hearts','diamonds','spades','clubs']
        for i,v in enumerate(suites*13):
            self.cards_dict[i] = v
       # print(self.cards_dict)
        print (self.cards_dict)
    
    # def assignType(self):
    #     for k in self.cards_dict.keys():
    #         if k % 4 == 0:
    #             self.cards_dict[2] = self.card_dict.pop(k)
    #     print(self.cards_dict)



# v1 of play function to run game
def play():
    jack = Blackjack({'0':0},0,0)
    while True:
        response = input("What do you want to do: play/exit: ")
        if response.lower() == "deal":
            jack.makeDeck()
            # jack.assignType()
        if response.lower() == "exit":
            break
play()