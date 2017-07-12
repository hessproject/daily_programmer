class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self, suits, aces_high=True):
        self.cards = []

        if aces_high:
            card_values = range(2,15)
        else:
            card_values = range(1,14)

        for i in card_values:
            for suit in suits:
                self.cards.append(Card(i,suit))
        


    def deal_all_cards(self, list_of_players):
        pass
        #TODO: loop through players, dealing a card to each until deck is empty

    def shuffle(self):
        pass
        #TODO: randomize order of cards

    def print_deck(self):
        for card in self.cards:
            print(str(card.value) + ' of ' + card.suit)

class Player:
    def __init__(self, hand=[]):
        self.hand = hand
        self.field = []

    def play_card(self):
        pass
        #TODO: Take top card from hand and play face up on field

    def war(self):
        pass
        #TODO: Play 3 (or less) cards face down, then a face up card
        

    def add_to_bottom_of_hand(self):
        pass
        #TODO: Take cards from field and place at end of deck



def main():
    #Game logic here
    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    deck = Deck(suits)
    deck.print_deck() #for debugging

    #player_1 = Player()
    #player_2 = Player()

if __name__ == '__main__': main()