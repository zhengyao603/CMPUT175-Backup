from reversi import *

def main():
    while True:
        reversi_game = Reversi()
        print("Starting new game!")
        print("Black goes first, then white")
        colour = input("Enter 'b' to choose to play black, 'w' to choose white: ")
        # set the colour for player and computer
        if colour == 'w' or colour == 'b':
            reversi_game.setPlayerColour(colour)
        else:
            print("Invalid colour: Invalid input")
            continue
        # let the player decide whether he/she wants an easy or a hard computer
        difficulty = input("Enter '1' to choose easy computer opponent, '2' for hard computer opponent: ")
        if difficulty != '1' and difficulty != '2':
            print("Invalid computer opponent: Invalid input")
            continue
        
        
        # display the gameboard
        reversi_game.displayBoard()
        # if the player choses white as his/her colour
        if reversi_game.playerColour == reversi_game.WHITE:
            while True:
                # if the game is over
                game_over = False
                # if the player wants to quit game
                quit_game = False
                # game will begin and computer will have the first move
                reversi_game.COUNTER = 'c'
                game_over = reversi_game.isGameOver()
                if game_over == True:
                    print("Game Over!")
                    reversi_game.displayBoard()
                    break                
                if difficulty == '1':
                    easycomputer_move = reversi_game.makeMoveNaive()
                    print("Computer making move:", easycomputer_move)
                elif difficulty == '2':
                    hardcomputer_move = reversi_game.makeMoveSmart()
                    print("Computer making move:", hardcomputer_move)
                # display the gameboard after computer making move
                reversi_game.displayBoard()
                
                print("Enter 2 numbers from 0-7 separated by a space to make a move,")
                print("  where the first number is the row and the second number is the column")
                print("Enter 'q' to quit.")                
                while True:
                    reversi_game.COUNTER = 'p'
                    game_over = reversi_game.isGameOver()
                    if game_over == True:
                        print("Game Over!")
                        break                    
                    player_input = input("Enter move: ")
                    # player can quit the game by pressing 'q'                
                    if player_input == 'q':
                        quit_game = True
                        print("Game Over!")
                        break                  
                    # if the player enter invalid position, there is a chance for re-entering
                    try:
                        if int(player_input.split()[0]) < 0 or int(player_input.split()[1]) < 0:
                            print("Invalid position: out of bound.")
                            continue
                        elif reversi_game.gameBoard[int(player_input.split()[0]) + 1].split()[int(player_input.split()[1]) + 1] != reversi_game.EMPTY:
                            print("Invalid position: occupied by another piece")
                            continue
                        else:
                            # if the position is valid, then player can make the move
                            if reversi_game.isPositionValid([int(player_input.split()[0]) + 1, int(player_input.split()[1]) + 1], reversi_game.playerColour) == True:
                                reversi_game.makeMovePlayer([int(player_input.split()[0]) + 1, int(player_input.split()[1]) + 1])
                                break
                            else:
                                print("Invalid position: piece doesn't surround line of opponent pieces.")
                                continue
                    except:
                        print("Invalid position: Invalid Input")
                        continue
                # display the gameboard after player making the move
                reversi_game.displayBoard()
                if quit_game == True or game_over == True:
                    break
            
        
        # if the player choses black as his/her colour
        elif reversi_game.playerColour == reversi_game.BLACK:
            print("Enter 2 numbers from 0-7 separated by a space to make a move,")
            print("  where the first number is the row and the second number is the column")
            print("Enter 'q' to quit.")            
            while True:
                # if the game is over
                game_over = False
                # if the player wants to quit the game
                quit_game = False
                # player will make the first move
                while True:
                    reversi_game.COUNTER = 'p'
                    game_over = reversi_game.isGameOver()
                    if game_over == True:
                        print("Game Over!")
                        break                    
                    player_input = input("Enter move: ")
                    if player_input == 'q':
                        quit_game = True
                        print("Game Over!")
                        break
                    try:
                        if int(player_input.split()[0]) < 0 or int(player_input.split()[1]) < 0:
                            print("Invalid position: out of bound.")
                            continue
                        elif reversi_game.gameBoard[int(player_input.split()[0]) + 1].split()[int(player_input.split()[1]) + 1] != reversi_game.EMPTY:
                            print("Invalid position: occupied by another piece")
                            continue
                        else:
                            # if the position is valid, player can make the move
                            if reversi_game.isPositionValid([int(player_input.split()[0]) + 1, int(player_input.split()[1]) + 1], reversi_game.playerColour) == True:
                                reversi_game.makeMovePlayer([int(player_input.split()[0]) + 1, int(player_input.split()[1]) + 1])
                                break
                            else:
                                print("Invalid position: piece doesn't surround line of opponent pieces.")
                                continue
                    except:
                        print("Invalid position: Invalid Input")
                        continue
                # display the gameboard after player making the move
                reversi_game.displayBoard()
                if game_over == True or quit_game == True:
                    break
                
                # computer will make the move after player
                reversi_game.COUNTER = 'c'
                game_over = reversi_game.isGameOver()
                if game_over == True:
                    print("Game Over!")
                    reversi_game.displayBoard()
                    break                 
                if difficulty == '1':
                    easycomputer_move = reversi_game.makeMoveNaive()
                    print("Computer making move:", easycomputer_move)
                elif difficulty == '2':
                    hardcomputer_move = reversi_game.makeMoveSmart()
                    print("Computer making move:", hardcomputer_move)
                reversi_game.displayBoard()

        
        # ask the user if he/she wants to play again
        play_again = input("Do you want to play again (y/n)? ")
        if play_again == 'y':
            continue
        elif play_again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid Input, quit the game automatically")
            break


main()