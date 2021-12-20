from Card import Card
from Player import Player
from Table import Table


def test_card():
    #Creates a card which is the Ace of Diamonds
    my_card = Card("A", "D")
	
    #tests get function
    assert my_card.get() == "AD", "Invalid card"
    #tests rank function
    assert my_card.get_rank() == "A", "Invalid rank"
    #tests suit function
    assert my_card.get_suit() == "D", "Invalid suit"
    
    #tests a rank convertion function
    assert my_card.convert_rank("A") == 14, "Invalid conversion"
    assert my_card.convert_rank("K") == 13, "Invalid conversion"
    assert my_card.convert_rank("Q") == 12, "Invalid conversion"
    assert my_card.convert_rank("J") == 11, "Invalid conversion"
    assert my_card.convert_rank("T") == 10, "Invalid conversion"
    assert my_card.convert_rank("9") == 9, "Invalid conversion"
    assert my_card.convert_rank("8") == 8, "Invalid conversion"
    assert my_card.convert_rank("7") == 7, "Invalid conversion"
    assert my_card.convert_rank("6") == 6, "Invalid conversion"
    assert my_card.convert_rank("5") == 5, "Invalid conversion"
    assert my_card.convert_rank("4") == 4, "Invalid conversion"
    assert my_card.convert_rank("3") == 3, "Invalid conversion"
    assert my_card.convert_rank("2") == 2, "Invalid conversion"
    
    #tests that the suit has no influence on comparison __eq__
    assert Card("A","D") == Card("A","S") == Card("A","H") == Card("A","C"), "Invalid comparison =="
    
    #tests rank comparison function _gt__
    assert Card("A","H") > Card("K", "H") > Card("2", "S"), "Invalid comparison >"
    
    #tests the __str__ function
    assert str(my_card) == "AD", "Invalid string"
    
    #returns True to sinalize that it has passed all tests	
    return True


def test_player():
    #TODO: checking for correct functionality of the Player class
    # creates a player object
    player_1 = Player()
    
    # tests add_chips function
    player_1.add_chips(100)
    assert player_1.get_chips() == 100, "Invalid Chips"
    player_1.add_chips(200)
    assert player_1.get_chips() == 300, "Invalid Chips"
    player_1.add_chips(200)
    assert player_1.get_chips() == 500, "Invalid Chips"
    
    # tests remove_chips function
    player_1.remove_chips(100)
    assert player_1.get_chips() == 400, "Invalid Chips"
    player_1.remove_chips(200)
    assert player_1.get_chips() == 200, "Invalid Chips"
    player_1.remove_chips(200)
    assert player_1.get_chips() == 0, "Invalid Chips"	

    # return True if passes all the tests
    return True


def test_table():
    #TODO: checking the correct functionality of the Table class
    table_1 = Table()
    
    # tests create_deck function and make_shoe function
    assert table_1.validate_deck(table_1.create_deck()) == True, "Invalid Deck"
    assert table_1.make_shoe().size() == 312, "Invalid Shoe"
    
    # tests set_bet function
    table_1.set_bet(100)
    assert table_1.get_bet() == 100, "Invalid Bets"
    table_1.set_bet(200)
    assert table_1.get_bet() == 200, "Invalid Bets"
    table_1.set_bet(300)
    assert table_1.get_bet() == 300, "Invalid Bets"
    
    table_1.set_shoe(table_1.make_shoe())
    # test deal_cards function
    player_card, dealer_card = table_1.deal_cards()
    assert type(player_card) == type(dealer_card), "Invalid Cards"
    # test resolve_round function
    result = table_1.resolve_round(player_card, dealer_card)
    assert result in [1, -1, 0], "Invalid Resolve"
    
    # return True if passes all the tests
    return True
