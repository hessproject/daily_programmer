from random import shuffle
from itertools import cycle
from abc import ABCMeta, abstractmethod
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

    def war(self):
        pass
        #TODO: Play 3 (or less) cards face down, then a face up card


class Game(metaclass=ABCMeta):
    @abstractmethod
    def play(self):
        raise NotImplementedError()


class WarGame(Game):
    def __init__(self):
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        self.deck = Deck(suits)
        self.players = create_players(2)

    def check_for_win(self):
        player1 = self.players[0]
        player2 = self.players[1]
        if player1.hand and not player2.hand:
            return 1
        elif not player1.hand and player2.hand:
            return 2
        else:
            return 0

    def play(self):
        self.deck.shuffle()

        for player in cycle(self.players):
            if not self.deck.cards:
                break
            card = self.deck.deal_card()
            player.hand.append(card)

        while True:
            if self.check_for_win() == 0:
                self.players[0].play_card()
            else:
                print("Player " + str(self.check_for_win()) + ' wins!')
                break


def create_players(number_of_players):
    players = []
    for i in range(number_of_players):
        players.append(Player(i + 1))
    return players

def create_game(type_of_game=None):
    if type_of_game == 'war':
        game = WarGame()
    else: 
        game = None
    return game

def main():
    game = create_game('war')

    if game:
        game.play()
    else: 
        print('No Game Selected')


if __name__ == '__main__': main()