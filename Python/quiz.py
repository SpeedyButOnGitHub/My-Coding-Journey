score = 0

playing = input("Would you like to play my quiz game? Y/N ")

if playing != "y":
    quit()

print("Awesome, let's play!")

def ask_question(question, options, correct_answer):
    global score
    print(question)
    for option, answer_text in options.items():
        print(f"{option}) {answer_text}")
    user_answer = input("Your answer (Enter the letter corresponding to your choice): ").strip().upper()
    
    if user_answer == correct_answer:
        score += 1
        print(f"Correct! You have gained 1 point. Your current score is: {score}")
        return True
    else:
        score -= 1
        print(f"Incorrect, the correct answer is {correct_answer}, {options[correct_answer]}. You have lost 1 point, your current score is: {score}.")
        return False
    
questions1 = "What is the capital of France? "
options1 = {
        "A": "London",
        "B": "Paris",
        "C": "Berlin",
        "D": "Rome"
}
correct_answer1 = "B"


questions2 = "Who was the first president of the United states?"
options2 = {
    "A": "Thomas Jerfferson",
    "B": "George Washington",
    "C": "Abraham Lincon",
    "D": "John F: Kennedy"
}
correct_answer2 = "B"


ask_question(questions1, options1, correct_answer1)
#Check if the score is 10 or higher
if score >= 10:
    print("You have won the game!")
    quit()

ask_question(questions2, options2, correct_answer2)
#Check if the score is 10 or higher 
if score >= 10:
    print("You have won the game!")
    quit()

# I know that there's technically no way to get a score of 10 with only two questions and that I don't have to check if the score is higher than 10 until you can actually get 10 points but it's just an example
    