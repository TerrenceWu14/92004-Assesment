import random


def int_check(question, exit_code="xxx"):
    # sets up an error message
    error = "Please enter an integer or one that is above 0"

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if response <= 0:
                print(error)

            return response

        except ValueError:
            print(error)


# Displays instructions
def instructions():
    print('''

*** Instructions ***

To begin, choose the number of questions you would
like to be asked. We will then ask that amount of questions.

To leave prematurely 

    ''')


# Checks whether the user entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you didn't choose a valid option (yes/no)")


def quiz():
    # Initializes variables
    question_num = 0
    history = []

    # asks the user how hard they would like the quiz to be
    while True:
        difficulty = int_check("What level of difficulty do you want to play? 1 to 3 with 3 being the hardest: ")
        if difficulty > 3:
            print("Choose a number from 1 to 3 only: ")
        else:
            break

    # loops while question_num is lower than amount of questions - chosen at the start
    while question_num <= amount_questions:
        question_num += 1
        print()
        print(f"Question {question_num}:")

        # Generates the numbers for the question and difficulty
        if difficulty == 3:
            num_1 = random.randint(1, 25)
            num_2 = random.randint(1, 25)
        elif difficulty == 2:
            num_1 = random.randint(1, 15)
            num_2 = random.randint(1, 15)
        else:
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)

        # the list for the types of question
        math_type = ["multiplication", "adding", "subtraction", "division"]

        # generates the question type
        question_type = random.choice(math_type)

        # generates the question format
        if math_type == "subtraction":
            question_format = f"What is {num_1} - {num_2}? "
            answer = num_1 - num_2

        elif question_type == "adding":
            question_format = f"What is {num_1} + {num_2}? "
            answer = num_1 + num_2

        elif question_type == "multiplication":
            question_format = f"What is {num_1} x {num_2}? "
            answer = num_1 * num_2

        else:
            # makes sure that the number being divided is always going to result in a whole number
            num_1 = num_1 * num_2
            question_format = f"What is {num_1} divided by {num_2}? "
            answer = num_1 / num_2

        # prints the question
        print(question_format)

        # The user gets to ask the question
        user_answer = int_check(question_format)
        print(f"Answer: {answer}")

        # sets correct to yes if the answer is correct
        if user_answer == answer:
            feedback = f"You got the answer right, it was {answer}"
            history_item = f"In Round {question_num}: You got the answer right, it was {answer}."

        # sets correct to no
        else:
            feedback = f"You got the answer wrong, it was {answer}"
            history_item = f"In Round {question_num}: You got the answer wrong, it was {answer}."

        history.append(history_item)
        print(feedback)

    # asks the user whether they would want to see the game history
    view_history = yes_no("Do you want to view the game history?")
    print()

    # displays the game history if the user wants to see it
    if view_history == "yes":
        print("\n⌛⌛⌛ Game History ⌛⌛⌛ ")
        print()
        # Outputs the game history
        for item in history:
            print(item)


# Main routine

# Displays the title
print()
print("--- Welcome to Terrence's Math Quiz on Basic Facts ---")
print()

# Asks the user if they want to see the instructions
want_instruction = yes_no("Do you want to read the instructions? (If so type yes or if not type no)")

# displays instructions
if want_instruction == "yes":
    instructions()

# asks the user how many questions they want
amount_questions = int_check("How many questions do you want us to ask? ")

# Starts the quiz
quiz()
