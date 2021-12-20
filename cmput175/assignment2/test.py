gameBoard= ["   0  1  2  3  4  5  6  7",
            "0  b  b  b  b  b  b  .  .",
            "1  .  b  b  b  b  b  .  .",
            "2  b  b  b  b  b  b  b  b",
            "3  b  w  b  b  b  b  b  .",
            "4  b  b  b  w  b  b  b  .",
            "5  b  b  b  w  w  b  b  w",
            "6  b  b  b  b  b  b  w  w",
            "7  b  b  b  .  b  w  .  w"]


def isVerticalValid(position, colour):
    validity = False
    # if the given colour is playerColur
    if colour == 'w':
        if position[0] >= 3:
            row_index = position[0] - 1
            if gameBoard[row_index].split()[position[1]] == 'b':
                while row_index >= 1:
                    if gameBoard[row_index].split()[position[1]] == '.':
                        break
                    if gameBoard[row_index].split()[position[1]] == 'w':
                        validity = True
                    row_index -= 1
        
        if position[0] <= 6:
            row_index = position[0] + 1
            if gameBoard[row_index].split()[position[1]] == 'b':
                while row_index <= 8:
                    if gameBoard[row_index].split()[position[1]] == '.':
                        break
                    if gameBoard[row_index].split()[position[1]] == 'w':
                        validity = True
                    row_index += 1
    
    
    # if the given colour is computerColour
    elif colour == self.computerColour:
        if position[0] >= 3:
            row_index = position[0] - 1
            if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                while row_index >= 1:
                    if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                        break
                    if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                        validity = True
                    row_index -= 1
        
        if position[0] <= 6:
            row_index = position[0] + 1
            if self.gameBoard[row_index].split()[position[1]] == self.playerColour:
                while row_index <= 8:
                    if self.gameBoard[row_index].split()[position[1]] == self.EMPTY:
                        break
                    if self.gameBoard[row_index].split()[position[1]] == self.computerColour:
                        validity = True
                    row_index += 1
    
    return validity

if isVerticalValid([2, 8], 'w') == True:
    print('wocaonima')
    # from the given position to the top
    row_index = position[0] - 1
    while row_index >= 1:
        if gameBoard[row_index].split()[position[1]] == 'w' \
           and gameBoard[row_index + 1].split()[position[1]] != '.':
            for i in range(row_index, position[0] + 1):
                changing_row = gameBoard[i].split()
                changing_row[position[1]] = colour
                gameBoard[i] = '  '.join(changing_row)
            break
        row_index -= 1
    
    # from the given position to the bottom
    row_index = position[0] + 1
    while row_index <= 8:
        if gameBoard[row_index].split()[position[1]] == 'w' \
           and self.gameBoard[row_index - 1].split()[position[1]] != '.':
            for j in range(position[0], row_index + 1):
                changing_row = gameBoard[j].split()
                changing_row[position[1]] = colour
                gameBoard[j] = '  '.join(changing_row)
            break
        row_index += 1
    
for line in gameBoard:
    print(line)