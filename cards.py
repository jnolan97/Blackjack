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
        return (self.cards_dict)
    
    def assignType(self):
        kinds = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        final_dict = dict(zip(kinds, list(self.cards_dict.values())))
        # for k in self.cards_dict.keys():
        #     if self.cards_dict[int(k)] % 4 == 0:
        #         self.cards_dict[2] = self.card_dict.pop(k)
        print(final_dict)



# v1 of play function to run game
def play():
    jack = Blackjack({'0':0},0,0)
    while True:
        response = input("What do you want to do: play/exit: ")
        if response.lower() == "deal":
            jack.makeDeck()
            jack.assignType()
        if response.lower() == "exit":
            break
play()