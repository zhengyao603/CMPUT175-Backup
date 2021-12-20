"""
CMPUT 175 - Assignment 2 Template
"""

"""
Hints:
    - self.gameBoard represents the game board
    - self.playerColour represents the colour of the human player
    - self.computerColour represents the colour of the computer
    - the colour arguments are eiter self.WHITE or self.BLACK, which are defined below
"""


class Reversi:
    WHITE = "w"
    BLACK = "b"
    EMPTY = "."
    SIZE = 8
    COUNTER = 0

    def __init__(self):
        self.newGame()


    """
    Functionality:
        Create the game state so players can play again
    Parameters: 
        None
    """
    def newGame(self):
        # initialize the gameboard
        self.gameBoard = ["   0  1  2  3  4  5  6  7",
                          "0  .  .  .  .  .  .  .  .",
                          "1  .  .  .  .  .  .  .  .",
                          "2  .  .  .  .  .  .  .  .",
                          "3  .  .  .  w  b  .  .  .",
                          "4  .  .  .  b  w  .  .  .",
                          "5  .  .  .  .  .  .  .  .",
                          "6  .  .  .  .  .  .  .  .",
                          "7  .  .  .  .  .  .  .  ."]
        return


    """
    Functionality:
        Return the score of the player
    Parameters:
        colour: The colour of the player to get the score for 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def getScore(self, colour):
        # count all the black pieces and white pieces, then record the score
        score = 0
        for row in self.gameBoard:
            for column in row.split():
                if column == colour:
                    score += 1
        return score


    """
    Functionality:
        Set the colour for the human player to the designated colour, as well as the computer will haev the other colour
    Parameters:
        colour: The colour of the player the user wants to play as 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def setPlayerColour(self, colour):
        # no matter which colour player choses, the other colour will be computerColour
        if colour == self.WHITE:
            self.playerColour = self.WHITE
            self.computerColour = self.BLACK
        elif colour == self.BLACK:
            self.playerColour = self.BLACK
            self.computerColour = self.WHITE


    """
    Functionality:
        Print out the current board state
        The index of the rows and columns should be on the left and top.
        See the sample output for details
    Parameters: 
        None
    """
    def displayBoard(self):
        for line in self.gameBoard:
            print(line)
        print("Score: white %d, black %d" %(self.getScore(self.WHITE), self.getScore(self.BLACK)))


    """
    Functionality:
        Return true if the input position 'position' is horizontal valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isHorizontalValid(self, position, colour):
        validity = False
        # if the given colour is playerColur
        if colour == self.playerColour:
            # from given position to right, trying to find if there is any pieces have same colour with given colour
            if position[1] >= 3:
                column_index = position[1] - 1
                if self.gameBoard[position[0]].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while column_index >= 1:
                        if self.gameBoard[position[0]].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[position[0]].split()[column_index] == self.playerColour:
                            validity = True
                        column_index -= 1
            
            # from given position to left, trying to find if there is any pieces have same colour with given colour
            if position[1] <= 6:
                column_index = position[1] + 1
                if self.gameBoard[position[0]].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while column_index <= 8:
                        if self.gameBoard[position[0]].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[position[0]].split()[column_index] == self.playerColour:
                            validity = True
                        column_index += 1
                        
        
        # if the given colour is computerColour
        elif colour == self.computerColour:
            # from given position to right, trying to find if there is any pieces have same colour with given colour
            if position[1] >= 3:
                column_index = position[1] - 1
                if self.gameBoard[position[0]].split()[column_index] == self.playerColour:
                     # if there is any empty, which means the move is invalid, then break the for loop
                    while column_index >= 1:
                        if self.gameBoard[position[0]].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[position[0]].split()[column_index] == self.computerColour:
                            validity = True
                        column_index -= 1
            
             # from given position to left, trying to find if there is any pieces have same colour with given colour
            if position[1] <= 6:
                column_index = position[1] + 1
                if self.gameBoard[position[0]].split()[column_index] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while column_index <= 8:
                        if self.gameBoard[position[0]].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[position[0]].split()[column_index] == self.computerColour:
                            validity = True
                        column_index += 1
        
        return validity
                        
                        
    """
    Functionality:
        Return true if the input position 'position' is vertical valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isVerticalValid(self, position, colour):
        validity = False
        # if the given colour is playerColur
        if colour == self.playerColour:
            # from given position to top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3:
                row_index = position[0] - 1
                if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1:
                        if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                            validity = True
                        row_index -= 1
            
            # from given position to bottom, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6:
                row_index = position[0] + 1
                if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8:
                        if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                            validity = True
                        row_index += 1
        
        
        # if the given colour is computerColour
        elif colour == self.computerColour:
            # from given position to top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3:
                row_index = position[0] - 1
                if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1:
                        if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                            validity = True
                        row_index -= 1
            
            # from given position to bottom, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6:
                row_index = position[0] + 1
                if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8:
                        if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                            validity = True
                        row_index += 1
        return validity
    
    """
    Functionality:
        Return true if the input position 'position' is diagonal(from right bottom to left top) valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isFirstDiagonalValid(self, position, colour):
        validity = False
        # if the given colour is playerColur
        if colour == self.playerColour:
            # from given position to right bottom, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6 and position[1] <= 6:
                row_index = position[0] + 1
                column_index = position[1] + 1
                if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8 and column_index <= 8:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                            validity = True
                        column_index += 1
                        row_index += 1
            
            # from given position to left top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3 and position[1] >= 3:
                row_index = position[0] - 1
                column_index = position[1] - 1
                if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1 and column_index >= 1:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                            validity = True
                        column_index -= 1
                        row_index -= 1
    
    
        # if the given colour is computerColour
        elif colour == self.computerColour:
            # from given position to right top, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6 and position[1] <= 6:
                row_index = position[0] + 1
                column_index = position[1] + 1
                if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8 and column_index <= 8:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                            validity = True
                        column_index += 1
                        row_index += 1
            
            # from given position to left top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3 and position[1] >= 3:
                row_index = position[0] - 1
                column_index = position[1] - 1
                if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1 and column_index >= 1:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                            validity = True
                        column_index -= 1
                        row_index -= 1

        return validity


    """
    Functionality:
        Return true if the input position 'position' is diagonal(from right top to left bottom) valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isSecondDiagonalValid(self, position, colour):
        validity = False
        # if the given colour is playerColur
        if colour == self.playerColour:
            # from given position to right top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3 and position[1] <= 6:
                row_index = position[0] - 1
                column_index = position[1] + 1
                if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1 and column_index <= 8:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                            validity = True
                        column_index += 1
                        row_index -= 1
            
            # from given position to left bottom, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6 and position[1] >= 3:
                row_index = position[0] + 1
                column_index = position[1] - 1
                if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8 and column_index >= 1:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                            validity = True            
                        column_index -= 1
                        row_index += 1
        
        
        # if the given colour is computerColour
        elif colour == self.computerColour:
            # from given position to right top, trying to find if there is any pieces have same colour with given colour
            if position[0] >= 3 and position[1] <= 6:
                row_index = position[0] - 1
                column_index = position[1] + 1
                if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index >= 1 and column_index <= 8:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                            validity = True
                        column_index += 1
                        row_index -= 1
            
            # from given position to left bottom, trying to find if there is any pieces have same colour with given colour
            if position[0] <= 6 and position[1] >= 3:
                row_index = position[0] + 1
                column_index = position[1] - 1
                if self.gameBoard[row_index].split()[column_index] == self.playerColour:
                    # if there is any empty, which means the move is invalid, then break the for loop
                    while row_index <= 8 and column_index >= 1:
                        if self.gameBoard[row_index].split()[column_index] == self.EMPTY:
                            break
                        if self.gameBoard[row_index].split()[column_index] == self.computerColour:
                            validity = True            
                        column_index -= 1
                        row_index += 1
            
        return validity


    """
    Functionality:
        Return true if the input position 'position' is valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isPositionValid(self, position, colour):
        # validity: list which contains three elements representing whether the position is horizontally/vertically/diagonally valid 
        validity = [False, False, False, False]
        # check if the position is horizontal, vertical, or diagnoal valid
        validity[0] = self.isHorizontalValid(position, colour)
        validity[1] = self.isVerticalValid(position, colour)
        validity[2] = self.isFirstDiagonalValid(position, colour)
        validity[3] = self.isSecondDiagonalValid(position, colour)
        # if any of those three is valid, then the position is valid
        if True in validity:
            return True


    """
    Functionality:
        Return true if the game is over, false otherwise
        The game is over if any player cannot make a move, no matter whose turn it is
    Parameters: 
        None
    Note: 
        Skipping is not allowed
    """
    def isGameOver(self):
        valid_move = False
        # if its player's turn to move, check if there is any valid move for player
        if self.COUNTER == 'p':
            for row_index in range(1, 9):
                for column_index in range(1, 9):
                    if self.gameBoard[row_index].split()[column_index] == self.EMPTY \
                       and self.isPositionValid([row_index, column_index], self.playerColour) == True:
                        valid_move = True
        
        # if its computer's turn to move, check if there is any valid move for computer
        elif self.COUNTER == 'c':
            for row_index in range(1, 9):
                for column_index in range(1, 9):
                    if self.gameBoard[row_index].split()[column_index] == self.EMPTY \
                    and self.isPositionValid([row_index, column_index], self.computerColour) == True:
                        valid_move= True
        
        # if there is no valid move for player or computer at their turn, then the game ends
        if valid_move == False:
            return True
        elif valid_move == True:
            return False


    """
    Functionality:
        Reverse all the piecese which are captured by different colour horizontally/veritically/diagonlally
        This function is only working after player/computer making move
    Parameters:
        psoition -> A list [i, j] where i is the riw and j is the column
        colour: The colour that is making the move
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def reversePiece(self, position, colour):
        """if the position is horizontal valid"""
        if self.isHorizontalValid(position, colour) == True:
            # from the given position to the left, reverse all the pieces which are surronded by the other colour
            column_index = position[1] - 1
            while column_index >= 1:
                if self.gameBoard[position[0]].split()[column_index] == colour \
                    and self.gameBoard[position[0]].split()[column_index + 1] != self.EMPTY:
                    changing_row = self.gameBoard[position[0]].split()
                    for i in range(column_index, position[1] + 1):
                        changing_row[i] = colour
                    self.gameBoard[position[0]] = '  '.join(changing_row)
                    break
                column_index -= 1
            
            # from the given position to the right, reverse all the pieces which are surronded by the other colour
            column_index = position[1] + 1
            while column_index <= 8:
                if self.gameBoard[position[0]].split()[column_index] == colour \
                   and self.gameBoard[position[0]].split()[column_index - 1] != self.EMPTY:
                    changing_row = self.gameBoard[position[0]].split()
                    for j in range(position[1], column_index + 1):
                        changing_row[j] = colour
                    self.gameBoard[position[0]] = '  '.join(changing_row)
                    break
                column_index += 1
        
        """if the position is vertical valid"""
        if self.isVerticalValid(position, colour) == True:
            # from the given position to the top, reverse all the pieces which are surronded by the other colour
            row_index = position[0] - 1
            while row_index >= 1:
                if self.gameBoard[row_index].split()[position[1]] == colour \
                   and self.gameBoard[row_index + 1].split()[position[1]] != self.EMPTY:
                    for i in range(row_index, position[0] + 1):
                        changing_row = self.gameBoard[i].split()
                        changing_row[position[1]] = colour
                        self.gameBoard[i] = '  '.join(changing_row)
                    break
                row_index -= 1
            
            # from the given position to the bottom, reverse all the pieces which are surronded by the other colour
            row_index = position[0] + 1
            while row_index <= 8:
                if self.gameBoard[row_index].split()[position[1]] == colour \
                   and self.gameBoard[row_index - 1].split()[position[1]] != self.EMPTY:
                    for j in range(position[0], row_index + 1):
                        changing_row = self.gameBoard[j].split()
                        changing_row[position[1]] = colour
                        self.gameBoard[j] = '  '.join(changing_row)
                    break
                row_index += 1
        
        """if the position is diagonal valid(from right top to left bottom)"""
        if self.isSecondDiagonalValid(position, colour) == True:
            # from given position to the right top, reverse all the pieces which are surronded by the other colour
            row_index = position[0] - 1
            column_index = position[1] + 1
            while row_index >= 1 and column_index <= 8:
                if self.gameBoard[row_index].split()[column_index] == colour \
                   and self.gameBoard[row_index + 1].split()[column_index - 1] != self.EMPTY:
                    while row_index != position[0] and column_index != position[1]:
                        changing_row = self.gameBoard[row_index].split()
                        changing_row[column_index] = colour
                        self.gameBoard[row_index] = '  '.join(changing_row)
                        row_index += 1
                        column_index -= 1
                    break
                row_index -= 1
                column_index += 1
                
            # from given position to the left bottom, reverse all the pieces which are surronded by the other colour
            row_index = position[0] + 1
            column_index = position[1] - 1
            while row_index <= 8 and column_index >= 1:
                if self.gameBoard[row_index].split()[column_index] == colour \
                   and self.gameBoard[row_index - 1].split()[column_index + 1] != self.EMPTY:
                    while row_index != position[0] and column_index != position[1]:
                        changing_row = self.gameBoard[row_index].split()
                        changing_row[column_index] = colour
                        self.gameBoard[row_index] = '  '.join(changing_row)
                        row_index -= 1
                        column_index += 1
                    break
                row_index += 1
                column_index -= 1
            
        """if the position is diagonal valid(from right bottom to left top)"""
        if self.isFirstDiagonalValid(position, colour) == True:
            # from given position to the right bottom, reverse all the pieces which are surronded by the other colour
            row_index = position[0] + 1
            column_index = position[1] + 1
            while row_index <= 8 and column_index <= 8:
                if self.gameBoard[row_index].split()[column_index] == colour \
                   and self.gameBoard[row_index - 1].split()[column_index - 1] != self.EMPTY:
                    while row_index != position[0] and column_index != position[1]:
                        changing_row = self.gameBoard[row_index].split()
                        changing_row[column_index] = colour
                        self.gameBoard[row_index] = '  '.join(changing_row)
                        row_index -= 1
                        column_index -= 1
                    break
                row_index += 1
                column_index += 1
            
            # from given position to the left top, reverse all the pieces which are surronded by the other colour
            row_index = position[0] - 1
            column_index = position[1] - 1
            while row_index >= 1 and column_index >= 1:
                if self.gameBoard[row_index].split()[column_index] == colour \
                   and self.gameBoard[row_index + 1].split()[column_index + 1] != self.EMPTY:
                    while row_index != position[0] and column_index != position[1]:
                        changing_row = self.gameBoard[row_index].split()
                        changing_row[column_index] = colour
                        self.gameBoard[row_index] = '  '.join(changing_row)
                        row_index += 1
                        column_index += 1
                    break
                row_index -= 1
                column_index -= 1


    """
    Functionality:
        Make the given move for the human player, and capture any pieces
        If you assume the move is valid, make sure the validity is checked before calling
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def makeMovePlayer(self, position):
        # change specific piece at given position with player's colour
        changing_row = self.gameBoard[position[0]].split()
        changing_row[position[1]] = self.playerColour
        self.gameBoard[position[0]] = '  '.join(changing_row)
        # reverse all the computer pieces which are surronded by player's piece
        self.reversePiece(position, self.playerColour)


    """
    Functionality:
        Make a naive move for the computer
        This is the first valid move when scanning the board left to right, starting at the top
    Parameters: 
        None
    """
    def makeMoveNaive(self):
        # from top to bottom, right to left, trying to find if there is any valid move for computer
        row_index = 1
        while row_index <= 8:
            column_index = 1
            while column_index <= 8:
                # make the move at the first valid position, and reverse all the pieces of player pieces,
                # which should be reversed
                if self.gameBoard[row_index].split()[column_index] == self.EMPTY \
                   and self.isPositionValid([row_index, column_index], self.computerColour) == True:
                    changing_row = self.gameBoard[row_index].split()
                    changing_row[column_index] = self.computerColour
                    self.gameBoard[row_index] = '  '.join(changing_row)
                    self.reversePiece([row_index, column_index], self.computerColour)
                    # return the actual position of computer's move
                    return [row_index - 1, column_index - 1]
                column_index += 1
            row_index += 1   


    """
    Functionality:
        Make a move for the computer which is the best move available
        This should be the move that results in the best score for the computer
    Parameters: 
        None
    """
    def makeMoveSmart(self):
        # valid_position: record all the valid moves for computer
        valid_position = []
        row_index = 1
        # find all the valid moves for computer
        while row_index <= 8:
            column_index = 1
            while column_index <= 8:
                if self.gameBoard[row_index].split()[column_index] == self.EMPTY \
                   and self.isPositionValid([row_index, column_index], self.computerColour) == True:
                    valid_position.append([row_index, column_index])
                column_index += 1
            row_index += 1
        
        best_move = [1, 1]
        best_score = 0
        # try which of the moves from valid_position can get the best score
        current_gameBoard = tuple(self.gameBoard)
        for position in valid_position:
            changing_row = self.gameBoard[position[0]].split()
            changing_row[position[1]] = self.computerColour
            self.gameBoard[position[0]] = '  '.join(changing_row)
            self.reversePiece(position, self.computerColour)
            if self.getScore(self.computerColour) > best_score:
                best_score = self.getScore(self.computerColour)
                best_move = position
            # return the status of gameboard after finish trying each move
            self.gameBoard = list(current_gameBoard)

        # make the move for comnputer at the position which can provide best score
        changing_row = self.gameBoard[best_move[0]].split()
        changing_row[best_move[1]] = self.computerColour
        self.gameBoard[best_move[0]] = '  '.join(changing_row)
        self.reversePiece(best_move, self.computerColour)
        # return the actual position of the "best move" position
        return [best_move[0] - 1, best_move[1] - 1]
