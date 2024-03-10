import math


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


# Main routine

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
    pass