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

    # Generates the numbers for the question
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    # the list for the types of question
    type = ["multiplication", "adding", "subtraction", "division"]

    # generates the question type
    question_type = random.choice(type)

    # generates the question format
    if type == "subtraction":
        question_format = f"What is {num_1} - {num_2}? "
        answer = num_1 - num_2

    elif question_type == "adding":
        question_format = f"What is {num_1} + {num_2}? "
        answer = num_1 + num_2

    elif question_type == "multiplication":
        question_format = f"What is {num_1} x {num_2}? "
        answer = num_1 * num_2

    else:
        question_format = f"What is {num_1} divided by {num_2}? "
        answer = num_1 / num_2

    # prints the question
    print(question_format)

    # The user gets to ask the question
    user_answer = int_check(question_format)
    print(f"Answer: {answer}")

    # sets correct to yes if the answer is correct
    if user_answer == answer:
        correct = "yes"

    # sets correct to no
    else:
        correct = "no"

    return correct


# Main routine

# Displays the title
print()
print("--- Welcome to Terrence's Math Quiz ---")
print()

# Asks the user if they want to see the instructions
want_instruction = yes_no("Do you want to read the instructions? (If so type yes or if not type no)")

# displays instructions
if want_instruction == "yes":
    instructions()

# asks the user how many questions they want
amount_questions = int_check("How many questions do you want us to ask? ")

# Initializes variables
question_num = 0

while question_num <= amount_questions:
    question_num += 1
    print(f"Question {question_num}:")

    # Starts the quiz
    quiz()
