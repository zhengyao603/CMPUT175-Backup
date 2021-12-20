# import random module
import random

# define a new class called 'Secret_Number'
class Secret_Number:
    # initialize the class
    def __init__(self):
        # number: for storing the random number
        number = []
        # generate the first digit which cannot be 0
        while True:
            first_digit = random.randint(0, 9)
            if first_digit != 0:
                number.append(str(first_digit))
                break
        # generate the second digit which cannot be same with the first
        while True:
            second_digit = random.randint(0, 9)
            if second_digit != int(number[0]):
                number.append(str(second_digit))
                break
        # generate the third digit which cannot be same with the first or the second
        while True:
            third_digit = random.randint(0, 9)
            if third_digit != int(number[0]) and third_digit != int(number[1]):
                number.append(str(third_digit))
                break
        # join the random number and set it as an attribute of the class
        self.number = "".join(number)
    
    # function which can return the generated random number
    def get(self):
        return self.number
    
    # function which is responsible for determining if the input guess number match the generated random number
    def getClues(self, guess_number):
        # correct_position: count for the digit which is in the generated number and its position is right
        correct_position = 0
        # wrong_position: count for the digit which is in the generaed number but its position is not correct
        wrong_position = 0
        for i in range(len(guess_number)):
            # if guess number is exactly same with generated numebr then return 'CORRECT'
            if guess_number == self.number:
                return "CORRECT"
            # if there is no such a single digit same with generated number then return 'WRONG'
            if guess_number[0] not in self.number and guess_number[1] not in \
               self.number and guess_number[2] not in self.number:
                return "WRONG"            
            # if there is some digits in generated number
            if guess_number[i] in self.number:
                if guess_number[i] == self.number[i]:
                    correct_position += 1
                else:
                    wrong_position += 1
        # return the count of correct_position followed by DING and count of
        # wrong_position followed by DONG
        return ("%dDING %dDONG" %(correct_position, wrong_position))
                

# function which is responsible for determing if the input is correct
def readNumber(attempts):
    print("Enter a three digit number with non-repeating digits")
    guess_number = input("Guess attempt %d: " %(attempts))
    count_of_number = 0
    repeat_number = 0
    if guess_number[0] == '0':
        return "Invalid Input"
    for digit in guess_number:
        if ord(digit) >= 48 and ord(digit) <= 57:
            count_of_number += 1
        if guess_number[0] == guess_number[1] or guess_number[1] == guess_number[2] \
           or guess_number[2] == guess_number[0]:
            return "Invalid Input"
    if count_of_number == 3:
        return guess_number
    else:
        print("Please enter a three digit non-repeating number")
        return "Invalid Input"
    

while True:
    secret_number = Secret_Number()
    print("I am thinking of a 3 digit number. Try to guess what it is. You have 10 attempts.")
    print("If you guess none of the digits I will answer WRONG")
    print("I will answer DING for every correct digit in the right position and will answer DONG for every correct digit in the wrong position.")
    print(secret_number.get())
    # initialize the count of attempts to 1
    attempts = 1
    # while the attempts is less or equal to 10
    while attempts <= 10:
        guess_number = readNumber(attempts)
        # if the input guess number is valid
        if guess_number != "Invalid Input":
            result = secret_number.getClues(guess_number)
            if result == "CORRECT":
                print("You guessed it after %d attempts. The number is indeed %s" \
                      %(attempts, secret_number.get()))
                break
            elif result == "WRONG":
                print("WRONG")
            else:
                if int(result[0]) > 0:
                    print("DING " * int(result[0]), end = " ")
                print("DONG " * int(result.split()[1][0]))
            attempts += 1
    # if all the attempts are used
    if attempts == 11:
        print("You guessed it after 10 attempts. The number is indeed %s" %(secret_number.get()))
    # ask if the user want to play again
    again = input("Do you want to play again (Y/N)?")
    if again == "y":
        continue
    else:
        break
