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
        for i,v in enumerate(suites):
            self.cards_dict[i] = v
       # print(self.cards_dict)
    
    def assignType(self):
        kinds = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        test = len(self.cards_dict.keys())
        print(test)
        final_dict = {}
        count = 0
        while kinds[count] != 'Ace' and self.cards_dict[count] != 'clubs':
            final_dict[kinds[count]] = self.cards_dict[count]
            count += 1

        # for k in range(len(self.cards_dict.keys())):
        #     final_dict = dict(zip(kinds[k], list(self.cards_dict.values())))
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