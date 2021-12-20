from WordGuess import WordGuess


def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    #TODO: read a file and stores the secret words as keys and their corresponding hints as values in a dictionary
    word_dict = {}
    # error handling
    try:
        input_file = open(filename, 'r')
    except IOError:
        print("IOError. %s does not exist" %(filename))
    else:
        # read the file and stores necessary information
        file_data = input_file.read()
        input_file.close()
        for word_and_hint in file_data.split('\n'):
            word_dict[word_and_hint.split()[0]] = word_and_hint.split()[1]
    return word_dict


def main():
    #TODO: function that allows multiple games of Word Guess to be played
    filename = input("Please enter a Word Guess input file: ")
    # being able to play the game several times
    while True:
        current_game = WordGuess(readWords(filename))
        current_game.play()
        play_again = input("Would you like to play again? (y/n): ")
        if play_again == 'y' or play_again == 'Y':
            continue
        elif play_again == 'n' or play_again == 'N':
            break


if __name__ == "__main__":
    main()