from random import sample

class Card():
    ''' Draw a card from a 52-card deck. '''

    def __init__(self,owner='Player'):
        self.owner = owner
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cardnums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = [(c,s) for c in self.cardnums for s in self.suits]
        self.hand = []
        self.points = 0
        
    def draw(self,num_cards=1):
        ''' Draw a card. '''
        picks = sample(self.deck, num_cards)
        for pick in picks:
            print(pick[0] + ' of ' + pick[1])
            self.deck.remove(pick)
            self.hand.append(pick)

    def score(self):
        ''' Calculate score of hand. '''
        self.points = 0
        for card in self.hand:
            try:
                value = int(card[0])
            except ValueError:
                if card[0] == 'Ace':
                    value = 1
                else:
                    value = 10
            self.points += value
        return self.points

'''
c1 = Card()

print(c1.deck,len(c1.deck))

c1.draw(2)

print(c1.deck,len(c1.deck),c1.hand)
print(c1.hand[0][0])
'''