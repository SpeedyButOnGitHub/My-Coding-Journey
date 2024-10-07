import random

#Check if number is an integer 
def isnumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def playing():
    while True:
        isplaying = input("Do you want to play guess the number? Y/N ")
        isplaying = isplaying.lower()
        if isplaying == "y":
            break
        elif isplaying == "n":
            print("What a bummer, hope to see you another time!")
            quit()
        else:
            print("Please enter a valid response!")

def game():
    while True:
        first_number = input("Select the first number: ")
        if isnumber(first_number):
            first_number = int(first_number)
            if first_number <= 0:
                print("Please select a number higher than 0. ")
            elif first_number > 0:
                break
        
        else:
            print("Invalid number") 
    while True:
        second_number = input("Select the second number: ")
        if isnumber(second_number):
            second_number = int(second_number)
            if second_number <= first_number:
                print(f"Please select a number higher than the first, ({first_number}).")
            elif second_number > first_number:
                break
        else:
            print("Invalid number")
    print(f"Alright, you have chosen a range between {first_number} and {second_number}. Start guessing numbers in that range and I will tell you if you're too high or too low. (Type 'exit' to leave)")
    
    # Picks a random number between the first and second one
    correct_answer = random.randint(first_number, second_number)
    while True:    
        guessing = input("Your guess: ")
        if guessing == "exit":
            quit()
        guessing = int(guessing)

        if guessing > correct_answer:
            print("Too high!")
        elif guessing < correct_answer:
            print("Too low!")
        else:
            print(f"You guessed right, the correct answer was {correct_answer}!")
            break

def play_again():
    playagain = input("Would you like to play again? Y/N ").lower()
    if playagain == "n":
        print("Hope to see you soon again!")
        quit()


playing()
while True:
    game()
    play_again()
