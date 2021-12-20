from Player import Player
from Table import Table


def main():
    #implement the game loop here
    #TODO: the main loop of the game, respond to user input
    player = Player()
    table = Table()
    # statistics need to be recorded
    totalhand = 0
    war = 0
    win = 0
    profit = 0
    totalbet = 0
    table.set_shoe(table.make_shoe())
    print("Welcome to Casino War")
    
    while True:
        # check if the table need to be reset
        table.reset_shoe()
        print("")
        print("You currently have %d chips." %(player.get_chips()))
        print("What would you like to do?")
        print("")
        print("Play(P)")
        print("Buy chips(B)")
        user_input = input("Quit(Q): ")
        
        # if the player wants to buy chips, the number should between 1 and 1000
        if user_input == 'b' or user_input == 'B':
            amount = int(input("How many chips would you like to buy?(1-1000): "))
            if 1 <= amount <= 1000:
                player.add_chips(amount)
            # otherwise the program will display error message and return to the beginning
            else:
                print("Invalid transaction, a number between 1 and 1000 should be inserted.")
                print("Returning to main menu.")
            continue
        
        # if the player wants to play
        elif user_input == 'p' or user_input == 'P':
            print("Place your bet!")
            # the amount of bets must be even and between 2 to 100
            amount = int(input("The bet should be an even number 2-100: "))
            if amount > 100:
                print("Bet is too large.")
                continue
            elif amount < 2:
                print("Bet is too small.")
                continue
            elif amount > player.get_chips():
                print("No enough chips.")
                continue
            elif amount % 2 != 0:
                print("Bet is odd, should be even.")
                continue
            # if the input is correct, the amount will be the bet and the player
            # will lose that amount chips
            else:
                table.set_bet(amount)
                player.remove_chips(amount)
                totalbet += amount
                profit -= amount
            # the shoe will burn one card before dealing cards
            totalhand += 1
            if totalhand == 1:
                print("First hand of the shoe, burning one card.")
                table.discard_cards(1)
            print("No more bets!")
            player_card, dealer_card = table.deal_cards()
            print("Player shows %s, Dealer shows %s" %(player_card, dealer_card))
            
            # if player wins, he/she can get twice of the bet
            if table.resolve_round(player_card, dealer_card) == 1:
                win += 1
                print("Player wins!")
                player.add_chips(amount * 2)
                profit += amount * 2
                table.set_bet(0)
                table.clear()
            # if dealer wins, player will not get anything
            elif table.resolve_round(player_card, dealer_card) == -1:
                print("Dealer wins!")
                table.set_bet(0)
                table.clear()
            # if there is draw, player choose if he/she want to go to war
            elif table.resolve_round(player_card, dealer_card) == 0:
                war += 1
                table.clear()
                while True:
                    if_war = input("War!!! Would you like to go to war(W) or surrender(S)?" )
                    
                    # if the player chose to go to war
                    if if_war == 'W' or if_war == 'w':
                        print("We are going to war!!! You doubled up your bet.")
                        # if player's chips is not enough for war, player will be asked to buy chips
                        if player.get_chips() < amount:
                            while True:
                                # player must ensure the amount player tries to buy is sufficient for war
                                buy_chips = int(input("No enough chips, how many chips would you like to buy?(1-1000): "))
                                if amount <= buy_chips <= 1000:
                                    player.add_chips(buy_chips)
                                    break
                                else:
                                    print("Invalid Transactions. Please ensure your chips is enough for war")
                                    continue
                        table.set_bet(amount * 2)
                        totalbet += amount
                        player.remove_chips(amount)
                        profit -= amount
                        # burn 3 cards from the game shoe
                        print("Burning three cards.")
                        table.discard_cards(3)
                        print("")
                        player_card, dealer_card = table.deal_cards()
                        print("Player shows %s, Dealer shows %s" %(player_card, dealer_card))
                        # if the dealer wins, player lose all the bets
                        if table.resolve_round(player_card, dealer_card) == -1:
                            print("Dealer wins!")
                            table.set_bet(0)
                            table.clear()
                        # if player wins or there is a draw, player wins twice of the original bets
                        else:
                            win += 1
                            print("Player wins!")
                            player.add_chips(amount * 2)
                            profit += amount * 2
                            table.set_bet(0)
                            table.clear()
                        break
                    
                    # if the player chose to surrender, player gets back half of the bets
                    elif if_war == 'S' or if_war == 's':
                        print("Player surrender.")
                        player.add_chips(amount // 2)
                        profit += amount // 2
                        table.set_bet(0)
                        break
                    
                    else:
                        print("Invalid input.")
                        continue
        
        # if the player wants to quit, quit the program and prints all the statistics
        elif user_input == 'q' or user_input == 'Q':
            print("Played %d hands." %(totalhand))
            print("From these hands, %d were war hands" %(war))
            # if the player at least play one hand
            if totalhand != 0:
                print("The average bet was %.3f chips" %(totalbet / totalhand))
                print("The average profit of the session was %.3f" %(profit / totalhand))
                win_percentage = 100 * (win / totalhand)
                print("Player won %d out of %d hands, or %.3f%%" %(win, totalhand, win_percentage))
            # if the player quit the game without playing any hand
            else:
                print("The average bet was %.3f chips" %(0))
                print("The average profit of the session was %.3f" %(0))
                print("Player won %d out of %d hands, or %.3f%%" %(win, totalhand, 0))
            print("Goodbye")
            break



class save_game_state:
    # TODO: defined class which contains attributes that can be used for storing game state for auto_play function
    def __init__(self):
        # initialize the class instance by assigning attributes
        self.table = Table()
        self.player = Player()
        self.totalhand = 0
        self.war = 0
        self.win = 0
        self.profit = 0
        self.totalbet = 0
    def reset(self):
        # reset all the attributes of the class
        self.table = Table()
        self.player = Player()
        self.totalhand = 0
        self.war = 0
        self.win = 0
        self.profit = 0
        self.totalbet = 0

game = save_game_state()
# set the table
game.table.set_shoe(game.table.make_shoe())


def auto_play(action, second_parameter):
    #TODO: This function does NOT ask for any user input nor prints any output, 
    # it simply resolves the game as if an user was inputting the commands.
    
    if action == 'p' or action == 'P':
        # if the amount of bets is valid and the player have enough chips to set the bet
        if type(second_parameter) == int and 2 <= second_parameter <= 100 and \
           second_parameter % 2 == 0 and game.player.get_chips() >= second_parameter:
            bets = second_parameter
            # set the bets
            game.table.set_bet(bets)
            game.player.remove_chips(bets)
            game.totalbet += bets
            game.profit -= bets            
            game.totalhand += 1
            # if it is the first hand, the first card should be burn
            if game.totalhand == 1:
                game.table.discard_cards(1)
            # deal cards to player and dealer respectively
            player_card, dealer_card = game.table.deal_cards()
            
            # if player wins, he/she can get twice of the bet
            if game.table.resolve_round(player_card, dealer_card) == 1:
                game.win += 1
                game.player.add_chips(bets * 2)
                game.profit += bets * 2
                game.table.set_bet(0)
                game.table.clear()
            # if dealer wins, player will not get anything
            elif game.table.resolve_round(player_card, dealer_card) == -1:
                game.table.set_bet(0)
                game.table.clear()
            # if there is a draw
            elif game.table.resolve_round(player_card, dealer_card) == 0:
                game.war += 1
                game.table.clear()
                # if the player does not have enough chips to double the bets, player surrender automatically
                if game.player.get_chips() < bets:
                    game.player.add_chips(bets // 2)
                    game.profit += bets // 2
                    game.table.set_bet(0)
                # otherwise, player goes to war automatically
                else:
                    game.table.set_bet(bets * 2)
                    game.totalbet += bets
                    game.player.remove_chips(bets)
                    game.profit -= bets
                    # burn 3 cards from the game shoe
                    game.table.discard_cards(3)
                    # deal cards to player and dealer respectively
                    player_card, dealer_card = game.table.deal_cards()
                    
                    # if the dealer wins, player lose all the bets
                    if game.table.resolve_round(player_card, dealer_card) == -1:
                        game.table.set_bet(0)
                        game.table.clear()
                    # if player wins or there is a draw, player wins twice of the original bets
                    else:
                        game.win += 1
                        game.player.add_chips(bets * 2)
                        game.profit += bets * 2
                        game.table.set_bet(0)
                        game.table.clear()
            # check if the game shoe need to be reset
            game.table.reset_shoe()
            # return total chips of player
            return game.player.get_chips()
        # return false if the function is not executing
        else:
            return False
    
    elif action == 'b' or action == 'B':
        # if the action is buy and second parameter is valid
        if type(second_parameter) == int and 1 <= second_parameter <= 1000:
            chips = second_parameter
            # add chips to player
            game.player.add_chips(chips)
            return True
        # return false if the function is not executing
        else:
            return False
    
    elif action == 'q' or action == 'Q':
        # if the user wants to quit and at least one hand is played, return statistics
        if game.totalhand != 0:
            # calculate and record the necessary statistics
            play_count = game.totalhand
            war_count = game.war
            average_bet = game.totalbet / game.totalhand
            average_profit = game.profit / game.totalhand
            win_count = game.win
            win_percentage = game.win / game.totalhand
            # reset the game status
            game.reset()
            game.table.set_shoe(game.table.make_shoe())
            return [play_count, war_count, average_bet, average_profit, win_count, win_percentage]
        # if no hand was played
        else:
            # record the necessary statistics
            play_count = game.totalhand
            war_count = game.war
            average_bet = 0
            average_profit = 0
            win_count = game.win
            win_percentage = 0           
            return [play_count, war_count, average_bet, average_profit, win_count, win_percentage]
    
    else:
        return -1



if __name__ == "__main__":
    main()
