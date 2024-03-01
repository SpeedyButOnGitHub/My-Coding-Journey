# Check if the value is a valid integer number
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def is_playing():
    while True:
        number1 = input("Please enter the first number: ")
        if is_number(number1):
            number1 = int(number1)
            break
        else:
            print("Invalid Number!")

    while True:
        number2 = input("Please enter the second number: ")
        if is_number(number2):
            number2 = int(number2)
            break
        else:
            print("Invalid Number!")

    while True:
        equation = input("Do you want to add, subtract, multiply, or divide? (Enter 'exit' to quit): ")
        if equation == "exit":
            break
        elif equation == "add":
            result = number1 + number2
            print(f"{number1} + {number2} = {result}")
        elif equation == "subtract":
            result = number1 - number2
            print(f"{number1} - {number2} = {result}")
        elif equation == "multiply":
            result = number1 * number2
            print(f"{number1} * {number2} = {result}")
        elif equation == "divide":
            if number2 != 0:  # Avoid dividing by 0
                result = number1 / number2
                print(f"{number1} / {number2} = {result}")
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid operation!")
        
        play_again = input("Would you like to do another equation? Y/N ")
        
        if play_again != "Y":
            break

is_playing()

