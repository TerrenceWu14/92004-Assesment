import random


# Check that users have entered a valid integer

def int_check(question, low=None, high=None, exit_code="xxx"):
    # sets up an error message
    if low is None and high is None:
        error = "Please enter an integer"
        print()

    # if the number needs to be more than an
    # integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
        print()

    # if the number needs to be between a low and a high
    else:
        error = (f"Please enter and integer that"
                 f"is between {low} and {high} (inclusive)")
        print()

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks that the integer is not lower than the low num
            if low is not None and response < low:
                print(error)

            # checks that the integer is not higher than the high num
            elif high is not None and response > high:
                print(error)

            # returns the response if the response entered meets the criteria
            else:
                return response

        except ValueError:
            print(error)


# Displays instructions
def instructions():
    print('''

*** Instructions ***

To begin, choose the number of questions you would
like to be asked. We will then ask that amount of questions.

To leave prematurely type "xxx" as your answer after we ask you a question.
To answer, just type your answer in (in integer form only!)

Choose a difficulty level from 1 to 3 with 3 being the hardest and 1 being the easiest,
the way this works is that depending on the level you choose we will randomly generate a range of
number depending on the level of difficulty you chose.

Good luck and have fun!

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
    round_won = 0
    round_lost = 0

    # asks the user how hard they would like the quiz to be
    while True:
        difficulty = int_check("What level of difficulty do you want to play? 1 to 3, with 3 being the hardest: ",
                               low=1, high=3)
        break

    # loops while question_num is lower than amount of questions - chosen at the start
    while question_num < amount_questions:

        print()
        print(f"Question {question_num + 1}:")

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
            num_1 = num_1 + num_2
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

        # The user gets to ask the question
        user_answer = int_check(question_format)

        # makes the answer an integer
        answer = int(answer)

        # if the user types the exit code they are able to leave the game
        if user_answer == "xxx":
            print("Thanks for playing my basic math quiz!")
            print()
            break

        # sets correct to yes if the answer is correct
        elif user_answer == answer:
            round_won += 1
            feedback = f"You got the answer right, it was {answer}"
            history_item = f"Question {question_num + 1}: You got the answer right, it was {answer} ✅."

        # sets correct to no
        else:
            round_lost += 1
            feedback = f"You got the answer wrong, it was {answer}"
            history_item = f"Question {question_num + 1}: You got the answer wrong, it was {answer} ❌."

        # adds the round result into a list
        history.append(history_item)

        # prints the feedback/result of the round
        print(feedback)

        question_num += 1

    # if the user doesn't answer a single question it doesn't display stats/history
    if question_num == 0:
        print("Sorry you have not answered a single question thus there is no history"
              "or statistics we can show you.")
        exit()

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

    # Asks the user if they want to view the game stats
    print()
    view_stats = yes_no("Do you want to view the stats? ")
    print()

    # If yes, displays the game stats
    if view_stats == "yes":
        # Calculates the win percentage
        question_correct = round_won / question_num * 100

        # Calculates loss percentage:
        question_wrong = round_lost / question_num * 100

        print(f"Out of {question_num} questions:")
        print()
        print(f"- {question_correct:.2f}% of questions correct")
        print()
        print(f"- {question_wrong:.2f}% of questions wrong")
        print()


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

while True:
    # asks the user how many questions they want
    amount_questions = int_check("How many questions do you want us to ask? ")

    if amount_questions > 0:
        break

# Starts the quiz
quiz()
