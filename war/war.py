from random import shuffle
from itertools import cycle
from pprint import pprint as pp

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

    def deal_card(self):
        return self.cards.pop()
            
    def shuffle(self):
        shuffle(self.cards)

    def deck_length(self):
        return len(self.cards)


class Player:
    def __init__(self, player_number, hand=None):
        self.player_number = player_number
        if hand is None:
            self.hand = []
        else:
            self.hand = hand
        self.field = []

    def get_hand(self):
        return self.hand

    def play_card(self):
        return self.hand.pop()
        #TODO: Take top card from hand and play face up on field

    def war(self):
        pass
        #TODO: Play 3 (or less) cards face down, then a face up card


def create_players(number_of_players):
    players = []
    for i in range(number_of_players):
        players.append(Player(i))

    return players

def main():

    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    #initialize and shuffle standard 52 card deck
    deck = Deck(suits)
    deck.shuffle()
 
    #initialize players, and deal them hands from deck
    players = create_players(2)

    #Deal cards to players until deck is empty    
    for player in cycle(players):
        if not deck.cards:
            break
        card = deck.deal_card()
        player.hand.append(card)

    for player in players:
        print(len(player.hand))
        pp(player.get_hand())


if __name__ == '__main__': main()