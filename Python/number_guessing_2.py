import random
round_amount = 0

def isnumber(s): # Checks if input string is a valid integer
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def rounds(): # Asks the amount of rounds that should be played
    while True:
        global round_amount
        round_amount = input("How many rounds would you like to play? (Type 'quit' to exist): ")
        if round_amount.lower() == "quit":
            print("See you next time")
            quit()
        elif isnumber(round_amount):
            round_amount = int(round_amount)
            game()
        else:
            print("Please enter a valid response.")

def isplaying(): # Asks the user if they want to play the game
    print("You will pick two numbers and a random number between those two numbers will be chosen.")
    print("You will have to try to guess the correct number. If you guess wrong, it will tell you if you went too high or too low until you guess correctly.")
    while True:
        playing = input("Would you like to play? y/n: ")
        playing = playing.lower()
        if playing == "n" or playing == "no":
            print("That's a shame, see you another time")
            quit()
        elif playing == "y" or playing == "yes":
            rounds()
        else:
            print("Please select a valid response.")

def game(): # Main code for the game
    for i in range(round_amount):
        while True:
            first_number = input("Select the first number: ")
            if isnumber(first_number):
                first_number = int(first_number)
                break
            else:
                print("Select a valid number.")
        while True:
            second_number = input("Select the second number: ")
            if isnumber(second_number):
                second_number = int(second_number)
                break
            else:
                print("Select a valid number. ")
        correct_answer = random.randint(first_number, second_number)
        print(f"Now guess a number between {first_number} and {second_number}.")
        while True:
            guess = input("Your guess: ")
            if isnumber(guess):
                guess = int(guess)
                if guess < first_number:
                    print(f"The number must be higher than {first_number}")
                elif guess > second_number:
                    print(f"The number must be smaller than {second_number}")
                elif guess < correct_answer:
                    print("Too low")
                elif guess > correct_answer:
                    print("Too high")
                elif guess == correct_answer:
                    print(f"Correct, the answer was {correct_answer}")
                    break
            else:
                print("Please select a valid number.")

isplaying()

# Ignore this