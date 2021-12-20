class Card:
    def __init__(self, rank, suit):
        #TODO: initialize the card class object by assigning two attributes
        try:
            assert rank in '2 3 4 5 6 7 8 9 T J Q K A'
        except:
            print("Invalid Rank")
        # assign rank as a private attribute to class object after checking input
        self.__rank = rank
        try:
            assert suit in 'H C D S'
        except:
            print("Invalid Suit")
        # assign suit as a private attribute to class object after checking input
        self.__suit = suit
	
	
    def get(self):
        #TODO: return the string representation of the card object
        return "%s%s" %(self.get_rank(), self.get_suit())
    
    
    def get_rank(self):
	#TODO: return the rank of the card object
        return self.__rank
    
    
    def get_suit(self):
        #TODO: return the suit of the card object
        return self.__suit
	    
    
    def __gt__(self, other):
        #TODO: compare a and b, return true if a larger than b
        return self.convert_rank(self.get_rank()) > self.convert_rank(other.get_rank())
	    
	    
    def __lt__(self, other):
        #TODO: compare a and b, return true if a less than b
        return self.convert_rank(self.get_rank()) < self.convert_rank(other.get_rank())
    
    
    def __eq__(self, other):
        #TODO: compare a and b, return true if a is equal to b
        return self.convert_rank(self.get_rank()) == self.convert_rank(other.get_rank())
    
    
    def convert_rank(self, target_rank):
        #TODO: convert rank of cards from string to integer
        rank_int = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, \
                    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_int[target_rank]
    
	    
    def __str__(self):
        #TODO: return the string representation of the card object
        return "%s%s" %(self.get_rank(), self.get_suit())	
