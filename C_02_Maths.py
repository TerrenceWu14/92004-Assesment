import math
import random

num_1 = random.randint(1, 100)
num_2 = random.randint(1, 100)

type = ["multiplication", "adding", "subtraction", "division"]

question_type = random.choice(type)

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

question = question_format
print(question)
print(f"Answer: {answer}")
