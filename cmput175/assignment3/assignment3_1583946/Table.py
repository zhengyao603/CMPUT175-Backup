from Card import Card
from random import shuffle
from Queue import Queue


class Table:
    def __init__(self):
        #TODO: initialize the Table class
        self.__player_card = None
        self.__dealer_card = None
        self.__discard = Queue(312)
        self.__shoe = None
        self.__bet = 0

    
    def resolve_round(self, player, dealer):
        #TODO: compare the cards of player and dealer, return 1 if player win, -1 if dealer win, 0 if tie
        if player > dealer:
            return 1
        elif player < dealer:
            return -1
        elif player == dealer:
            return 0
    
    
    def set_shoe(self, shoe):
        #TODO: takes a shoe as parameter and sets the shoe property
        self.__shoe = shoe
    
    
    def reset_shoe(self):
        #TODO: reset the shoe when it is less than 1/6 of the original shoe
        if self.__shoe.size() < 52:
            # dequeue all the cards from shoe and enqueue 156 cards to queue1 and 156 cards to queue2
            while self.__shoe.size() != 0:
                self.__discard.enqueue(self.__shoe.dequeue())
            queue_1 = Queue(156)
            queue_2 = Queue(156)
            game_shoe = Queue(312)
            list_1 = []
            for i in range(156):
                queue_1.enqueue(self.__discard.dequeue())
            for j in range(156):
                queue_2.enqueue(self.__discard.dequeue())
            # dequeue all the cards from queue1 and queue2, then append them into list1
            while not queue_1.isEmpty() and not queue_2.isEmpty():
                for k in range(26):
                    list_1.append(queue_1.dequeue())
                    list_1.append(queue_2.dequeue())
                    # shuffle the list before enqueuing those cards back to game shoe
                    shuffle(list_1)
                    while len(list_1) != 0:
                        game_shoe.enqueue(list_1.pop())
            # reset the game shoe
            self.set_shoe(game_shoe)
            
        
        
    def discard_cards(self, number):
        #TODO: discard certain amount numbers of cards from game shoe and add them into discard queue
        for i in range(number):
            self.__discard.enqueue(self.__shoe.dequeue())
            
            
    def deal_cards(self):
        #TODO: dequeue a card from the game shoe and return it as the card for player and dealer respectively
        self.__player_card = self.__shoe.dequeue()
        self.__dealer_card = self.__shoe.dequeue()
        return (self.__player_card, self.__dealer_card)

        
    def set_bet(self, bet):
        #TODO: takes a bet as parameter and sets the bet property
        self.__bet = bet
    
    
    def get_bet(self):
        #TODO: return the current bet
        return self.__bet
    
    
    def clear(self):
        #TODO: clears the current bets, adding player card and dealer card into discard queue
        self.__discard.enqueue(self.__player_card)
        self.__player_card = None
        self.__discard.enqueue(self.__dealer_card)
        self.__dealer_card = None
    
    
    def create_deck(self):
        #TODO: creates and returns a 52 card deck this deck should be a list of object of Card type
        deck = []
        for i in range(13):
            rank = i + 1
            if rank == 1:
                rank = 'A'
            elif rank == 10:
                rank = 'T'
            elif rank == 11:
                rank = 'J'
            elif rank == 12:
                rank = 'Q'
            elif rank == 13:
                rank = 'K'
            deck.append(Card(str(rank), 'D'))
            deck.append(Card(str(rank), 'C'))
            deck.append(Card(str(rank), 'H'))
            deck.append(Card(str(rank), 'S'))
        return deck


    def validate_deck(self, deck):
        #TODO: check if the input deck is valid, return true if it is valid
        count_of_rank = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, \
	                '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        for card in deck:
            count_of_rank[card.get_rank()] += 1
        for rank in count_of_rank.keys():
            assert count_of_rank[rank] == 4, "Invalid number of cards for rank %s" %(rank)
        return True
	

    def make_shoe(self):
        #TODO: create the game shoe, which is a queue contains 6 decks of card
        queue_1 = Queue(156)
        queue_2 = Queue(156)
        game_shoe = Queue(312)
        temp_list = []
        # create 6 decks or 52 cards
        for i in range(6):
            deck = self.create_deck()
            self.validate_deck(deck)
            # shuffle each deck before enqueuing them into two queues
            shuffle(deck)
            if i <= 2:
                for card in deck:
                    queue_1.enqueue(card)
            else:
                for card in deck:
                    queue_2.enqueue(card)
        # keep dequeuing card from two queues until they are empty
        while not queue_1.isEmpty() and not queue_2.isEmpty():
            # add half a deck into a list
            for j in range(26):
                temp_list.append(queue_1.dequeue())
                temp_list.append(queue_2.dequeue())
                # shuffle the list before enqueuing cards into game shoe
                shuffle(temp_list)
                while len(temp_list) != 0:
                    game_shoe.enqueue(temp_list.pop())
        return game_shoe	
