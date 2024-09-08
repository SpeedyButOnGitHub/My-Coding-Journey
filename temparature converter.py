def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def display_menu():
    print("Temperature Converter")
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Celcius to Kelvin")
    print("4. Kelvin to Celcius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Farhenheit")
    print("7. Exit")

def get_conversion_choice():
    while True:
        try:
            choice = int(input("Enter the number of the conversion you want to perfrom (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number")

def convert_temperature():
    while True:
        display_menu()
        choice = get_conversion_choice()

        if choice == 7:
            print("Exiting the program")
            break
        try:
            temp = float(input("Enter the temparature value to convert: "))
        except ValueError:
            print("Invalid temparature value, Please enter a numeric value.")
            continue

        if choice == 1:
            print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit")
        elif choice == 2:
            print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius")
        elif choice == 3:
            print(f"{temp} Celsius is {celsius_to_kelvin(temp)} Kelvin")
        elif choice == 4:
            print(f"{temp} Kelvin is {kelvin_to_celsius(temp)} Celsius")
        elif choice == 5:
            print(f"{temp} Fahrenheit is {fahrenheit_to_kelvin(temp)} Kelvin")
        elif choice == 6:
            print(f"{temp} Kelvin is {kelvin_to_fahrenheit(temp)} Fahrenheit")

        while True: 
            repeat_conversion = input("Would you like to do another conversion? Y/N: ")
            repeat_conversion = repeat_conversion.lower()
            if repeat_conversion == "n" or repeat_conversion == "no":
                print("Exiting the program")
                quit()
            elif repeat_conversion == "y" or repeat_conversion == "yes":
                break   
            else:
                print("Please enter a correct response.")

if __name__ == "__main__":
    convert_temperature()