class Player:
    def __init__(self):
        #implement the properties here
        #TODO: initialize the Player class object(initialize chips attribute)
        self.__chips = 0
	
	
    def add_chips(self, chips):
        #TODO: takes the number of chips to add and increase the number of chips by that amount
        try:
            assert int(chips) > 0
        except:
            print("Invalid Input")
        else:
            self.__chips += chips
	    
	    
    def remove_chips(self, chips):
        #TODO: takes the number of chips to be taken from the player and decreases the number of chips by that amount
        try:
            assert int(chips) > 0
        except:
            print("Invalid Input")
        else:
            self.__chips -= chips
    
    
    def get_chips(self):
        #TODO: return the amount of chips that the player has
        return self.__chips
